#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <limits>
#include <map>
#include <iomanip>
#include <chrono>
#include <thread>
#include <mutex>
#include <future>
#include <unordered_map>
#include <atomic>

//-----------------------------------------------------
// Resource Class
//-----------------------------------------------------
class Resource {
public:
    int RI, RA, RP, RW, RM, RL, RU;
    std::string RT;
    int RE;
    bool active;
    bool in_active_phase;
    int cycles;
    int turn_in_phase;
    int accumulated;

    Resource(int ri, int ra, int rp, int rw, int rm, int rl, int ru,
             const std::string& rt, int re = 0)
        : RI(ri), RA(ra), RP(rp), RW(rw), RM(rm), RL(rl), RU(ru),
          RT(rt), RE(re), active(true),
          in_active_phase(true), cycles(0),
          turn_in_phase(0), accumulated(0) {}

    Resource(const Resource& other) = default;

    // Advance resource turn and return its active status.
    bool advance_turn() {
        if (!active)
            return false;
        turn_in_phase++;
        if (in_active_phase) {
            if (turn_in_phase >= RW) {
                in_active_phase = false;
                turn_in_phase = 0;
                cycles++;
            }
        } else {
            if (turn_in_phase >= RM) {
                in_active_phase = true;
                turn_in_phase = 0;
            }
        }
        int total_turns = cycles * (RW + RM) + turn_in_phase;
        if (total_turns >= RL) {
            active = false;
        }
        return active;
    }

    // Calculate maintenance cost over lifetime
    double total_lifetime_cost() const {
        double cycles_total = static_cast<double>(RL) / (RW + RM);
        return RA + (RP * cycles_total);
    }
};

//-----------------------------------------------------
// Utility Structures
//-----------------------------------------------------
struct Turn {
    int TM, TX, TR;
    Turn(int tm, int tx, int tr) : TM(tm), TX(tx), TR(tr) {}
};

struct ResourceInfo {
    int RI, RA, RP, RW, RM, RL, RU;
    std::string RT;
    int RE;

    // Calculate efficiency score for quick heuristic evaluation
    double efficiency_score() const {
        double lifetime = static_cast<double>(RL);
        double active_ratio = static_cast<double>(RW) / (RW + RM);
        double power_per_cost = static_cast<double>(RU) / (RA + RP);
        return lifetime * active_ratio * power_per_cost;
    }
};

//-----------------------------------------------------
// Progress Logger with time estimation
//-----------------------------------------------------
class ProgressLogger {
private:
    std::vector<int> checkpoints;
    std::atomic<int> current_checkpoint;
    int total_steps;
    std::chrono::steady_clock::time_point start_time;
    bool first_update;
    std::mutex log_mutex;

public:
    ProgressLogger(int total, const std::vector<int>& custom_checkpoints = {})
        : total_steps(total), current_checkpoint(0), first_update(true) {
        if (custom_checkpoints.empty()) {
            for (int i = 5; i <= 100; i += 5) {
                checkpoints.push_back(i);
            }
        } else {
            checkpoints = custom_checkpoints;
        }
        start_time = std::chrono::steady_clock::now();
    }

    void update(int current_step) {
        if (first_update && current_step > 0) {
            std::lock_guard<std::mutex> lock(log_mutex);
            first_update = false;
        }

        double progress = (static_cast<double>(current_step) / total_steps) * 100.0;

        while (current_checkpoint.load() < checkpoints.size() &&
               progress >= checkpoints[current_checkpoint.load()]) {

            std::lock_guard<std::mutex> lock(log_mutex);

            if (current_checkpoint.load() >= checkpoints.size() ||
                progress < checkpoints[current_checkpoint.load()]) {
                break;
            }

            auto current_time = std::chrono::steady_clock::now();
            auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(
                current_time - start_time).count();
            double time_per_step = static_cast<double>(elapsed) / current_step;
            int steps_remaining = total_steps - current_step;
            int estimated_seconds = static_cast<int>(time_per_step * steps_remaining);

            int hours = estimated_seconds / 3600;
            int minutes = (estimated_seconds % 3600) / 60;
            int seconds = estimated_seconds % 60;

            std::stringstream time_str;
            if (hours)
                time_str << hours << "h ";
            if (minutes || hours)
                time_str << minutes << "m ";
            time_str << seconds << "s";

            std::cerr << "Progress: " << std::fixed << std::setprecision(1)
                      << checkpoints[current_checkpoint] << "% - Estimated time remaining: "
                      << time_str.str() << std::endl;
            current_checkpoint++;
        }
    }
};

//-----------------------------------------------------
// Evaluation Structures
//-----------------------------------------------------
struct EvaluationResult {
    double net_value;
    ResourceInfo* resource;
    EvaluationResult() : net_value(-std::numeric_limits<double>::infinity()), resource(nullptr) {}
    EvaluationResult(double net, ResourceInfo* res) : net_value(net), resource(res) {}
};

using SimulationKey = std::tuple<int, int, size_t>; // turn_idx, budget, active_resources hash
using SimCache = std::unordered_map<size_t, double>; // Simulation cache

//-----------------------------------------------------
// Helper functions for simulation effects
//-----------------------------------------------------
double compute_effect(const std::vector<Resource>& active_resources, const std::string& type) {
    double effect = 0;
    for (const auto& res : active_resources) {
        if (res.RT == type && res.active && res.in_active_phase) {
            effect += res.RE / 100.0;
        }
    }
    return effect;
}

int compute_powered(const std::vector<Resource>& resources, double a_effect) {
    int tot = 0;
    for (const auto& res : resources) {
        if (res.active && res.in_active_phase) {
            tot += static_cast<int>(std::floor(res.RU * (1 + a_effect)));
        }
    }
    return tot;
}

int adjust_turn(int base_value, double effect) {
    return std::max(0, static_cast<int>(std::floor(base_value * (1 + effect))));
}

// Hash function for resource vector (for caching)
size_t hash_resources(const std::vector<Resource>& resources) {
    size_t hash = resources.size();
    for (const auto& res : resources) {
        hash ^= res.RI + 0x9e3779b9 + (hash << 6) + (hash >> 2);
        hash ^= res.accumulated + 0x9e3779b9 + (hash << 6) + (hash >> 2);
        hash ^= (res.active ? 1 : 0) + 0x9e3779b9 + (hash << 6) + (hash >> 2);
        hash ^= (res.in_active_phase ? 1 : 0) + 0x9e3779b9 + (hash << 6) + (hash >> 2);
        hash ^= res.turn_in_phase + 0x9e3779b9 + (hash << 6) + (hash >> 2);
        hash ^= res.cycles + 0x9e3779b9 + (hash << 6) + (hash >> 2);
    }
    return hash;
}

//-----------------------------------------------------
// Recursively simulate future outcomes
//-----------------------------------------------------
double simulate_future(int turn_idx, int budget, std::vector<Resource> active_resources,
                       const std::vector<ResourceInfo>& resources, const std::vector<Turn>& turns,
                       SimCache& cache, int depth = 3) {

    if (depth == 0 || turn_idx >= turns.size())
        return 0.0;

    // Create a cache key
    size_t resources_hash = hash_resources(active_resources);
    size_t cache_key = (static_cast<size_t>(turn_idx) << 40) |
                       (static_cast<size_t>(budget) << 20) |
                       (resources_hash & 0xFFFFF);

    // Check cache
    auto it = cache.find(cache_key);
    if (it != cache.end()) {
        return it->second;
    }

    // Filter resources by budget
    std::vector<const ResourceInfo*> affordable_resources;
    for (const auto& r_info : resources) {
        if (r_info.RA <= budget) {
            affordable_resources.push_back(&r_info);
        }
    }

    // Sort by efficiency for faster pruning
    std::sort(affordable_resources.begin(), affordable_resources.end(),
        [](const ResourceInfo* a, const ResourceInfo* b) {
            return a->efficiency_score() > b->efficiency_score();
        });

    double best_profit = 0.0;
    for (const auto* r_info_ptr : affordable_resources) {
        const auto& r_info = *r_info_ptr;

        std::vector<Resource> temp_active = active_resources;
        Resource new_r(r_info.RI, r_info.RA, r_info.RP, r_info.RW, r_info.RM,
                       r_info.RL, r_info.RU, r_info.RT, r_info.RE);

        double c_effect = compute_effect(temp_active, "C");
        new_r.RL = std::max(1, static_cast<int>(std::floor(r_info.RL * (1 + c_effect))));
        temp_active.push_back(new_r);

        int sim_budget = budget - r_info.RA;
        int maintenance = 0;
        for (const auto& res : temp_active) {
            if (res.active)
                maintenance += res.RP;
        }
        sim_budget -= maintenance;

        const Turn& current_turn = turns[turn_idx];
        double a_effect = compute_effect(temp_active, "A");
        double b_effect = compute_effect(temp_active, "B");
        double d_effect = compute_effect(temp_active, "D");

        int effective_tm = adjust_turn(current_turn.TM, b_effect);
        int effective_tx = adjust_turn(current_turn.TX, b_effect);
        int effective_tr = adjust_turn(current_turn.TR, d_effect);

        int powered = compute_powered(temp_active, a_effect);
        int deficit = std::max(0, effective_tm - powered);
        for (auto& res : temp_active) {
            if (res.RT == "E" && res.active) {
                int withdraw = std::min(deficit, res.accumulated);
                deficit -= withdraw;
                res.accumulated -= withdraw;
                if (deficit == 0)
                    break;
            }
        }

        int profit = 0;
        if (deficit <= 0) {
            int served = std::min(powered, effective_tx);
            profit = served * effective_tr;
        }
        sim_budget += profit;

        // Early stopping if budget is negative
        if (sim_budget < 0) continue;

        int surplus = std::max(0, powered - effective_tx);
        std::vector<Resource*> accumulators;
        for (auto& res : temp_active) {
            if (res.RT == "E" && res.active)
                accumulators.push_back(&res);
        }
        if (!accumulators.empty() && surplus > 0) {
            int add_each = surplus / accumulators.size();
            for (auto* acc : accumulators)
                acc->accumulated += add_each;
        }

        std::vector<Resource> next_active;
        next_active.reserve(temp_active.size());
        for (auto& res : temp_active) {
            if (res.advance_turn())
                next_active.push_back(res);
        }
        double future_profit = simulate_future(turn_idx + 1, sim_budget, next_active, resources, turns, cache, depth - 1);
        best_profit = std::max(best_profit, profit + future_profit);
    }

    // Cache result
    cache[cache_key] = best_profit;
    return best_profit;
}

//-----------------------------------------------------
// Process a single turn
//-----------------------------------------------------
std::pair<EvaluationResult, std::vector<Resource>> process_turn(
    int turn_idx,
    int budget,
    std::vector<Resource>& active_resources,
    const std::vector<ResourceInfo>& resources,
    const std::vector<Turn>& turns)
{
    SimCache sim_cache;

    // Evaluate each resource option
    EvaluationResult best_overall;

    for (const auto& r_info : resources) {
        if (r_info.RA > budget)
            continue;

        std::vector<Resource> current_active = active_resources;
        Resource candidate(r_info.RI, r_info.RA, r_info.RP, r_info.RW, r_info.RM,
                          r_info.RL, r_info.RU, r_info.RT, r_info.RE);

        double c_effect = compute_effect(current_active, "C");
        candidate.RL = std::max(1, static_cast<int>(std::floor(r_info.RL * (1 + c_effect))));
        current_active.push_back(candidate);

        int sim_budget = budget - r_info.RA;
        int maintenance = 0;
        for (const auto& res : current_active)
            if (res.active) maintenance += res.RP;
        sim_budget -= maintenance;

        const Turn& cur_turn = turns[turn_idx];
        double a_effect = compute_effect(current_active, "A");
        double b_effect = compute_effect(current_active, "B");
        double d_effect = compute_effect(current_active, "D");

        int effective_tm = adjust_turn(cur_turn.TM, b_effect);
        int effective_tx = adjust_turn(cur_turn.TX, b_effect);
        int effective_tr = adjust_turn(cur_turn.TR, d_effect);

        int powered = compute_powered(current_active, a_effect);
        int deficit = std::max(0, effective_tm - powered);
        for (auto& res : current_active) {
            if (res.RT == "E" && res.active && res.in_active_phase) {
                int withdraw = std::min(deficit, res.accumulated);
                res.accumulated -= withdraw;
                deficit -= withdraw;
                if (deficit == 0) break;
            }
        }

        int profit = 0;
        if (deficit <= 0) {
            int served = std::min(powered, effective_tx);
            profit = served * effective_tr;
        }
        sim_budget += profit;

        int surplus = std::max(0, powered - effective_tx);
        std::vector<Resource*> accumulators;
        for (auto& res : current_active)
            if (res.RT == "E" && res.active && res.in_active_phase)
                accumulators.push_back(&res);
        if (!accumulators.empty() && surplus > 0) {
            int add_each = surplus / accumulators.size();
            for (auto* acc : accumulators)
                acc->accumulated += add_each;
        }

        std::vector<Resource> next_active;
        next_active.reserve(current_active.size());
        for (auto& res : current_active)
            if (res.advance_turn())
                next_active.push_back(res);

        double future_profit = simulate_future(turn_idx + 1, sim_budget, next_active, resources, turns, sim_cache, 2);

        // More sophisticated evaluation
        double roi = profit / (r_info.RA > 0 ? r_info.RA : 1.0);
        double lifetime_value = candidate.RL / (candidate.RW + candidate.RM) * profit;
        double total_net = profit + future_profit - r_info.RA;

        // Weighted scoring
        double score = total_net * 0.6 + roi * 0.2 + lifetime_value * 0.2;

        if (score > best_overall.net_value) {
            best_overall.net_value = score;
            best_overall.resource = const_cast<ResourceInfo*>(&r_info);

            if (sim_budget <= 0) { // Break early if we find a profitable option
                break;
            }
        }
    }

    // Apply the best resource selection
    std::vector<Resource> updated_resources = active_resources;

    if (best_overall.resource) {
        double c_effect = compute_effect(active_resources, "C");
        int new_rl = std::max(1, static_cast<int>(std::floor(best_overall.resource->RL * (1 + c_effect))));
        Resource new_resource(best_overall.resource->RI, best_overall.resource->RA, best_overall.resource->RP,
                              best_overall.resource->RW, best_overall.resource->RM, new_rl,
                              best_overall.resource->RU, best_overall.resource->RT, best_overall.resource->RE);
        updated_resources.push_back(new_resource);
    }

    return {best_overall, updated_resources};
}

//-----------------------------------------------------
// Main Function
//-----------------------------------------------------
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int D, R, T;
    std::cin >> D >> R >> T;

    std::vector<ResourceInfo> resources;
    resources.reserve(R);
    for (int i = 0; i < R; i++) {
        ResourceInfo info;
        std::cin >> info.RI >> info.RA >> info.RP >> info.RW >> info.RM >> info.RL >> info.RU;
        std::cin >> info.RT;
        if (info.RT != "X")
            std::cin >> info.RE;
        else
            info.RE = 0;
        resources.push_back(info);
    }

    std::vector<Turn> turns;
    turns.reserve(T);
    for (int i = 0; i < T; i++) {
        int tm, tx, tr;
        std::cin >> tm >> tx >> tr;
        turns.emplace_back(tm, tx, tr);
    }

    int num_threads = std::thread::hardware_concurrency();
    num_threads = num_threads > 0 ? num_threads : 4;

    std::cerr << "Starting Green Revolution Game solver with " << num_threads << " threads..." << std::endl;
    ProgressLogger logger(T);

    std::vector<Resource> active_resources;
    std::vector<std::string> output;
    int budget = D;

    for (int turn_idx = 0; turn_idx < T; turn_idx++) {
        auto [best_result, updated_resources] = process_turn(turn_idx, budget, active_resources, resources, turns);

        if (best_result.resource) {
            budget -= best_result.resource->RA;
            active_resources = updated_resources;

            std::stringstream ss;
            ss << turn_idx << " 1 " << best_result.resource->RI;
            output.push_back(ss.str());
        }

        int maintenance = 0;
        for (const auto& res : active_resources)
            if (res.active)
                maintenance += res.RP;
        budget -= maintenance;

        double a_effect = compute_effect(active_resources, "A");
        double b_effect = compute_effect(active_resources, "B");
        double d_effect = compute_effect(active_resources, "D");

        const Turn& cur_turn = turns[turn_idx];
        int effective_tm = adjust_turn(cur_turn.TM, b_effect);
        int effective_tx = adjust_turn(cur_turn.TX, b_effect);
        int effective_tr = adjust_turn(cur_turn.TR, d_effect);

        int powered = compute_powered(active_resources, a_effect);
        int deficit = std::max(0, effective_tm - powered);
        for (auto& res : active_resources) {
            if (res.RT == "E" && res.active && res.in_active_phase) {
                int withdraw = std::min(deficit, res.accumulated);
                res.accumulated -= withdraw;
                deficit -= withdraw;
                if (deficit == 0)
                    break;
            }
        }

        int profit = 0;
        if (deficit <= 0) {
            int served = std::min(powered, effective_tx);
            profit = served * effective_tr;
        }
        budget += profit;

        int surplus = std::max(0, powered - effective_tx);
        std::vector<Resource*> accumulators;
        for (auto& res : active_resources)
            if (res.RT == "E" && res.active && res.in_active_phase)
                accumulators.push_back(&res);
        if (!accumulators.empty() && surplus > 0) {
            int add_each = surplus / accumulators.size();
            for (auto* acc : accumulators)
                acc->accumulated += add_each;
        }

        std::vector<Resource> new_active;
        new_active.reserve(active_resources.size());
        for (auto& res : active_resources)
            if (res.advance_turn())
                new_active.push_back(res);
        active_resources = new_active;

        logger.update(turn_idx + 1);
    }

    std::cerr << "Calculation complete. Writing solution..." << std::endl;
    for (const auto& line : output)
        std::cout << line << std::endl;
    std::cerr << "Solution output complete." << std::endl;

    return 0;
}

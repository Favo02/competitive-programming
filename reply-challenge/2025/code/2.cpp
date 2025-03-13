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
};

//-----------------------------------------------------
// Progress Logger with time estimation
//-----------------------------------------------------
class ProgressLogger {
private:
    std::vector<int> checkpoints;
    int current_checkpoint;
    int total_steps;
    std::chrono::steady_clock::time_point start_time;
    bool first_update;

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
        if (first_update && current_step > 0)
            first_update = false;

        double progress = (static_cast<double>(current_step) / total_steps) * 100.0;
        while (current_checkpoint < checkpoints.size() && progress >= checkpoints[current_checkpoint]) {
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

//-----------------------------------------------------
// Recursively simulate future outcomes
//-----------------------------------------------------
double simulate_future(int turn_idx, int budget, std::vector<Resource> active_resources,
                       const std::vector<ResourceInfo>& resources, const std::vector<Turn>& turns,
                       int depth = 3) {
    if (depth == 0 || turn_idx >= turns.size())
        return 0.0;

    double best_profit = 0.0;
    for (const auto& r_info : resources) {
        if (r_info.RA > budget)
            continue;

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
        for (auto& res : temp_active) {
            if (res.advance_turn())
                next_active.push_back(res);
        }
        double future_profit = simulate_future(turn_idx + 1, sim_budget, next_active, resources, turns, depth - 1);
        best_profit = std::max(best_profit, profit + future_profit);
    }
    return best_profit;
}

//-----------------------------------------------------
// Evaluate a single resource option
//-----------------------------------------------------
EvaluationResult evaluate_resource(const ResourceInfo& r_info, int budget,
                                   const std::vector<Resource>& active_resources,
                                   const std::vector<ResourceInfo>& all_resources,
                                   const std::vector<Turn>& turns, int turn_idx) {
    if (r_info.RA > budget)
        return EvaluationResult();

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
        if (res.RT == "E" && res.active) {
            int withdraw = std::min(deficit, res.accumulated);
            deficit -= withdraw;
            res.accumulated -= withdraw;
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
    int e_count = 0;
    for (const auto& res : current_active)
        if (res.RT == "E" && res.active) e_count++;

    if (e_count > 0 && surplus > 0) {
        int add_each = surplus / e_count;
        for (auto& res : current_active)
            if (res.RT == "E" && res.active)
                res.accumulated += add_each;
    }

    std::vector<Resource> next_active;
    for (auto& res : current_active)
        if (res.advance_turn())
            next_active.push_back(res);

    double future_profit = simulate_future(turn_idx + 1, sim_budget, next_active, all_resources, turns, 2);
    double total_periodic_cost = r_info.RP * (candidate.RL / (candidate.RW + candidate.RM));
    double total_net = (profit - r_info.RA - total_periodic_cost) + future_profit;

    return EvaluationResult(total_net, const_cast<ResourceInfo*>(&r_info));
}

//-----------------------------------------------------
// Get the optimal number of threads
//-----------------------------------------------------
int get_optimal_thread_count() {
    int hw_threads = std::thread::hardware_concurrency();
    return hw_threads > 0 ? hw_threads : 4;
}

//-----------------------------------------------------
// Main Function
//-----------------------------------------------------
int main() {
    int D, R, T;
    std::cin >> D >> R >> T;

    std::vector<ResourceInfo> resources;
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
    for (int i = 0; i < T; i++) {
        int tm, tx, tr;
        std::cin >> tm >> tx >> tr;
        turns.emplace_back(tm, tx, tr);
    }

    int num_threads = get_optimal_thread_count();
    std::cerr << "Starting Green Revolution Game solver with " << num_threads << " threads..." << std::endl;
    ProgressLogger logger(T);

    std::vector<Resource> active_resources;
    std::vector<std::string> output;
    int budget = D;

    for (int turn_idx = 0; turn_idx < T; turn_idx++) {
        std::vector<std::future<EvaluationResult>> futures;
        std::vector<std::vector<ResourceInfo>> resource_chunks(num_threads);

        // Distribute resources among threads
        for (size_t i = 0; i < resources.size(); i++) {
            resource_chunks[i % num_threads].push_back(resources[i]);
        }

        // Launch asynchronous evaluations.
        for (int tid = 0; tid < num_threads; tid++) {
            futures.push_back(std::async(std::launch::async, [&, tid]() {
                EvaluationResult best_local;
                for (const auto& r_info : resource_chunks[tid]) {
                    EvaluationResult res = evaluate_resource(r_info, budget, active_resources, resources, turns, turn_idx);
                    if (res.net_value > best_local.net_value)
                        best_local = res;
                }
                return best_local;
            }));
        }

        EvaluationResult best_overall;
        for (auto& fut : futures) {
            EvaluationResult res = fut.get();
            if (res.net_value > best_overall.net_value)
                best_overall = res;
        }

        if (best_overall.resource) {
            double c_effect = compute_effect(active_resources, "C");
            int new_rl = std::max(1, static_cast<int>(std::floor(best_overall.resource->RL * (1 + c_effect))));
            Resource new_resource(best_overall.resource->RI, best_overall.resource->RA, best_overall.resource->RP,
                                  best_overall.resource->RW, best_overall.resource->RM, new_rl,
                                  best_overall.resource->RU, best_overall.resource->RT, best_overall.resource->RE);

            active_resources.push_back(new_resource);
            budget -= best_overall.resource->RA;

            std::stringstream ss;
            ss << turn_idx << " 1 " << best_overall.resource->RI;
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

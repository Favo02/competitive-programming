#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <limits>
#include <map>
#include <iomanip> // For output formatting
#include <chrono>  // For time estimation
#include <thread>  // For multithreading
#include <mutex>   // For thread synchronization
#include <future>  // For async tasks

class Resource {
public:
    int RI, RA, RP, RW, RM, RL, RU;
    std::string RT;
    int RE;
    bool active;
    bool active_phase;
    int cycles;
    int current_turn_in_phase;
    int accumulated;

    Resource(int ri, int ra, int rp, int rw, int rm, int rl, int ru, const std::string& rt, int re = 0) 
        : RI(ri), RA(ra), RP(rp), RW(rw), RM(rm), RL(rl), RU(ru), RT(rt), RE(re),
          active(true), active_phase(true), cycles(0), current_turn_in_phase(0), accumulated(0) {}

    Resource(const Resource& other) 
        : RI(other.RI), RA(other.RA), RP(other.RP), RW(other.RW), RM(other.RM), RL(other.RL), 
          RU(other.RU), RT(other.RT), RE(other.RE), active(other.active), 
          active_phase(other.active_phase), cycles(other.cycles), 
          current_turn_in_phase(other.current_turn_in_phase), accumulated(other.accumulated) {}

    bool advance_turn() {
        if (!active) {
            return false;
        }
        current_turn_in_phase++;
        if (active_phase) {
            if (current_turn_in_phase >= RW) {
                active_phase = false;
                current_turn_in_phase = 0;
                cycles++;
            }
        } else {
            if (current_turn_in_phase >= RM) {
                active_phase = true;
                current_turn_in_phase = 0;
            }
        }
        int total_turns = cycles * (RW + RM) + current_turn_in_phase;
        if (total_turns >= RL) {
            active = false;
        }
        return active;
    }
};

struct Turn {
    int TM, TX, TR;
    Turn(int tm, int tx, int tr) : TM(tm), TX(tx), TR(tr) {}
};

struct ResourceInfo {
    int RI, RA, RP, RW, RM, RL, RU;
    std::string RT;
    int RE;
};

// Enhanced progress logger class with time estimation
class ProgressLogger {
private:
    std::vector<int> checkpoints;
    int current_checkpoint;
    int total_steps;
    std::chrono::steady_clock::time_point start_time;
    bool first_update;
    
public:
    ProgressLogger(int total, const std::vector<int>& check_points = {}) 
        : total_steps(total), current_checkpoint(0), first_update(true) {
        // If no checkpoints provided, create checkpoints from 1 to 100
        if (check_points.empty()) {
            for (int i = 5; i <= 100; i += 5) {  // Using 5% increments to reduce output
                checkpoints.push_back(i);
            }
        } else {
            checkpoints = check_points;
        }
        start_time = std::chrono::steady_clock::now();
    }
    
    void update(int current_step) {
        if (first_update && current_step > 0) {
            first_update = false;
        }
        
        double progress = (static_cast<double>(current_step) / total_steps) * 100.0;
        
        while (current_checkpoint < checkpoints.size() && 
               progress >= checkpoints[current_checkpoint]) {
            auto current_time = std::chrono::steady_clock::now();
            auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(
                current_time - start_time).count();
            
            // Calculate estimated time remaining
            double time_per_step = static_cast<double>(elapsed) / current_step;
            int steps_remaining = total_steps - current_step;
            int estimated_seconds = static_cast<int>(time_per_step * steps_remaining);
            
            // Format time remaining
            int hours = estimated_seconds / 3600;
            int minutes = (estimated_seconds % 3600) / 60;
            int seconds = estimated_seconds % 60;
            
            std::stringstream time_str;
            if (hours > 0) {
                time_str << hours << "h ";
            }
            if (minutes > 0 || hours > 0) {
                time_str << minutes << "m ";
            }
            time_str << seconds << "s";
            
            std::cerr << "Progress: " << std::fixed << std::setprecision(1) 
                      << checkpoints[current_checkpoint] << "% - Estimated time remaining: " 
                      << time_str.str() << std::endl;
            
            current_checkpoint++;
        }
    }
};

// Structure to hold evaluation results
struct EvaluationResult {
    double net_value;
    ResourceInfo* resource;
    
    EvaluationResult() : net_value(-std::numeric_limits<double>::infinity()), resource(nullptr) {}
    
    EvaluationResult(double net, ResourceInfo* res) : net_value(net), resource(res) {}
};

// Increased depth from 3 to 5
double simulate_future(int turn_num, int budget, std::vector<Resource> active_resources, 
                      const std::vector<ResourceInfo>& resources, const std::vector<Turn>& turns, int depth = 5) {
    if (depth == 0 || turn_num >= turns.size()) {
        return 0;
    }

    // For deeper levels, use a less exhaustive search to maintain performance
    // When depth is high, limit the number of resources we consider
    int max_resources_to_consider = (depth > 3) ? 3 : resources.size();
    
    // Sort resources by a heuristic value (RU/RA ratio as a simple ROI metric)
    std::vector<std::pair<double, const ResourceInfo*>> resource_value;
    for (const auto& r_info : resources) {
        if (r_info.RA <= budget) {
            // Consider RU/RA as return on investment, weighted by active period ratio
            double active_ratio = static_cast<double>(r_info.RW) / (r_info.RW + r_info.RM);
            double roi = (static_cast<double>(r_info.RU) / r_info.RA) * active_ratio;
            // Prioritize E-type resources in early turns for long-term benefit
            if (r_info.RT == "E" && turn_num < turns.size() / 2) {
                roi *= 1.5;  // Boost priority for accumulators
            }
            resource_value.push_back({roi, &r_info});
        }
    }
    
    // Sort by ROI descending
    std::sort(resource_value.begin(), resource_value.end(), 
              [](const auto& a, const auto& b) { return a.first > b.first; });
    
    // Limit the number of resources to consider
    int resources_to_check = std::min(max_resources_to_consider, static_cast<int>(resource_value.size()));
    
    double best_profit = 0;
    
    // Also consider the option of not buying anything
    {
        int maintenance = 0;
        for (const auto& res : active_resources) {
            if (res.active) {
                maintenance += res.RP;
            }
        }
        int sim_budget = budget - maintenance;
        
        const Turn& current_turn = turns[turn_num];
        
        // Calculate effects
        double a_effect = 0, b_effect = 0, d_effect = 0;
        for (const auto& res : active_resources) {
            if (res.active && res.active_phase) {
                if (res.RT == "A") a_effect += res.RE / 100.0;
                if (res.RT == "B") b_effect += res.RE / 100.0;
                if (res.RT == "D") d_effect += res.RE / 100.0;
            }
        }
        
        int effective_tm = std::max(0, static_cast<int>(std::floor(current_turn.TM * (1 + b_effect))));
        int effective_tx = std::max(0, static_cast<int>(std::floor(current_turn.TX * (1 + b_effect))));
        int effective_tr = std::max(0, static_cast<int>(std::floor(current_turn.TR * (1 + d_effect))));
        
        int powered = 0;
        for (const auto& res : active_resources) {
            if (res.active && res.active_phase) {
                powered += static_cast<int>(std::floor(res.RU * (1 + a_effect)));
            }
        }
        
        std::vector<Resource> temp_active = active_resources;
        int deficit = std::max(0, effective_tm - powered);
        for (auto& res : temp_active) {
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
        std::vector<Resource*> accumulators;
        for (auto& res : temp_active) {
            if (res.RT == "E" && res.active) {
                accumulators.push_back(&res);
            }
        }
        
        if (!accumulators.empty() && surplus > 0) {
            int add_each = surplus / accumulators.size();
            for (auto& acc : accumulators) {
                acc->accumulated += add_each;
            }
        }
        
        std::vector<Resource> next_active;
        for (auto& res : temp_active) {
            if (res.advance_turn()) {
                next_active.push_back(res);
            }
        }
        
        double future_profit = simulate_future(turn_num + 1, sim_budget, next_active, resources, turns, depth - 1);
        double total_profit = profit + future_profit;
        
        best_profit = total_profit;
    }
    
    // Check top N resources by ROI
    for (int i = 0; i < resources_to_check; i++) {
        const auto& r_info = *resource_value[i].second;
        
        std::vector<Resource> temp_active = active_resources;
        Resource new_r(r_info.RI, r_info.RA, r_info.RP, r_info.RW, r_info.RM, r_info.RL, r_info.RU, r_info.RT, r_info.RE);

        // Calculate C effect on new resource lifespan
        double c_effect = 0;
        for (const auto& res : temp_active) {
            if (res.RT == "C" && res.active_phase && res.active) {
                c_effect += res.RE / 100.0;
            }
        }
        new_r.RL = std::max(1, static_cast<int>(std::floor(r_info.RL * (1 + c_effect))));
        temp_active.push_back(new_r);

        int sim_budget = budget - r_info.RA;
        int maintenance = 0;
        for (const auto& res : temp_active) {
            if (res.active) {
                maintenance += res.RP;
            }
        }
        sim_budget -= maintenance;

        const Turn& current_turn = turns[turn_num];
        
        // Calculate effects
        double a_effect = 0, b_effect = 0, d_effect = 0;
        for (const auto& res : temp_active) {
            if (res.active && res.active_phase) {
                if (res.RT == "A") a_effect += res.RE / 100.0;
                if (res.RT == "B") b_effect += res.RE / 100.0;
                if (res.RT == "D") d_effect += res.RE / 100.0;
            }
        }

        int effective_tm = std::max(0, static_cast<int>(std::floor(current_turn.TM * (1 + b_effect))));
        int effective_tx = std::max(0, static_cast<int>(std::floor(current_turn.TX * (1 + b_effect))));
        int effective_tr = std::max(0, static_cast<int>(std::floor(current_turn.TR * (1 + d_effect))));

        int powered = 0;
        for (const auto& res : temp_active) {
            if (res.active && res.active_phase) {
                powered += static_cast<int>(std::floor(res.RU * (1 + a_effect)));
            }
        }

        int deficit = std::max(0, effective_tm - powered);
        for (auto& res : temp_active) {
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
        std::vector<Resource*> accumulators;
        for (auto& res : temp_active) {
            if (res.RT == "E" && res.active) {
                accumulators.push_back(&res);
            }
        }
        
        if (!accumulators.empty() && surplus > 0) {
            int add_each = surplus / accumulators.size();
            for (auto& acc : accumulators) {
                acc->accumulated += add_each;
            }
        }

        std::vector<Resource> next_active;
        for (auto& res : temp_active) {
            if (res.advance_turn()) {
                next_active.push_back(res);
            }
        }

        double future_profit = simulate_future(turn_num + 1, sim_budget, next_active, resources, turns, depth - 1);
        double total_profit = profit + future_profit;

        if (total_profit > best_profit) {
            best_profit = total_profit;
        }
    }

    return best_profit;
}

// Function to evaluate a single resource - separated for parallelization
EvaluationResult evaluate_resource(
    const ResourceInfo& r_info,
    int budget,
    const std::vector<Resource>& active_resources,
    const std::vector<ResourceInfo>& all_resources,
    const std::vector<Turn>& turns,
    int turn_num
) {
    if (r_info.RA > budget) {
        return EvaluationResult();
    }
    
    std::vector<Resource> current_active = active_resources;
    Resource temp_r(r_info.RI, r_info.RA, r_info.RP, r_info.RW, r_info.RM, r_info.RL, r_info.RU, r_info.RT, r_info.RE);
    
    // Apply C effect on resource lifespan
    double c_effect = 0;
    for (const auto& res : current_active) {
        if (res.RT == "C" && res.active_phase && res.active) {
            c_effect += res.RE / 100.0;
        }
    }
    temp_r.RL = std::max(1, static_cast<int>(std::floor(r_info.RL * (1 + c_effect))));
    current_active.push_back(temp_r);
    
    int sim_budget = budget - r_info.RA;
    int maintenance = 0;
    for (const auto& res : current_active) {
        if (res.active) {
            maintenance += res.RP;
        }
    }
    sim_budget -= maintenance;
    
    const Turn& current_turn = turns[turn_num];
    
    // Calculate effects
    double a_effect = 0, b_effect = 0, d_effect = 0;
    for (const auto& res : current_active) {
        if (res.active && res.active_phase) {
            if (res.RT == "A") a_effect += res.RE / 100.0;
            if (res.RT == "B") b_effect += res.RE / 100.0;
            if (res.RT == "D") d_effect += res.RE / 100.0;
        }
    }
    
    int effective_tm = std::max(0, static_cast<int>(std::floor(current_turn.TM * (1 + b_effect))));
    int effective_tx = std::max(0, static_cast<int>(std::floor(current_turn.TX * (1 + b_effect))));
    int effective_tr = std::max(0, static_cast<int>(std::floor(current_turn.TR * (1 + d_effect))));
    
    int powered = 0;
    for (const auto& res : current_active) {
        if (res.active && res.active_phase) {
            powered += static_cast<int>(std::floor(res.RU * (1 + a_effect)));
        }
    }
    
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
    for (const auto& res : current_active) {
        if (res.RT == "E" && res.active) {
            e_count++;
        }
    }
    
    if (e_count > 0 && surplus > 0) {
        int add_each = surplus / e_count;
        for (auto& res : current_active) {
            if (res.RT == "E" && res.active) {
                res.accumulated += add_each;
            }
        }
    }
    
    std::vector<Resource> next_active;
    for (auto& res : current_active) {
        if (res.advance_turn()) {
            next_active.push_back(res);
        }
    }
    
    // Increase simulation depth from 2 to 4
    double future_profit = simulate_future(turn_num + 1, sim_budget, next_active, all_resources, turns, 4);
    double total_periodic_cost = r_info.RP * (temp_r.RL / (temp_r.RW + temp_r.RM));
    double total_net = (profit - r_info.RA - total_periodic_cost) + future_profit;
    
    // Create a non-const pointer for the result
    ResourceInfo* r_ptr = const_cast<ResourceInfo*>(&r_info);
    return EvaluationResult(total_net, r_ptr);
}

// Add adaptive depth control based on turns remaining
int calculate_simulation_depth(int turn_num, int total_turns) {
    // Use deeper simulation for early turns, shallower for later turns
    int turns_remaining = total_turns - turn_num - 1;
    
    if (turns_remaining <= 2) {
        return std::min(2, turns_remaining); // Very short horizon at the end
    } else if (turns_remaining <= 5) {
        return 3; // Medium depth for middle-late game
    } else if (turns_remaining <= 10) {
        return 4; // Deeper for middle game
    } else {
        return 5; // Maximum depth for early game
    }
}

// Determine the optimal number of threads based on hardware
int get_optimal_thread_count() {
    int hardware_threads = std::thread::hardware_concurrency();
    // If we can't determine the hardware threads, default to 4
    return hardware_threads > 0 ? hardware_threads : 4;
}

int main() {
    int D, R, T;
    std::cin >> D >> R >> T;

    std::vector<ResourceInfo> resources;
    for (int i = 0; i < R; i++) {
        ResourceInfo info;
        std::cin >> info.RI >> info.RA >> info.RP >> info.RW >> info.RM >> info.RL >> info.RU;
        
        std::string rt;
        std::cin >> rt;
        info.RT = rt;
        
        if (rt != "X") {
            std::cin >> info.RE;
        } else {
            info.RE = 0;
        }
        
        resources.push_back(info);
    }

    std::vector<Turn> turns;
    for (int i = 0; i < T; i++) {
        int tm, tx, tr;
        std::cin >> tm >> tx >> tr;
        turns.emplace_back(tm, tx, tr);
    }

    // Get optimal thread count
    int num_threads = get_optimal_thread_count();
    std::cerr << "Starting Green Revolution Game solver with " << num_threads << " threads..." << std::endl;

    // Initialize progress logger
    ProgressLogger logger(T);

    std::vector<Resource> active_resources;
    std::vector<std::string> output;
    int budget = D;

    for (int turn_num = 0; turn_num < T; turn_num++) {
        // Calculate adaptive simulation depth based on game progress
        int sim_depth = calculate_simulation_depth(turn_num, T);
        std::cerr << "Turn " << turn_num << " - Using simulation depth: " << sim_depth << std::endl;
        
        // This is the part we can parallelize
        // Each thread will evaluate a subset of resources
        std::vector<std::future<EvaluationResult>> futures;
        std::mutex best_result_mutex;
        
        // Divide resources among threads
        std::vector<std::vector<ResourceInfo>> resource_chunks;
        resource_chunks.resize(num_threads);
        
        for (size_t i = 0; i < resources.size(); ++i) {
            resource_chunks[i % num_threads].push_back(resources[i]);
        }
        
        // Launch threads to evaluate resources in parallel
        for (int thread_id = 0; thread_id < num_threads; ++thread_id) {
            futures.push_back(std::async(std::launch::async, [&, thread_id, sim_depth]() {
                EvaluationResult best_result;
                
                for (const auto& r_info : resource_chunks[thread_id]) {
                    EvaluationResult result = evaluate_resource(
                        r_info, budget, active_resources, resources, turns, turn_num);
                    
                    if (result.net_value > best_result.net_value) {
                        best_result = result;
                    }
                }
                
                return best_result;
            }));
        }
        
        // Collect results from all threads
        EvaluationResult best_overall;
        for (auto& future : futures) {
            EvaluationResult result = future.get();
            if (result.net_value > best_overall.net_value) {
                best_overall = result;
            }
        }
        
        // Process the best result
        ResourceInfo* best_r = best_overall.resource;
        
        if (best_r) {
            double c_effect = 0;
            for (const auto& res : active_resources) {
                if (res.RT == "C" && res.active_phase && res.active) {
                    c_effect += res.RE / 100.0;
                }
            }
            
            int new_rl = std::max(1, static_cast<int>(std::floor(best_r->RL * (1 + c_effect))));
            Resource new_resource(best_r->RI, best_r->RA, best_r->RP, best_r->RW, best_r->RM, 
                                 new_rl, best_r->RU, best_r->RT, best_r->RE);
            
            active_resources.push_back(new_resource);
            budget -= best_r->RA;
            
            std::stringstream ss;
            ss << turn_num << " 1 " << best_r->RI;
            output.push_back(ss.str());
        }
        
        int maintenance = 0;
        for (const auto& res : active_resources) {
            if (res.active) {
                maintenance += res.RP;
            }
        }
        budget -= maintenance;
        
        double a_effect = 0, b_effect = 0, d_effect = 0;
        for (const auto& res : active_resources) {
            if (res.active && res.active_phase) {
                if (res.RT == "A") a_effect += res.RE / 100.0;
                if (res.RT == "B") b_effect += res.RE / 100.0;
                if (res.RT == "D") d_effect += res.RE / 100.0;
            }
        }
        
        const Turn& current_turn = turns[turn_num];
        int effective_tm = std::max(0, static_cast<int>(std::floor(current_turn.TM * (1 + b_effect))));
        int effective_tx = std::max(0, static_cast<int>(std::floor(current_turn.TX * (1 + b_effect))));
        int effective_tr = std::max(0, static_cast<int>(std::floor(current_turn.TR * (1 + d_effect))));
        
        int powered = 0;
        for (const auto& res : active_resources) {
            if (res.active && res.active_phase) {
                powered += static_cast<int>(std::floor(res.RU * (1 + a_effect)));
            }
        }
        
        int deficit = std::max(0, effective_tm - powered);
        for (auto& res : active_resources) {
            if (res.RT == "E" && res.active && res.active_phase) {
                if (deficit <= 0) break;
                int withdraw = std::min(deficit, res.accumulated);
                res.accumulated -= withdraw;
                deficit -= withdraw;
            }
        }
        
        int profit = 0;
        if (deficit <= 0) {
            int served = std::min(powered, effective_tx);
            profit = served * effective_tr;
        }
        
        budget += profit;
        
        int surplus = std::max(0, powered - effective_tx);
        std::vector<Resource*> e_accs;
        for (auto& res : active_resources) {
            if (res.RT == "E" && res.active && res.active_phase) {
                e_accs.push_back(&res);
            }
        }
        
        if (!e_accs.empty() && surplus > 0) {
            int add_each = surplus / e_accs.size();
            for (auto* acc : e_accs) {
                acc->accumulated += add_each;
            }
        }
        
        std::vector<Resource> new_active;
        for (auto& res : active_resources) {
            if (res.advance_turn()) {
                new_active.push_back(res);
            }
        }
        active_resources = new_active;
        
        // Update progress after each turn
        logger.update(turn_num + 1);
    }
    
    std::cerr << "Calculation complete. Writing solution..." << std::endl;
    
    for (const auto& line : output) {
        std::cout << line << std::endl;
    }
    
    std::cerr << "Solution output complete." << std::endl;
    
    return 0;
}
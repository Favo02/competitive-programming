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
#include <queue>
#include <unordered_map>
#include <memory>

// Resource class with optimized memory footprint
class Resource {
public:
    int RI, RA, RP, RW, RM, RL, RU;
    char RT;  // Using char instead of string saves memory
    int RE;
    bool active;
    bool active_phase;
    int cycles;
    int current_turn_in_phase;
    int accumulated;

    Resource(int ri, int ra, int rp, int rw, int rm, int rl, int ru, char rt, int re = 0) 
        : RI(ri), RA(ra), RP(rp), RW(rw), RM(rm), RL(rl), RU(ru), RT(rt), RE(re),
          active(true), active_phase(true), cycles(0), current_turn_in_phase(0), accumulated(0) {}

    Resource(const Resource& other) = default;  // Use default copy constructor

    bool advance_turn() {
        if (!active) return false;
        
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
        
        // More efficient calculation of total turns
        if (cycles * (RW + RM) + current_turn_in_phase >= RL) {
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
    char RT;  // Changed from string to char
    int RE;
    
    // Calculate a resource efficiency score for sorting and prioritization
    double efficiency_score() const {
        // Base efficiency is buildings powered per cost unit
        double base_efficiency = static_cast<double>(RU) / (RA + RP);
        
        // Adjust for resource lifespan and active/inactive ratio
        double active_ratio = static_cast<double>(RW) / (RW + RM);
        double lifespan_factor = static_cast<double>(RL) / (RW + RM);
        
        // Special resource type bonuses
        double type_bonus = 1.0;
        if (RT == 'E') type_bonus = 2.0;      // Accumulators are very valuable
        else if (RT == 'D') type_bonus = 1.5; // Profit boosters are valuable
        else if (RT == 'A') type_bonus = 1.3; // Building boosters are good
        
        return base_efficiency * active_ratio * lifespan_factor * type_bonus;
    }
};

// Progress logger with reduced output frequency
class ProgressLogger {
private:
    int total_steps;
    int last_percentage = 0;
    std::chrono::steady_clock::time_point start_time;
    
public:
    ProgressLogger(int total) : total_steps(total) {
        start_time = std::chrono::steady_clock::now();
    }
    
    void update(int current_step) {
        // Only log when percentage changes by at least 10%
        int current_percentage = (current_step * 100) / total_steps;
        if (current_percentage - last_percentage >= 10 || current_step == total_steps) {
            auto current_time = std::chrono::steady_clock::now();
            auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(current_time - start_time).count();
            
            // Estimate remaining time
            double time_per_step = static_cast<double>(elapsed) / current_step;
            int steps_remaining = total_steps - current_step;
            int estimated_seconds = static_cast<int>(time_per_step * steps_remaining);
            
            // Format time
            int hours = estimated_seconds / 3600;
            int minutes = (estimated_seconds % 3600) / 60;
            int seconds = estimated_seconds % 60;
            
            std::stringstream time_str;
            if (hours > 0) time_str << hours << "h ";
            if (minutes > 0 || hours > 0) time_str << minutes << "m ";
            time_str << seconds << "s";
            
            std::cerr << "Progress: " << current_percentage << "% - ETA: " 
                      << time_str.str() << std::endl;
            
            last_percentage = current_percentage;
        }
    }
};

// Game state cache to avoid recalculating states
using StateKey = std::tuple<int, int, std::vector<int>>;  // turn, budget, resource counts
struct StateKeyHash {
    std::size_t operator()(const StateKey& key) const {
        const auto& [turn, budget, resources] = key;
        std::size_t h = std::hash<int>{}(turn) ^ (std::hash<int>{}(budget) << 1);
        for (const auto& r : resources) {
            h ^= (std::hash<int>{}(r) << 1);
        }
        return h;
    }
};

// Optimized simulation using memoization and pruning
class GameSimulator {
private:
    const std::vector<ResourceInfo>& resources;
    const std::vector<Turn>& turns;
    std::unordered_map<StateKey, double, StateKeyHash> memo_cache;
    
    // Convert active resources to a state key for caching
    StateKey make_state_key(int turn, int budget, const std::vector<Resource>& active) {
        std::vector<int> resource_counts(resources.size(), 0);
        for (const auto& res : active) {
            int index = 0;
            for (size_t i = 0; i < resources.size(); i++) {
                if (resources[i].RI == res.RI) {
                    index = i;
                    break;
                }
            }
            resource_counts[index]++;
        }
        return {turn, budget, resource_counts};
    }
    
public:
    GameSimulator(const std::vector<ResourceInfo>& res, const std::vector<Turn>& t)
        : resources(res), turns(t) {}
    
    double simulate(int turn_num, int budget, const std::vector<Resource>& active_resources, int depth) {
        if (depth == 0 || turn_num >= turns.size()) {
            return 0;
        }
        
        // Try to get result from cache
        StateKey key = make_state_key(turn_num, budget, active_resources);
        auto it = memo_cache.find(key);
        if (it != memo_cache.end()) {
            return it->second;
        }
        
        // Base case - calculate profit for not buying anything
        double best_profit = calculate_no_purchase_profit(turn_num, budget, active_resources, depth);
        
        // Limit resources to consider based on depth to avoid explosion
        int max_resources = (depth > 3) ? 3 : (depth > 1) ? 5 : resources.size();
        
        // Sort resources by efficiency score
        std::vector<std::pair<double, const ResourceInfo*>> sorted_resources;
        for (const auto& r_info : resources) {
            if (r_info.RA <= budget) {
                sorted_resources.push_back({r_info.efficiency_score(), &r_info});
            }
        }
        
        std::sort(sorted_resources.begin(), sorted_resources.end(),
                 [](const auto& a, const auto& b) { return a.first > b.first; });
        
        // Evaluate top resources
        int resources_to_check = std::min(max_resources, static_cast<int>(sorted_resources.size()));
        for (int i = 0; i < resources_to_check; i++) {
            const auto& r_info = *sorted_resources[i].second;
            double resource_profit = calculate_resource_profit(turn_num, budget, active_resources, r_info, depth);
            best_profit = std::max(best_profit, resource_profit);
        }
        
        // Store in cache
        memo_cache[key] = best_profit;
        return best_profit;
    }
    
    double calculate_no_purchase_profit(int turn_num, int budget, const std::vector<Resource>& active_resources, int depth) {
        const Turn& current_turn = turns[turn_num];
        
        // Calculate maintenance cost
        int maintenance = 0;
        for (const auto& res : active_resources) {
            if (res.active) {
                maintenance += res.RP;
            }
        }
        
        // Calculate effects
        double a_effect = 0, b_effect = 0, d_effect = 0;
        for (const auto& res : active_resources) {
            if (res.active && res.active_phase) {
                if (res.RT == 'A') a_effect += res.RE / 100.0;
                if (res.RT == 'B') b_effect += res.RE / 100.0;
                if (res.RT == 'D') d_effect += res.RE / 100.0;
            }
        }
        
        // Apply effects
        int effective_tm = std::max(0, static_cast<int>(std::floor(current_turn.TM * (1 + b_effect))));
        int effective_tx = std::max(0, static_cast<int>(std::floor(current_turn.TX * (1 + b_effect))));
        int effective_tr = std::max(0, static_cast<int>(std::floor(current_turn.TR * (1 + d_effect))));
        
        // Calculate buildings powered
        int powered = 0;
        for (const auto& res : active_resources) {
            if (res.active && res.active_phase) {
                powered += static_cast<int>(std::floor(res.RU * (1 + a_effect)));
            }
        }
        
        // Handle accumulators
        std::vector<Resource> temp_active = active_resources;
        int deficit = std::max(0, effective_tm - powered);
        
        for (auto& res : temp_active) {
            if (res.RT == 'E' && res.active && res.active_phase) {
                int withdraw = std::min(deficit, res.accumulated);
                deficit -= withdraw;
                res.accumulated -= withdraw;
                if (deficit == 0) break;
            }
        }
        
        // Calculate profit
        int profit = 0;
        if (deficit <= 0) {
            int served = std::min(powered, effective_tx);
            profit = served * effective_tr;
        }
        
        int updated_budget = budget - maintenance + profit;
        
        // Store surplus in accumulators
        int surplus = std::max(0, powered - effective_tx);
        int accumulator_count = 0;
        
        for (auto& res : temp_active) {
            if (res.RT == 'E' && res.active && res.active_phase) {
                accumulator_count++;
            }
        }
        
        if (accumulator_count > 0 && surplus > 0) {
            int add_each = surplus / accumulator_count;
            for (auto& res : temp_active) {
                if (res.RT == 'E' && res.active && res.active_phase) {
                    res.accumulated += add_each;
                }
            }
        }
        
        // Advance to next turn
        std::vector<Resource> next_active;
        for (auto res : temp_active) {
            if (res.advance_turn()) {
                next_active.push_back(res);
            }
        }
        
        double future_profit = simulate(turn_num + 1, updated_budget, next_active, depth - 1);
        return profit + future_profit;
    }
    
    double calculate_resource_profit(int turn_num, int budget, const std::vector<Resource>& active_resources, 
                                    const ResourceInfo& r_info, int depth) {
        if (r_info.RA > budget) {
            return -std::numeric_limits<double>::infinity();
        }
        
        std::vector<Resource> temp_active = active_resources;
        
        // Calculate C effect on resource lifespan
        double c_effect = 0;
        for (const auto& res : temp_active) {
            if (res.RT == 'C' && res.active_phase && res.active) {
                c_effect += res.RE / 100.0;
            }
        }
        
        int new_rl = std::max(1, static_cast<int>(std::floor(r_info.RL * (1 + c_effect))));
        Resource new_r(r_info.RI, r_info.RA, r_info.RP, r_info.RW, r_info.RM, 
                       new_rl, r_info.RU, r_info.RT, r_info.RE);
        
        temp_active.push_back(new_r);
        
        // Calculate maintenance
        int maintenance = 0;
        for (const auto& res : temp_active) {
            if (res.active) {
                maintenance += res.RP;
            }
        }
        
        // Calculate effects
        double a_effect = 0, b_effect = 0, d_effect = 0;
        for (const auto& res : temp_active) {
            if (res.active && res.active_phase) {
                if (res.RT == 'A') a_effect += res.RE / 100.0;
                if (res.RT == 'B') b_effect += res.RE / 100.0;
                if (res.RT == 'D') d_effect += res.RE / 100.0;
            }
        }
        
        const Turn& current_turn = turns[turn_num];
        
        // Apply effects
        int effective_tm = std::max(0, static_cast<int>(std::floor(current_turn.TM * (1 + b_effect))));
        int effective_tx = std::max(0, static_cast<int>(std::floor(current_turn.TX * (1 + b_effect))));
        int effective_tr = std::max(0, static_cast<int>(std::floor(current_turn.TR * (1 + d_effect))));
        
        // Calculate buildings powered
        int powered = 0;
        for (const auto& res : temp_active) {
            if (res.active && res.active_phase) {
                powered += static_cast<int>(std::floor(res.RU * (1 + a_effect)));
            }
        }
        
        // Handle accumulators for deficit
        int deficit = std::max(0, effective_tm - powered);
        for (auto& res : temp_active) {
            if (res.RT == 'E' && res.active && res.active_phase) {
                int withdraw = std::min(deficit, res.accumulated);
                deficit -= withdraw;
                res.accumulated -= withdraw;
                if (deficit == 0) break;
            }
        }
        
        // Calculate profit
        int profit = 0;
        if (deficit <= 0) {
            int served = std::min(powered, effective_tx);
            profit = served * effective_tr;
        }
        
        int updated_budget = budget - r_info.RA - maintenance + profit;
        
        // Store surplus in accumulators
        int surplus = std::max(0, powered - effective_tx);
        int accumulator_count = 0;
        
        for (auto& res : temp_active) {
            if (res.RT == 'E' && res.active && res.active_phase) {
                accumulator_count++;
            }
        }
        
        if (accumulator_count > 0 && surplus > 0) {
            int add_each = surplus / accumulator_count;
            for (auto& res : temp_active) {
                if (res.RT == 'E' && res.active && res.active_phase) {
                    res.accumulated += add_each;
                }
            }
        }
        
        // Advance to next turn
        std::vector<Resource> next_active;
        for (auto res : temp_active) {
            if (res.advance_turn()) {
                next_active.push_back(res);
            }
        }
        
        double future_profit = simulate(turn_num + 1, updated_budget, next_active, depth - 1);
        return profit + future_profit;
    }
    
    void clear_cache() {
        memo_cache.clear();
    }
};

// Evaluation result structure
struct EvaluationResult {
    double net_value;
    const ResourceInfo* resource;
    
    EvaluationResult() : net_value(-std::numeric_limits<double>::infinity()), resource(nullptr) {}
    
    EvaluationResult(double net, const ResourceInfo* res) : net_value(net), resource(res) {}
};

// Determine optimal simulation depth based on remaining turns
int calculate_simulation_depth(int turn_num, int total_turns) {
    int turns_remaining = total_turns - turn_num - 1;
    
    if (turns_remaining <= 1) {
        return 1; // Very end game
    } else if (turns_remaining <= 3) {
        return 2; // End game
    } else if (turns_remaining <= 6) {
        return 3; // Mid-late game
    } else if (turns_remaining <= 15) {
        return 4; // Mid game
    } else {
        return 5; // Early game
    }
}

// Get optimal thread count with safety cap
int get_optimal_thread_count() {
    int hardware_threads = std::thread::hardware_concurrency();
    // Cap at 16 threads to avoid over-parallelization
    return std::min(hardware_threads > 0 ? hardware_threads : 4, 16);
}

// Batch resources for thread assignments
std::vector<std::vector<const ResourceInfo*>> batch_resources(
    const std::vector<ResourceInfo>& resources, 
    int budget, 
    int num_threads) {
    
    // Only include resources we can afford
    std::vector<const ResourceInfo*> affordable;
    for (const auto& r : resources) {
        if (r.RA <= budget) {
            affordable.push_back(&r);
        }
    }
    
    // Sort by efficiency score
    std::sort(affordable.begin(), affordable.end(), 
              [](const ResourceInfo* a, const ResourceInfo* b) {
                  return a->efficiency_score() > b->efficiency_score();
              });
    
    // Create balanced batches for threads
    std::vector<std::vector<const ResourceInfo*>> batches(num_threads);
    for (size_t i = 0; i < affordable.size(); i++) {
        batches[i % num_threads].push_back(affordable[i]);
    }
    
    return batches;
}

int main() {
    int D, R, T;
    std::cin >> D >> R >> T;

    std::vector<ResourceInfo> resources;
    resources.reserve(R);
    
    for (int i = 0; i < R; i++) {
        ResourceInfo info;
        std::cin >> info.RI >> info.RA >> info.RP >> info.RW >> info.RM >> info.RL >> info.RU;
        
        char rt;
        std::cin >> rt;
        info.RT = rt;
        
        if (rt != 'X') {
            std::cin >> info.RE;
        } else {
            info.RE = 0;
        }
        
        resources.push_back(info);
    }

    std::vector<Turn> turns;
    turns.reserve(T);
    
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
    
    // Create game simulator
    GameSimulator simulator(resources, turns);

    for (int turn_num = 0; turn_num < T; turn_num++) {
        // Calculate adaptive simulation depth
        int sim_depth = calculate_simulation_depth(turn_num, T);
        std::cerr << "Turn " << turn_num << " - Using simulation depth: " << sim_depth << std::endl;
        
        // Clear cache at the start of each turn to free memory
        simulator.clear_cache();
        
        // Batch resources for threads
        auto resource_batches = batch_resources(resources, budget, num_threads);
        
        // Launch threads to evaluate resources in parallel
        std::vector<std::future<EvaluationResult>> futures;
        for (int thread_id = 0; thread_id < num_threads; ++thread_id) {
            if (resource_batches[thread_id].empty()) continue;
            
            futures.push_back(std::async(std::launch::async, [&, thread_id, sim_depth]() {
                EvaluationResult best_result;
                
                for (const auto* r_info : resource_batches[thread_id]) {
                    // Skip resources we can't afford
                    if (r_info->RA > budget) continue;
                    
                    // Create temporary active resources with the new resource
                    std::vector<Resource> temp_active = active_resources;
                    
                    // Apply C effect on resource lifespan
                    double c_effect = 0;
                    for (const auto& res : temp_active) {
                        if (res.RT == 'C' && res.active_phase && res.active) {
                            c_effect += res.RE / 100.0;
                        }
                    }
                    
                    int new_rl = std::max(1, static_cast<int>(std::floor(r_info->RL * (1 + c_effect))));
                    Resource new_r(r_info->RI, r_info->RA, r_info->RP, r_info->RW, r_info->RM, 
                                  new_rl, r_info->RU, r_info->RT, r_info->RE);
                    
                    temp_active.push_back(new_r);
                    
                    // Simulate future with this resource
                    double profit = simulator.calculate_resource_profit(
                        turn_num, budget, active_resources, *r_info, sim_depth);
                    
                    if (profit > best_result.net_value) {
                        best_result.net_value = profit;
                        best_result.resource = r_info;
                    }
                }
                
                return best_result;
            }));
        }
        
        // Evaluate the option of not buying anything
        futures.push_back(std::async(std::launch::async, [&, sim_depth]() {
            double profit = simulator.calculate_no_purchase_profit(
                turn_num, budget, active_resources, sim_depth);
            
            return EvaluationResult(profit, nullptr);
        }));
        
        // Collect results from all threads
        EvaluationResult best_overall;
        for (auto& future : futures) {
            EvaluationResult result = future.get();
            if (result.net_value > best_overall.net_value) {
                best_overall = result;
            }
        }
        
        // Process the best result
        const ResourceInfo* best_r = best_overall.resource;
        
        if (best_r) {
            // Apply C effect to the purchased resource
            double c_effect = 0;
            for (const auto& res : active_resources) {
                if (res.RT == 'C' && res.active_phase && res.active) {
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
        
        // Process turn effects and update budget
        
        // Pay maintenance costs
        int maintenance = 0;
        for (const auto& res : active_resources) {
            if (res.active) {
                maintenance += res.RP;
            }
        }
        budget -= maintenance;
        
        // Calculate special effects
        double a_effect = 0, b_effect = 0, d_effect = 0;
        for (const auto& res : active_resources) {
            if (res.active && res.active_phase) {
                if (res.RT == 'A') a_effect += res.RE / 100.0;
                if (res.RT == 'B') b_effect += res.RE / 100.0;
                if (res.RT == 'D') d_effect += res.RE / 100.0;
            }
        }
        
        // Apply effects to turn parameters
        const Turn& current_turn = turns[turn_num];
        int effective_tm = std::max(0, static_cast<int>(std::floor(current_turn.TM * (1 + b_effect))));
        int effective_tx = std::max(0, static_cast<int>(std::floor(current_turn.TX * (1 + b_effect))));
        int effective_tr = std::max(0, static_cast<int>(std::floor(current_turn.TR * (1 + d_effect))));
        
        // Calculate buildings powered
        int powered = 0;
        for (const auto& res : active_resources) {
            if (res.active && res.active_phase) {
                powered += static_cast<int>(std::floor(res.RU * (1 + a_effect)));
            }
        }
        
        // Handle accumulators for deficit
        int deficit = std::max(0, effective_tm - powered);
        for (auto& res : active_resources) {
            if (res.RT == 'E' && res.active && res.active_phase) {
                if (deficit <= 0) break;
                int withdraw = std::min(deficit, res.accumulated);
                res.accumulated -= withdraw;
                deficit -= withdraw;
            }
        }
        
        // Calculate profit
        int profit = 0;
        if (deficit <= 0) {
            int served = std::min(powered, effective_tx);
            profit = served * effective_tr;
        }
        
        budget += profit;
        
        // Store surplus in accumulators
        int surplus = std::max(0, powered - effective_tx);
        std::vector<Resource*> e_accs;
        for (auto& res : active_resources) {
            if (res.RT == 'E' && res.active && res.active_phase) {
                e_accs.push_back(&res);
            }
        }
        
        if (!e_accs.empty() && surplus > 0) {
            int add_each = surplus / e_accs.size();
            for (auto* acc : e_accs) {
                acc->accumulated += add_each;
            }
        }
        
        // Advance to next turn
        std::vector<Resource> new_active;
        new_active.reserve(active_resources.size());
        for (auto& res : active_resources) {
            if (res.advance_turn()) {
                new_active.push_back(res);
            }
        }
        active_resources = std::move(new_active);
        
        // Update progress
        logger.update(turn_num + 1);
    }
    
    std::cerr << "Calculation complete. Writing solution..." << std::endl;
    
    // Output the solution
    for (const auto& line : output) {
        std::cout << line << std::endl;
    }
    
    std::cerr << "Solution output complete." << std::endl;
    
    return 0;
}
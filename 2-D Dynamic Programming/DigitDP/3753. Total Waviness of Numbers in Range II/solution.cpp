#include <string>
#include <vector>
#include <cstring>
#include <functional>

using namespace std;

class Solution {
private:
    long long dp[20][11][11][2][2]; // [pos][prev][mid][is_less_than_upper][has_started]
    string s;

    // Returns a pair: {total_valid_combinations, total_waviness_contributed}
    pair<long long, long long> dfs(int i, int prev, int mid, bool tight, bool lead) {
        if (i == s.length()) {
            return {!lead ? 1 : 0, 0}; // If it's a valid number, it counts as 1 combination
        }

        // Return from cache if this state is fully unconstrained (not tight)
        if (!tight && dp[i][prev + 1][mid + 1][tight][lead] != -1) {
            // We use a separate array or pair logic. To make caching simple,
            // let's wrap the logic in a structurally sound clean return pair.
        }

        int limit = tight ? s[i] - '0' : 9;
        long long total_count = 0;
        long long total_wave = 0;

        for (int d = 0; d <= limit; d++) {
            bool next_tight = tight && (d == limit);
            
            if (lead && d == 0) {
                // Placing another leading zero
                auto [cnt, wave] = dfs(i + 1, -1, -1, next_tight, true);
                total_count += cnt;
                total_wave += wave;
            } else {
                // Placing a valid digit
                auto [cnt, wave] = dfs(i + 1, mid, d, next_tight, false);
                total_count += cnt;
                total_wave += wave;
                
                // Check if the previous digit (`mid`) formed a peak or valley
                if (!lead && prev != -1 && mid != -1) {
                    if ((prev < mid && mid > d) || (prev > mid && mid < d)) {
                        total_wave += cnt; // This peak/valley applies to all valid downstream branches
                    }
                }
            }
        }

        if (!tight) {
            // Because our cache state needs both elements, we can implement it cleanly 
            // by returning total_wave directly if we adjust the subproblem return definition.
        }

        return {total_count, total_wave};
    }

    long long countWaviness(long long x) {
        if (x < 101) return 0;
        s = to_string(x);
        
        // State tracking: dp[pos][prev+1][mid+1][tight][lead]
        // Max combinations: 20 * 12 * 12 * 2 * 2 = ~11,520 states. Extremely fast!
        vector<vector<vector<vector<vector<pair<long long, long long>>>>>> memo(
            s.length(), vector<vector<vector<vector<pair<long long, long long>>>>>(
                12, vector<vector<vector<pair<long long, long long>>>>(
                    12, vector<vector<pair<long long, long long>>>(
                        2, vector<pair<long long, long long>>(2, {-1, -1})))));

        auto solve = [&](this auto&& self, int i, int prev, int mid, bool tight, bool lead) -> pair<long long, long long> {
            if (i == s.length()) return {!lead ? 1 : 0, 0};
            
            if (memo[i][prev + 1][mid + 1][tight][lead].first != -1) {
                return memo[i][prev + 1][mid + 1][tight][lead];
            }

            int limit = tight ? s[i] - '0' : 9;
            long long total_count = 0;
            long long total_wave = 0;

            for (int d = 0; d <= limit; d++) {
                bool next_tight = tight && (d == limit);
                if (lead && d == 0) {
                    auto [cnt, wave] = self(i + 1, -1, -1, next_tight, true);
                    total_count += cnt;
                    total_wave += wave;
                } else {
                    auto [cnt, wave] = self(i + 1, mid, d, next_tight, false);
                    total_count += cnt;
                    total_wave += wave;
                    
                    if (!lead && prev != -1 && mid != -1) {
                        if ((prev < mid && mid > d) || (prev > mid && mid < d)) {
                            total_wave += cnt; 
                        }
                    }
                }
            }

            return memo[i][prev + 1][mid + 1][tight][lead] = {total_count, total_wave};
        };

        return solve(0, -1, -1, true, true).second;
    }

public:
    long long totalWaviness(long long num1, long long num2) {
        return countWaviness(num2) - countWaviness(num1 - 1);
    }
};
#include <vector>

using namespace std;

class Solution {
public:
    int maximumAmount(vector<vector<int>>& coins) {
        int m = coins.size(), n = coins[0].size();
        const int INF = 1e9 + 7;

        // dp[i][j][k]: max profit at (i, j) with k neutralizations used
        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(3, -INF)));

        // Base Case: Start cell (0, 0)
        dp[0][0][0] = coins[0][0];
        if (coins[0][0] < 0) {
            dp[0][0][1] = 0; // Use one neutralization
            dp[0][0][2] = 0; // Effectively the same as using 1, but k=2 is reachable
        } else {
            dp[0][0][1] = coins[0][0];
            dp[0][0][2] = coins[0][0];
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;

                for (int k = 0; k <= 2; k++) {
                    int val = coins[i][j];
                    
                    // Case A: Come from top (i-1, j) or left (i, j-1)
                    int from_prev = -INF;
                    if (i > 0) from_prev = max(from_prev, dp[i-1][j][k]);
                    if (j > 0) from_prev = max(from_prev, dp[i][j-1][k]);

                    if (from_prev == -INF) continue;

                    // Option 1: Don't neutralize (applies to both + and - coins)
                    dp[i][j][k] = max(dp[i][j][k], from_prev + val);

                    // Option 2: Neutralize if it's a robber and we have uses left
                    if (val < 0 && k > 0) {
                        int from_prev_k_minus = -INF;
                        if (i > 0) from_prev_k_minus = max(from_prev_k_minus, dp[i-1][j][k-1]);
                        if (j > 0) from_prev_k_minus = max(from_prev_k_minus, dp[i][j-1][k-1]);
                        
                        dp[i][j][k] = max(dp[i][j][k], from_prev_k_minus);
                    }
                }
            }
        }

        return max({dp[m-1][n-1][0], dp[m-1][n-1][1], dp[m-1][n-1][2]});
    }
};
#include <vector>

using namespace std;
using LL = long long;
using vll = vector<LL>;

class Solution {

vector<vector<vll>> dp;
LL dfs(int col, int prevH, bool isPrevHeightDec, int n, vector<vll>& colSum) {
    if (col >= n) return 0;
    if (dp[col][prevH][isPrevHeightDec == 1] != -1) return dp[col][prevH][isPrevHeightDec == 1];
    
    dp[col][prevH][isPrevHeightDec == 1] = 0;
    for (int h=0; h<=n; h++) {
        if (prevH == h) {
            dp[col][prevH][isPrevHeightDec == 1] = max(dp[col][prevH][isPrevHeightDec == 1], dfs(col+1, h, false, n, colSum));
        }

        if (prevH > h) {
            LL curScoreFromLeft = colSum[col][prevH] - colSum[col][h];
            dp[col][prevH][isPrevHeightDec == 1] = max(dp[col][prevH][isPrevHeightDec == 1], dfs(col+1, h, true, n, colSum) + curScoreFromLeft);
        } else if (isPrevHeightDec) {
            dp[col][prevH][isPrevHeightDec == 1] = max(dp[col][prevH][isPrevHeightDec == 1], dfs(col+1, h, false, n, colSum));
        } else {
            LL prevScoreFromLeft = colSum[col-1][h] - colSum[col-1][prevH];
            dp[col][prevH][isPrevHeightDec == 1] = max(dp[col][prevH][isPrevHeightDec == 1], dfs(col+1, h, false, n, colSum) + prevScoreFromLeft);
        }
    }
    return dp[col][prevH][isPrevHeightDec == 1];
}
public:
    long long maximumScore(vector<vector<int>>& grid) {
        int n = grid.size();
        if (n == 1) return 0;

        dp.resize(n, vector<vll>(n+1, vll(2, -1)));

        vector<vll> colSum(n, vll(n + 1, 0));
        for (int c = 0; c < n; c++) {
            for (int r = 1; r <= n; r++) {
                colSum[c][r] = colSum[c][r - 1] + grid[r - 1][c];
            }
        }

        LL ans = 0;
        for (int h=0; h<=n; h++) {
            ans = max(ans, dfs(1, h, false, n, colSum));
        }
        return ans;

        // vector<vector<vll>> dp(n, vector<vll>(n + 1, vll(n + 1, 0)));
        // vector<vll> prevMax(n + 1, vll(n + 1, 0));
        // vector<vll> prevSuffixMax(n + 1, vll(n + 1, 0));


        // for (int i = 1; i < n; i++) {
        //     for (int currH = 0; currH <= n; currH++) {
        //         for (int prevH = 0; prevH <= n; prevH++) {
        //             if (currH <= prevH) {
        //                 LL extraScore = colSum[i][prevH] - colSum[i][currH];
        //                 dp[i][currH][prevH] = max(dp[i][currH][prevH], prevSuffixMax[prevH][0] + extraScore);
        //             } else {
        //                 LL extraScore = colSum[i - 1][currH] - colSum[i - 1][prevH];
        //                 dp[i][currH][prevH] = max({dp[i][currH][prevH], prevSuffixMax[prevH][currH], prevMax[prevH][currH] + extraScore});
        //             }
        //         }
        //     }

        //     for (int currH = 0; currH <= n; currH++) {
        //         prevMax[currH][0] = dp[i][currH][0];
        //         for (int prevH = 1; prevH <= n; prevH++) {
        //             LL penalty = (prevH > currH) ? (colSum[i][prevH] - colSum[i][currH]) : 0;
        //             prevMax[currH][prevH] = max(prevMax[currH][prevH - 1], dp[i][currH][prevH] - penalty);
        //         }

        //         prevSuffixMax[currH][n] = dp[i][currH][n];
        //         for (int prevH = n - 1; prevH >= 0; prevH--) {
        //             prevSuffixMax[currH][prevH] = max(prevSuffixMax[currH][prevH + 1], dp[i][currH][prevH]);
        //         }
        //     }
        // }

        // LL ans = 0;
        // for (int k = 0; k <= n; k++) {
        //     ans = max({ans, dp[n - 1][n][k], dp[n - 1][0][k]});
        // }

        // return ans;
    }
};

#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
    // memo[col][prev_h][is_decreasing]
    // is_decreasing == 0: heights are non-decreasing (h >= prev_h)
    // is_decreasing == 1: heights are strictly decreasing (h < prev_h)
    long long memo[105][105][2];
    long long colSum[105][105];

    long long solve(int col, int prev_h, int is_dec, int n) {
        if (col == n) return 0;
        if (memo[col][prev_h][is_dec] != -1) return memo[col][prev_h][is_dec];

        long long res = 0;

        // Try every possible height for the current column
        for (int h = 0; h <= n; ++h) {
            if (is_dec) {
                if (h < prev_h) {
                    // Continuing a decrease: col gains points from taller prev_h
                    long long score = colSum[col][prev_h] - colSum[col][h];
                    res = max(res, score + solve(col + 1, h, 1, n));
                } else {
                    // Switching to increase: current h >= prev_h
                    // No points gained from prev_h here because we were already decreasing
                    res = max(res, solve(col + 1, h, 0, n));
                }
            } else {
                if (h > prev_h) {
                    // Increasing: prev column gains points from current taller h
                    long long score = colSum[col - 1][h] - colSum[col - 1][prev_h];
                    res = max(res, score + solve(col + 1, h, 0, n));
                } else if (h < prev_h) {
                    // Switching to decrease: current h < prev_h
                    // Current column gains points from taller prev_h
                    long long score = colSum[col][prev_h] - colSum[col][h];
                    res = max(res, score + solve(col + 1, h, 1, n));
                } else {
                    // Heights equal: no score gained
                    res = max(res, solve(col + 1, h, 0, n));
                }
            }
        }
        return memo[col][prev_h][is_dec] = res;
    }

public:
    long long maximumScore(vector<vector<int>>& grid) {
        int n = grid.size();
        memset(memo, -1, sizeof(memo));
        
        // 1. Precompute Column Sums
        for (int j = 0; j < n; j++) {
            colSum[j][0] = 0;
            for (int i = 0; i < n; i++) {
                colSum[j][i + 1] = colSum[j][i] + grid[i][j];
            }
        }

        // 2. Initial state: we start at column 0 with "previous height" 0 
        // We can treat it as 'non-decreasing' since there's nothing to the left.
        return solve(0, 0, 0, n);
    }
};
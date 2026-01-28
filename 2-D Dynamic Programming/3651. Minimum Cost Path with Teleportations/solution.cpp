#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <queue>

using namespace std;


class Solution {
public:
    int minCost(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();

        vector<vector<vector<int>>> dp(m+1, vector<vector<int>>(n+1, vector<int>(k+1, INT_MAX)));
        for (int r=0; r<m; r++) {
            for (int c=0; c<n; c++) {
                if (r==0 && c==0) {
                    dp[r][c][0] = 0;
                } else {
                    if (r > 0) {
                        dp[r][c][0] = min(dp[r][c][0], dp[r-1][c][0]);
                    }
                    if (c > 0) {
                        dp[r][c][0] = min(dp[r][c][0], dp[r][c-1][0]);
                    }
                    dp[r][c][0] += grid[r][c];
                }
            }
        }

        for (int kk=1; kk<=k; kk++) {
            vector<vector<int>> arr;
            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    arr.push_back({grid[i][j], dp[i][j][kk-1], i, j});
                }
            }
            sort(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
                if (a[0] != b[0]) return a[0] > b[0]; // Grid descending
                return a[1] < b[1]; // DP ascending
            });

            int mini = INT_MAX;
            for (const auto& item : arr) {
                int cost = item[1];
                int r = item[2], c = item[3];
                mini = min(mini, cost);
                dp[r][c][kk] = mini;
            }

            for (int r=0; r<m; r++) {
                for (int c=0; c<n; c++) {
                    if (r == 0 && c == 0) {
                        dp[r][c][kk] = 0;
                    } else {
                        if (r > 0) {
                            dp[r][c][kk] = min(dp[r][c][kk], dp[r-1][c][kk] + grid[r][c]);
                        }
                        if (c > 0) {
                            dp[r][c][kk] = min(dp[r][c][kk], dp[r][c-1][kk] + grid[r][c]);
                        }
                    }
                }
            }
        }
        return dp[m-1][n-1][k];
    }
};
#include <vector>

using namespace std;

using LL = long long;

class Solution {
public:
    int numberOfPaths(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();

        LL mod = 1000000007;

        vector<vector<vector<LL>>> dp(m, vector<vector<LL>>(n, vector<LL>(k, 0)));
        dp[0][0][grid[0][0]%k] = 1;

        for (int r=0; r<m; r++) {
            for (int c=0; c<n; c++) {
                if (r==0 && c==0) continue;

                for (int kk=0; kk<k; kk++) {
                    int sum = (kk + grid[r][c])%k;
                    if (c-1 >= 0) {
                        dp[r][c][sum] += dp[r][c-1][kk];
                    }
                    if (r-1 >= 0) {
                        dp[r][c][sum] += dp[r-1][c][kk];
                    }
                    dp[r][c][sum] %= mod;
                }
            }
        }
        return dp[m-1][n-1][0];
    }
};



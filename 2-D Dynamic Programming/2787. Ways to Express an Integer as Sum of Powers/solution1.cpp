// dp[i][j]: the number of ways of i such that j is the maximum factor.
// i = a1^x + a2^x + ...+ j^x where a1 < a2 < ... < j

using LL = long long;

class Solution {
public:
int numberOfWays(int n, int x) {
        int mod = 1e9+7;
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        dp[0][0] = 1;

        for (int i=0; i<=n; i++) {
            for (int j=1; j<=n; j++) {
                LL p = pow(j, x);
                
                dp[i][j] = dp[i][j-1] + (i-p >= 0 ? dp[i-p][j-1] : 0); // skip j^x + pick j^x
                dp[i][j] %= mod;
            }
        }

        return dp[n][n];
    }
};

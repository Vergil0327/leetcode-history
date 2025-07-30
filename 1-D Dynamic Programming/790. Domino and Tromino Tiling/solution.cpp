// https://www.youtube.com/watch?v=S-fUTfqrdq8&ab_channel=HuaHua
using LL = long long;

class Solution {
public:
    int mod = 1e9 + 7;
    int numTilings(int n) {
        vector<vector<LL>> dp(n+1, vector<LL>(2, 0));
        dp[0][0] = dp[1][0] = 1;
        for (int i=2; i<= n; i++) {
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + 2 * dp[i-1][1]) % mod;
            dp[i][1] = (dp[i-2][0] + dp[i-1][1]) % mod;
        }
        return dp[n][0];
    }
};

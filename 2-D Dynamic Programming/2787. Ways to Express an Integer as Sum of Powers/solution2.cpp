using LL = long long;

class Solution {
public:
int numberOfWays(int n, int x) {
        int mod = 1e9+7;
        vector<int> dp(n+1, 0);
        dp[0] = 1;

        for (int i=1; i<=n; i++) {
            LL num = pow(i, x);

            // 從後往前更新: dp_new[sum] += dp_old[sum-num]
            for (int sum=n; sum>=num; sum--) {
                dp[sum] += dp[sum-num];
                dp[sum] %= mod;
            }
        }
        return dp[n];
    }
};

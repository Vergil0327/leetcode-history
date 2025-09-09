class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        int mod = 1e9 + 7;
        vector<long long> dp(n + 1, 0);
        dp[1] = 1;  // 1 person knows on day 1
        
        for (int day = 2; day <= n; day++) {
            // People who learned the secret 'delay' to 'forget-1' days ago
            // can share it today
            for (int learned_day = max(1, day - forget + 1); 
                 learned_day <= min(day - delay, n); 
                 learned_day++) {
                dp[day] = (dp[day] + dp[learned_day]) % mod;
            }
        }
        
        // Count people who still remember on day n
        long long res = 0;
        for (int learned_day = max(1, n - forget + 1); learned_day <= n; learned_day++) {
            res = (res + dp[learned_day]) % mod;
        }
        
        return res;
    }
};
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        int n = nums.size();
        for (int i=0; i<n; i++) {
            nums[i] %= k;
        }

        vector<vector<int>> dp(k, vector<int>(k, 0));
        int res = 1;
        for (auto& num: nums) {
            for (int m=0; m<k; m++) {
                int prev = ((m-num)+k)%k;
                dp[num][m] = max(dp[num][m], dp[prev][m]+1);
                res = max(res, dp[num][m]);
            }
        }
        return res;
    }
};
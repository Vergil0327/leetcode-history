class Solution {
public:
    long long maximumProduct(vector<int>& nums, int m) {
        long long mx = nums[0], mn = nums[0];

        long long res = LLONG_MIN;
        for (int j=m-1; j<nums.size(); j++) {
            res = max(res, nums[j] * mx);
            res = max(res, nums[j] * mn);

            int i = j - (m-1) + 1;
            if (i < nums.size()) {
                mx = max(mx, (long long)nums[i]);
                mn = min(mn, (long long)nums[i]);
            }
        }
        return res;
    }
};
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int n = nums.size();

        unordered_map<int,int> count;
        unordered_map<int,int> diff;
        for (auto& num : nums) {
            diff[num-k]++;
            diff[num+k+1]--;
            
            count[num]++;
        }
        
        
        int mn = *min_element(nums.begin(), nums.end()), mx = *max_element(nums.begin(), nums.end());
        for (int i=mn-k; i<mx+k+1; i++) {
            diff[i] += diff[i-1];
        }

        int res = 0;
        for (int num=mn; num<=mx; num++) {
            int op = diff[num] - count[num];
            res = max(res, count[num] + min(numOperations, op));
        }        

        return res;
    }
};
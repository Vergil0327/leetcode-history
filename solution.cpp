class Solution {
public:
    int maxFrequency(vector<int>& nums, int k, int numOperations) {
        int n = nums.size();

        unordered_map<int,int> count;
        unordered_map<int,int> diff;
        unordered_set<int> s;
        for (auto& num: nums) {
            s.insert(num-k);
            s.insert(num);
            s.insert(num+k+1);
            count[num]++;
            diff[num-k]++;
            diff[num+k+1]--;
        }

        vector<int> positions;
        for (auto& pos : s) {
            positions.push_back(pos);
        }
        sort(positions.begin(), positions.end());
        
        int res = 0, freq = 0;
        for (auto& i: positions) {
            freq += diff[i];
            res = max(res, count[i] + min(numOperations, freq - count[i]));
        }

        return res;
    }
};

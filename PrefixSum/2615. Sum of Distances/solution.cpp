#include <vector>
#include <unordered_map>
using namespace std;

using LL = long long;

class Solution {
public:
    vector<long long> distance(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, vector<LL>> indices;

        for (int i = 0; i < n; i++) {
            indices[nums[i]].push_back(i);
        }

        vector<LL> res(n, 0);
        
        for (auto& [val, idxs] : indices) {
            int m = idxs.size();
            if (m == 1) continue;
            
            // Create prefix sum using partial_sum
            vector<LL> presum(m);
            partial_sum(idxs.begin(), idxs.end(), presum.begin());
            
            for (int i = 0; i < m; i++) {
                LL idx = idxs[i];
                
                // Left: sum of distances to indices before i
                LL leftSum = i * idx - (i > 0 ? presum[i - 1] : 0);
                
                // Right: sum of distances to indices after i
                LL rightSum = (presum[m - 1] - presum[i]) - (m - 1 - i) * idx;
                
                res[idx] = leftSum + rightSum;
            }
        }

        return res;
    }
};
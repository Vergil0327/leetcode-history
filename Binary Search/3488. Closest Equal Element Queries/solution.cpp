#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        unordered_map<int, vector<int>> valToIndex;
        
        // Step 1: Group indices by their values
        for (int i = 0; i < n; i++) {
            valToIndex[nums[i]].push_back(i);
        }

        vector<int> res;
        for (auto& targetIdx : queries) {
            const vector<int>& indices = valToIndex[nums[targetIdx]];

            // If only one such element exists, there's no "other" index j
            if (indices.size() <= 1) {
                res.push_back(-1);
                continue;
            }

            // Step 2: Use binary search to find the position of targetIdx in the index list
            auto it = lower_bound(indices.begin(), indices.end(), targetIdx);
            int pos = distance(indices.begin(), it);
            int m = indices.size();

            // Step 3: Check neighbors (with circular wrapping)
            // The closest element must be the one immediately before or after in the sorted list
            int prevIdx = indices[(pos - 1 + m) % m];
            int nextIdx = indices[(pos + 1) % m];

            // Step 4: Calculate circular distances
            auto getDist = [&](int i, int j) {
                int d = abs(i - j);
                return min(d, n - d);
            };

            res.push_back(min(getDist(targetIdx, prevIdx), getDist(targetIdx, nextIdx)));
        }

        return res;
    }
};
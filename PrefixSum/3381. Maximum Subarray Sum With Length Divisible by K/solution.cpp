#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    long long maxSubarraySum(vector<int>& nums, int k) {
        unordered_map<int,long long> m = {{0,0}};
        long long res = LLONG_MIN, presum = 0;
        for (int i=0; i<nums.size(); i++) {
            presum += nums[i];
            int key = (i+1)%k;

            if (m.find(key) != m.end()) {
                res = max(res, presum - m[key]);
            }

            if (m.find(key) == m.end()) {
                m[key] = presum;
            } else {
                m[key] = min(m[key], presum);
            }
        }
        return res;
    }
};
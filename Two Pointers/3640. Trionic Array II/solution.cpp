#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

using LL = long long;

class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();

        vector<vector<LL>> dec_interval;

        int i = 0;
        while (i < n) {
            LL total = nums[i];
            int j = i;
            while (j+1 < n && nums[j] > nums[j+1]) {
                j++;
                total += nums[j];
            }

            // make sure we have valid decreasing interval
            if (i < j) {
                // make sure we have two extendable sides
                if (i > 0 && j < n-1) {
                    dec_interval.push_back({i, j, total});
                }
                i = j;
            } else {
                i++;
            }
        }

        LL res = LLONG_MIN;

        for (const auto& interval : dec_interval) {
            int l = interval[0], r = interval[1];
            LL sum = interval[2];

            if (nums[l-1] < nums[l] && nums[r+1] > nums[r]) {
                l--;
                r++;
                sum += nums[l] + nums[r];
            }

            // extend to the left
            LL sum_left = sum;
            while (l-1 >= 0 && nums[l-1] < nums[l]) {
                l--;
                sum_left += nums[l];
                sum = max(sum, sum_left); // since `-10^9 <= nums[i] <= 10^9`, take max in every possible answer
            }

            // extend to the right
            LL sum_right = sum;
            while (r+1<n && nums[r+1] > nums[r]) {
                r++;
                sum_right += nums[r];
                sum = max(sum, sum_right); // since `-10^9 <= nums[i] <= 10^9`, take max in every possible answer
            }

            res = max(res, sum);
        }

        return res;
    }
};
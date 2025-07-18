// # Three Pass
// minimumDifference: sum_first要盡可能小, sum_second要盡可能大, 這樣sum_first-sum_second會是最小
// 1. 首先從左往右找出前i個數裡, 最小的sum_first
// 2. 再來從右往左找出後面i個數裡, 最大的sum_second
// 3. 遍歷每個位置i, 找出左右兩邊的sum_first跟sum_second相減, 找出全局最小

class Solution {
public:
    long long minimumDifference(vector<int>& nums) {
        int n = nums.size() / 3;

        long long sum = 0;
        priority_queue<int> max_heap;
        for (int i=0; i<n; i++) {
            sum += nums[i];
            max_heap.push(nums[i]);
        }
        vector<long long> min_from_left(n+1, 0);
        min_from_left[0] = sum;
        for (int i=n; i<2*n; i++) {
            max_heap.push(nums[i]);
            sum += nums[i];
            sum -= max_heap.top();
            max_heap.pop();

            min_from_left[i-n+1] = sum;
        }

        reverse(nums.begin(), nums.end());
        sum = 0;
        priority_queue<int, vector<int>, greater<int>> min_heap;
        for (int i=0; i<n; i++) {
            sum += nums[i];
            min_heap.push(nums[i]);
        }
        vector<long long> max_from_right;
        max_from_right.push_back(sum);

        for (int i=n; i<2*n; i++) {
            min_heap.push(nums[i]);
            sum += nums[i];
            sum -= min_heap.top();
            min_heap.pop();

            max_from_right.push_back(sum);
        }
        reverse(max_from_right.begin(), max_from_right.end());

        long long res = LLONG_MAX;
        for (int i=0; i<n+1; i++) {
            res = min(res, min_from_left[i] - max_from_right[i]);
        }
        return res;
    }
};

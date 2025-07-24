class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int n = nums.size();
        nums.insert(nums.begin(), -INT_MAX);
        nums.push_back(-INT_MAX);
        int l = 1, r = n;

        while (l <= r) {
            int mid = l + (r-l)/2;

            if (nums[mid] < nums[mid+1]) {
                l = mid+1;
            } else if (nums[mid-1] > nums[mid]) {
                r = mid-1;
            } else {
                return mid-1; // back to 0-indexed
            }
        }
        return 0;
    }
};
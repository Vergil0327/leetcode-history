// Recursion Approach
class Solution {
public:
    int findPivot(int low, int high, vector<int>& nums) {
        int mid = (low+high)/2;

        // Sort the three elements (low, mid, high) to find the median
        // and place them in their sorted positions within the array.
        // This also helps in setting up the partitioning.
        if (nums[low] > nums[mid]) {
            nums[low], nums[mid] = nums[mid], nums[low];
            swap(nums[low], nums[mid]);
        }
        if (nums[low] > nums[high]) {
            swap(nums[low], nums[high]);
        }
        if (nums[mid] > nums[high]) {
            swap(nums[mid], nums[high]);
        }

        // After sorting, nums[mid] is the median. Swap it to the high position
        // to be used as the pivot for partitioning.
        swap(nums[mid], nums[high]);
        return nums[high];
    }
    int partition(vector<int>& nums, int l, int r) {
        int pivot = findPivot(l, r, nums);
        int p = l;
        for (int i=l; i<r; i++) {
            if (nums[i] < pivot) {
                swap(nums[i], nums[p]);
                p++;
            }
        }

        swap(nums[p], nums[r]);
        return p; // pivot is at jth index
    }
    int quickSelect(int l, int r, int t, vector<int>& nums) {
        int p = partition(nums, l, r);

        if (p == t) {
            return nums[p];
        } else if (p > t) {
            return quickSelect(l, p-1, t, nums);
        } else {
            return quickSelect(p+1, r, t, nums);
        }
    }
    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        int index = n-k; // k-th largest
        return quickSelect(0, n-1, index, nums);
    }
};

// Iterative Approach
class Solution {
public:
    int partition(vector<int>& nums, int l, int r) {
        int pivot = nums[r];
        int p = l;
        for (int i=l; i<r; i++) {
            if (nums[i] < pivot) {
                swap(nums[i], nums[p]);
                p++;
            }
        }

        swap(nums[p], nums[r]);
        return p; // pivot is at jth index
    }

    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();

        int l = 0;
        int r = n - 1;
        int pivot_idx = 0;
        while (l < r) {
            pivot_idx = partition(nums, l, r);

            // Base case optimization: use insertion sort for small subarrays
            // For small subarrays (< 10 elements), sorting is often faster than partitioning
            if (r - l < 10) {
                sort(nums.begin() + l, nums.begin() + r + 1);
                return nums[n-k];
            }

            if (pivot_idx == n-k) {
                break;
            } else if (pivot_idx > (n-k)) {
                r = pivot_idx - 1;
            } else {
                l = pivot_idx + 1;
            }
        }

        return nums[pivot_idx];
    }
};

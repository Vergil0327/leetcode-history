# Monotonic Stack

monotonical decreasing stack
once stack is not empty, we must know current num < stack's top,
and we just compare current num with min value until current

we can also precompute minimum value until `i` index where i from 0 to n-1

ex. stack = [XXXXXXX j k XXXX] nums[j] > nums[k] since it's monotonically decreasing
and we just maintain `min` in the left portion until `j`

# Complexity

- time complexity

$$O(n)$$

- space complexity

$$O(n)$$
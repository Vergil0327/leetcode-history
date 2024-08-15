# Intuition

minimum k sum = sum of first k smallest positive missing number

therefore, we find missing number between (nums[i], nums[i+1])

1.  append `0` and `max(nums) + k + 1` in the beginning and end of nums. make sure we can always find enough k missing number.
2.  iterate (nums[i], nums[i+1]) to find first k unique elements


# Complexity

time: O(nlogn) for sorting
space: O(1)

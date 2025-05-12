# Intuition

The key idea is that we can only remove the minimum value of a subarray in one operation, and we can use this fact to design a smarter approach than brute-force.

Brute Force:
Approach:
For each unique number x > 0 in nums, find how many disjoint subarrays are needed to cover all its occurrences.

For example, if the array is [1, 2, 3, 2, 3, 2, 1, 1, 1, 2]:

For 1: we can remove all 1s in a single operation using a large enough subarray → +1
For 2: the 2s are broken across: [2,3,2,3,2], [2], hence ans += 2
Total operations = 3 so far, and similarly for 3.
For 3: [3], [3] blocks, that is ans += 2.
Final ans = 5.

### Optimized Approach (Monotonic Stack):

Observations:
Think in terms of increasing segments.
For every value that is greater than the last seen, and not already part of a valid subarray, we'll need a new operation.
We can use a monotonic stack to track the values and determine where a new operation is needed.

Why Monotonic Stack?
Because:
    - Each time we encounter a smaller number, we pop from the stack.
    - If the number is greater than the current top (or the stack is empty), we increment the operation count.

### Summary

```
{X X X X X X X X X} X
```

use stack to store nums[i] in order to represent subarray segment

- if stack[-1] == nums[i]: consecutive subarray => no extra operation here
- if stack[-1] > nums[i], which means older ones can't operate with nums[i] together, we should do operation to older ones. we should "go back" and deal without `num` using a new operation.
- if stack[-1] < nums[i], which means we must use a new operation to remove `nums[i]`, because all smaller numbers before it are already cleared.
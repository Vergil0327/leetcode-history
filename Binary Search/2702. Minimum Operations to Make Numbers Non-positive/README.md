[2702. Minimum Operations to Make Numbers Non-positive](https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/)

`Hard`

You are given a **0-indexed** integer array `nums` and two integers `x` and `y`. In one operation, you must choose an index `i` such that `0 <= i < nums.length` and perfom the following:
- Decrement `nums[i]` by `x`
- Decrement values by `y` at all indices except the `i-th` one.

Return the minimum number of operations to make all the integers in `num` less than or equal to zero.

```
Example 1:
Input: nums = [3,4,1,7,6], x = 4, y = 2
Output: 3
Explanation: You will need three operations. One of the optimal sequence of operations is:
Operation 1: Choose i = 3. then, nums = [1,2,-1,3,4]
Operation 2: Choose i = 3. then, nums = [-1,0,-3,-1,2]
Operation 3: Choose i = 4. then, nums = [-3,-2,-5,-3,-2]
Now, all the numbers are non-positive.

Example 1:
Input: nums = [1,2,1], x = 2, y = 1
Output: 1
```

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= y < x <= 10^9
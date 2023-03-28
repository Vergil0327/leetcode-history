# Intuition

Solve the reverse problem by Hint 2, but why?

based on constraints:
- 1 <= nums.length, k <= 1000
- 1 <= nums[i] <= $10^9$


`n` can up to **1000**, therefore, the sum can up to $10^9$ x 1000 which exceeds the memory limitation.

Since the maximum of `k` is only **1000**, we can calculate the number of combinations for sum strickly less than k


let's say we have two groups, `A` & `B`

since each nums[i] can put in either `A` or `B` groups. thus, we have $2^n$ partitions totally.

if we have $X$ invalid partitions in group `A`. it can happen in group `B`
therefore, final answer = $2^n$ - $2 * X$

and the problem turns into knapsack problem

# Complexity

- time complexity
$$O(nk)$$

- space complexity

$$O(nk)$$
# Intuition

The key insight is how we handle the k * i term. Initially, the problem states that for the ith subarray, we need to add k * i to the sum of elements

However, the solution uses k * (presum_cost[-1] - presum_cost[i]) instead.

Here's why this works:
Imagine we decide to split the array at index i, creating a subarray from nums[i] to nums[j]. The cost includes:

- `(sum of elements in subarray + k * position) * (sum of costs)`

When we add this subarray, all future subarrays will have their position increased by 1. This means:

- For all elements after position j, the k * position term increases by k
- This increase in cost is exactly: k * (sum of costs from index j+1 to the end)

Mathematical Explanation:

Consider two ways to split the array:

Split at i -> Creates subarrays with positions 1, 2, ..., n
Split at i+1 -> Creates subarrays with positions 1, 2, ..., n-1

The difference in cost comes from the k * position term. By splitting at i, we're essentially adding k to the position of every future subarray.
This incremental cost is exactly k * (sum of all costs from i to the end), which is what `k * (presum_cost[-1] - presum_cost[i])` calculates.


therefore, dp state should be:

```
{X X X X X} X X X X X X X X X
 l       r
```

dp[l] = dp[r+1] + presum_num[r] * (presum_cost[r+1] - presum_cost[l]) + k * (presum_cost[-1] - presum_cost[l])

where presum_num is 1-indexed prefix sum of nums
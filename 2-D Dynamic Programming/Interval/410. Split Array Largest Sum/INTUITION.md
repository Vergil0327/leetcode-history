# DP

## Intuition

對於將一個序列分成k個求極值的題目，我們可以這麼定義DP

dp[i][k]: the minimum largest sum for nums[:i] with k-th partition

**state transfer fn** should be:

we must found a `j` such that:
X X X [X X X]
   j-1 j   i

dp[i][k] = min(dp[i][k], dp[j-1][k-1] + sum(nums[j:i])),
and we can precompute prefix sum for this part `sum(nums[j:i])`

in the beginning, the core structure for dp is:
```py
n = len(nums)

dp = [[inf] * (K+1) for _ in range(n+1)]
nums = [0] + nums # to 1-indexed
dp[0][0] = 0

for i in range(1, n+1):
    for k in range(1, min(i, K)+1):
        total = 0
        for j in range(i, k-1, -1):
            total += nums[j]
            dp[i][k] = min(dp[i][k], max(dp[j-1][k-1], total))
```
there are some details in iteration.
- we change nums and set dp to 1-indexed to prevent dp[j-1][k-1] from out-of-bounds
- k's range should be [1:min(i,K)] because we can't have more partitions than i or K
- j's range should be k at least if we want to keep dp[j][k] valid.
- replace total summation with precomputed prefix sum

# Other Solution - Binary Search

## Intuition

首先subarray分得越多，largest sum就會越低
分的越少則越高，有個極值在所以可以考慮binary search試試

subarray至少為1，最多為全部因此search space則:
`[l, r] = [max(nums), sum(nums)]`

再來我們二分搜值就直接猜說largest sum是多少

我們遍歷nums一遍，Greedy的思想盡可能的把subarray組的越大越好，只要不超過我們猜的`mid`
假如最後分出來 `<=K`，就代表`mid`為可能解，我們解能縮短上界讓`r = mid`，反之則`l = mid+1`

## Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$
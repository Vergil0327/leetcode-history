# Intuition

首先subarray分得越多，largest sum就會越低
分的越少則越高，有個極值在所以可以考慮binary search試試

subarray至少為1，最多為全部因此search space則:
`[l, r] = [max(nums), sum(nums)]`

再來我們二分搜值就直接猜說largest sum是多少

我們遍歷nums一遍，Greedy的思想盡可能的把subarray組的越大越好，只要不超過我們猜的`mid`
假如最後分出來 `<=K`，就代表`mid`為可能解，我們解能縮短上界讓`r = mid`，反之則`l = mid+1`

# Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(1)$$
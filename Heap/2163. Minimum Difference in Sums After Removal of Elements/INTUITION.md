# Intuition
minimum difference = sum_first - sum_second
所以當:
    - 前n個數為first n lowest nums[i]
    - 後n個數為first n largest nums[i]
這時`sum_first-sum_second`會是最小的difference (越是負數越小)

nums = [7,9,5,8,1,3], n=2

[7,9] - [5,8,1,3]
[7,9,5] - [8,1,3]
[7,9,5,8] - [1,3]
左邊用min heap挑出n個最小, 右邊用max heap挑出n個最大, 兩邊總和相減得到當前分法的minimum difference

這時想到3-pass:

1. 首先先遍歷一遍, 找出到index `i`為止的前n個最小sum => 維護size為n的max heap
  - 因為必須保證右邊至少有n-size sum, 所以遍歷[n,2n)這範圍
2. 在逆著掃一遍, 找出到index `i`為止的最大n-sum => 維護size為n的min heap
  - 由於要保證左邊至少有n-size sum, 所以遍歷[n,2n]
3. 最後再掃一遍, 以O(n)時間找出以index `i`為界的lowest difference = min(min_sum[i]-max_sum[i])

# Complexity

time: $O(nlogn)$
space: $O(n)$
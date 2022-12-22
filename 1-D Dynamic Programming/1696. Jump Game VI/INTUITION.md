# 1-D Bottom-Up DP

## Intuition

首先我們可以很清楚知道，我們可以定義

dp[i]: the maximum scores for nums[:i]

因此狀態轉移方程則為: `dp[i] = d[i-k] + nums[i]`

Base case: dp[0] = nums[0]

可以很快寫出狀態轉移為:
```python
def maxResult(self, nums: List[int], k: int) -> int:
    n = len(nums)

    # dp[i]: maximum scores for nums[:i]
    dp = [-inf] * n
    
    # base case
    dp[0] = nums[0]

    for i in range(1, n):
        # 遍歷所有k找出最佳解
        for j in range(1, k+1):
            if i-j < 0: continue
            dp[i] = max(dp[i], dp[i-j]+nums[i])

    return dp[n-1]
```

## Optimized

但其實我們可以不用每次都從`i-k`到`i`之間線性尋找最大值
我們可以利用**max heap**來儲存我們的`dp`狀態，分別是`max score`與`index`

每次遍歷時:
- 一但dp超出`i-k`的範圍便從`max heap`中彈出
- 同時也可以迅速找出`i-k`範圍內的最大分數並加上`nums[i]`來更新我們的`dp`.
  - dp[i] = dp[max] + nums[i] where dp[max] within `i-k`

等到遍歷完後，從`max heap`中找出`dp[n-1]`即為我們要的答案

## Complexity

- time complexity:

$$O(nlogk)$$

- space complexity:

$$O(n)$$

## Further Optimized

dp: maximum score until nums[:i]

其實這題也就是Sliding Window Maximum的變形
利用Monotonically Decreasing Deque來維護`dp`

- 一但index超出i-k的範圍，便從deque中移除
- 更新dp的時候，因為是單調遞減，一但deque[-1]裡頭存的dp小於目前的dp時也移除，然後再把目前的dp加入到deque裡面，讓裡面永遠是單調遞減的

因為如果我們的window是長這樣

Sliding Window DP State: [8,7,6,5,4]
然後目前的dp[i] = 6
那們`5`跟`4`都可以移除，因為再考慮下一個dp[i+1]時，往回找的時候`dp[i]=6`永遠都優於`5`跟`4`，即使他們都處於合法的`i-k`範圍內

因此透過維護一個單調遞減的Sliding Window，我們可以用`O(n)`的時間複雜度找出max score

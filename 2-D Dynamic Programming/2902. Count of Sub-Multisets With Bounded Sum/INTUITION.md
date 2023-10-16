# Intuition

一開始想法: brute force

subset_sum = ({X X X X X X}) => l <= subset_sum <= r

用top-down dp:
1. dfs(i+1, tot)
2. dfs(i+1, tot+nums[i])
base case: return 1 if l <= tot <= r else 0 if i == n

```py
def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:
    arr = list(Counter(nums).items())
    nums.sort()
    n = len(arr)
    
    @cache
    def dfs(i, tot):
        if i == n:
            return 1 if l <= tot <= r else 0
        if tot > r: return 0

        res = dfs(i+1, tot)
        res %= 1_000_000_007

        for x in range(1, arr[i][1]+1):
            if tot+arr[i][0]*x > r: break
            res += dfs(i+1, tot+arr[i][0]*x)
            res %= 1_000_000_007
        
        return res
    return dfs(0, 0)
```

        
可看到這段是最耗時的
```py
for x in range(1, arr[i][1]+1):
  res += dfs(i+1, tot+arr[i][0]*x)
```

比起遍歷每個num加或不加, 我們可以看一下這個constraint
- Sum of nums does not exceed 2 * 10^4

如果我們定義: dp[i]: the ways to sum up i
base case: dp[0] = 1 for empty set
=> what we want is sum(dp[l] + ... + dp[r])

所以我們可以遍歷`num, freq in Counter(nums).items()`

對於num來說, 我們可以來更新dp[i]
如果我們不加num, dp[i] += dp[i-0]
如果我們加上1個num, dp[i] += dp[i-num]
...
dp[i] += dp[i-num*freq]
所以curr_dp[i] += prev_dp[i-num*k] for k in range(freq)
這段我們可以事先計算prefix sum, 使得
curr_dp[i] += presum_dp[i] - presum_dp[i-num*(k+1)]

0為例外處理, 加不加都不影響subset sum, 所以k個0的話有(k+1)種subset. (不加上0也是種選擇)
所以等於當前方法數再乘上**count[0]+1**
curr_dp[i] *= (count[0]+1)
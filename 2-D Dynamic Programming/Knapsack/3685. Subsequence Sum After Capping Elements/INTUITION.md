# Intuition

依題意敘述, 過程很像是knapsack problem:
定義dp[i][sum] (or just dp[sum]), 其中sum <= k

而過程中我們還有另個capped value `x`, 這個`x`相當於是個upperbound
那如果我們對nums**排序**的話, 這個`x`其實就會隨著`i`增加

這樣如果我們先撇除那些`>=x`的nums[i]的話, 其實就是個knapsack dp
我們遍歷所有可能`x`時, 也會像是在進行knapsack dp在遍歷可用的nums[i]
所以我們能透過knapsack dp找出, 對於當前的`x`來說, 所有`< x`這段區間的subseq.的所有可能`sum`, 藉此判斷是否可行

```py
n = len(nums)

res = [False] * n

nums.sort()

dp = [False] * (k+1)
dp[0] = True

i = 0
for x in range(1, n+1):
    while i < n and nums[i] < x:
        for _sum in range(k, 0, -1):
            if _sum - nums[i] < 0: break # avoid out-of-bounds

            # dp[i][sum] = dp[i-1][sum - nums[i]]
            dp[_sum] = dp[_sum] or dp[_sum - nums[i]]
        i += 1
    
    # 此時, dp[k]代表對於當前x來說, k是否是個合法subsequence sum
    res[x-1] = dp[k] # x: 1-indexed
```

所以到目前為止, 我們能得到對於當前`x`來說, `dp[k]`代表我們是否可以用目前所有 **<x** 的數來組出`k`

但別忘了我們還有額外的capped value可以用
所以後面我們在遍歷當前所有可用的capped value個數, 來更新res[x]: `if dp[k - x * cnt] == True: res[x] = True`

```py
i = 0
for x in range(1, n+1):
    # ...
    
    # 此時, dp[k]代表對於當前x來說, k是否是個合法subsequence sum
    res[x-1] = dp[k] # x: 1-indexed

    for cnt in range(n-i+1):
        extra = x * cnt
        if k - extra >= 0 and dp[k - extra]:
            res[x-1] = True # x: 1-indexed
            break
return res
```

# Resources

great video explanation by [@HuifengGuan](https://www.youtube.com/watch?v=G6xwQHlxRqQ&ab_channel=HuifengGuan)
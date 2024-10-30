# Intuition

首先得先找出我們能操作的每個連續相同字符串有哪些, 我們用`consecutive` 紀錄每個連續字符串的長度

```py
n = len(word)

consecutive = []
cnt = 1
for i in range(n-1):
    if word[i] == word[i+1]:
        cnt += 1
    else:
        consecutive.append(cnt)
        cnt = 1

consecutive.append(cnt)
```

那再來依題意, 對於每個`consecutive[i]`我們至少得選一個, 然後後續長度多少自選
相當於我們總共可能產生的字符串有: `total_ways = consecutive[0] * consecutive[1] * ... * consecutive[i]`種字串

最後如果我們能扣除所有長度不及`k`的字串, 那就是最終答案

special case: 如果`len(consecutive) >= k`, 也就是每段挑一個, 長度就已經滿足`k`的話, 那代表全部組合方式都是合法的, 可以直接返回`total_ways`

```py
m = len(consecutive)

total_ways = 1
for i in range(m):
    total_ways = (total_ways * consecutive[i]) % mod

if k <= m: return total_ways
```



再來定義dp[i][j]: the number of words of length exactly j using the first i consecutive segments (consecutive[:i])

那這樣要求出所有可能長度的話, 初始化如下所示, 但n約10^5級別, 如果再配上`m`, 那時間、空間上肯定不足
```py
dp = [[0]* (n+1) for _ in range(m+1)]
```

這時想的是, 我們前面已經知道如何求出所有可能的字符組合方式
那這樣我們如果要求出**至少長度為k**的合法字符串的話, 是不是把所有合法方法減去0到`k-1`長度的不合法方式
就是我們要的答案了

所以我們dp空間僅需要開到`m * (k-1)`即可, 目的是求出長度最多`k-1`的所有字符串組合方法數

```py
dp = [[0]* k for _ in range(m+1)]

# TODO: state transition

return ((total_ways - sum(dp[m])) + mod) % mod
```

首先base case:

```py
dp[0][0] = 1 # one way for 0 length of word with 0 segments
dp[i][0] = 0 # there is no way of making workds of size i with 0 segments
```

狀態轉移:

首先肯定遍歷當前考慮的consecutive[:i], 以及當前要組的字串長度`k`
那當前的dp[i][j]這狀態肯定是由`dp[i-1][0], dp[i-1][1], ..., dp[i-1][consecutive[i]]`這些狀態轉移過來

因此, `dp[i][j] += dp[i-1][j - seg] for seg in range(1, consecutive[i]+1)`

但要注意j-seg不可為負數, `consecutive[i]`最多長度使用到`j`個, 所以: `dp[i][j] += dp[i-1][j - seg] for seg in range(1, min(j, consecutive[i])+1)`

```py
for i in range(1, m+1):
    for j in range(k):
        for seg in range(1, min(j, consecutive[i-1])+1):
            dp[i][j] += dp[i-1][j - seg]
            dp[i][j] %= mod
```

所以整理在一起如下所示

time: O(m * k * m)
space: O(m * k)

```py
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7
        n = len(word)

        consecutive = []
        cnt = 1
        for i in range(n-1):
            if word[i] == word[i+1]:
                cnt += 1
            else:
                consecutive.append(cnt)
                cnt = 1
        consecutive.append(cnt)
        
        m = len(consecutive)

        total_ways = 1
        for size in consecutive:
            total_ways = (total_ways * size) % mod

        if k <= m: return total_ways
        
        dp = [[0]* k for _ in range(m+1)] # 1-indexed
        dp[0][0] = 1
        for i in range(1, m+1):
            for j in range(k):
                for seg in range(1, min(j, consecutive[i-1])+1):
                    dp[i][j] += dp[i-1][j - seg]
                    dp[i][j] %= mod

        return ((total_ways - sum(dp[m])) + mod) % mod
```

但可惜這樣O(m^2 * k)會Time Limit Exceeded (823 / 846 testcases passed)

這時要優化的話會發現最內層迴圈其實是一段連續的和, `dp[i-][(j-consecutive[i]) ... j]`去更新dp[i]
所以如果我們有prefix_sum_dp的話, 內層應可簡化成:

`dp[i][j] =  prefix_sum_prev_dp[j] - prefix_sum_prev_dp[j - min(j, consecutive[i-1])]`

```py
for i in range(1, m+1):
    prefix_sum_prev_dp = list(accumulate(dp[i-1], lambda x, y: (x+y)%mod, initial=0))

    for j in range(k):
        # for seg in range(1, min(j, consecutive[i-1])+1):
        #     dp[i][j] += dp[i-1][j - seg]
        #     dp[i][j] %= mod
        dp[i][j] =  prefix_sum_prev_dp[j] - prefix_sum_prev_dp[j - min(j, consecutive[i-1])]
        dp[i][j] %= mod
```

所以最終Complexity為:

- time:
  - O(n + k*k) for m < k
  - O(n) for m >= k

- space: O(k*k)
# Intuition

```py
X X X X X X
    j     i
```

由於是subsequence
首先想到的是對於當前的nums[i]來說，他可以接在公差相同的任意nums[j]上
接上去後的公差為nums[i]-nums[j]


如果我們定義dp[i]為:
dp[i][diff]: the longest length of arithmetic subsequence ends at `i` with `diff` arithmetic

那麼對於nums[i]來說, dp[i][diff]的狀態轉移就是之前的dp[j][diff]再加上當前的nums[i], 所以是:
```py
for i in range(n):
    for j in range(i):
        diff = nums[i]-nums[j]
        dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
```

由於公差可正可負, 所以我們用hashmap而非一般二維array來儲存
hashmap = { diff: longest length of arithmetic subseq. }

並且初始值設為1, 因為至少自己本身也是個subsequence

```py
dp = [defaultdict(lambda: 1) for _ in range(n)]
```

由於subsequence可能結束於任意一個位置
所以最後答案就是整個dp掃過一遍, 求出全局最長的arithmetic subsequence

```py
res = 1    
for m in dp:
    res = max(res, max(m.values()))
return res
```
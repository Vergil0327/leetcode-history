# Intuition

我們要求的是在不超過`m`個0及`n`個1的情況下, 對於每個`strs[i]`我們可選可不選
然後看我們合法的最大subset size是多少

由於這題也是在某個capability底下可選可不選，所以我們可以把這個想成是個背包問題
可以這麼定義dp:

`dp[i][m][n]: the largest size of subset considering first i strs with at most m 0's and n 1's`

那麼狀態轉移就是:

- if we can't choose strs[i]: dp[i][m][n] = dp[i-1][m][n]
- if we choose strs[i]: dp[i][m][n] = dp[i-1][m-count0(strs[i])][n-count1(strs[i])] + 1

由於在不超過m 0's跟n 1's的情況可能很多，而我們要求的是最大的subset size
所以我們從所有可能中取最大的:

```py
# dp[i][m][n]至少是dp[i-1][m][n] size
dp[i][m][n] = max(dp[i][m][n], dp[i-1][m][n])

# 如果可以選strs[i], 那就是dp[i][m][n] 跟 dp[i-1][m-zero][n-one] + 1裡面選大的
dp[i][m][n] = max(dp[i][m][n], dp[i-1][m-zero][n-one] + 1)
```

**base case**
由於i=0時dp[i-1]index會越界，所以我們i=0時單獨處理

```py
for mm in range(m+1):
    for nn in range(n+1):
        zero, one = strs[0].count("0"), strs[0].count("1")
        if mm-zero >= 0 and nn-one >= 0:
            dp[0][mm][nn] = 1
```

那根據定義最終答案就是`dp[len(strs)-1][m][n]`

# Space-optimized

由於dp[i]只跟dp[i-1]有關
所以我們可以只用兩個dp[m][n]數組來代表dp[i][m][n]跟dp[i-1][m][n]

# Futher Optimization

最後有個常見的技巧是如果dp[m][n]都是由dp[m-zeros][n-ones]
我們可以倒著進行狀態轉移，這樣就只需要一個dp array就好
因為這樣在更新完dp[m][n]後就確定了, 就相當於此時的狀態已經是prevdp了, 如下所示:

並且由於我們只在 mm-zero >= 0 and nn-one >= 0 更新，所以我們可以從後往前只遍歷到zero跟one就好
```py
for i in range(1, len(strs)):
    zero, one = counters[i]["0"], counters[i]["1"]
    for mm in range(m, zero-1, -1):
        for nn in range(n, one-1, -1):
            dp[mm][nn] = max(dp[mm][nn], dp[mm-zero][nn-one] + 1)
```

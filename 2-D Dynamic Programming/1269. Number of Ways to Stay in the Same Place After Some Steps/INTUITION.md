# Intuition

一開始想說因為必須得折返, 所以只有`min(steps//2, arrLen)`這些位置可以回到`index 0`
所以排列組合為 Right ... Right Left ... Left 然後穿插剩下的Stay

但實際上由於每次都只能往左往右跟停留, 所以其實狀態轉移已經出來了
如果更general點來看的話, 對於`steps`步後能抵達`pos`位置的步數定義成dp[step][pos]的話:

他的方法數只可能來自這三個位置
dp[step][pos] = dp[step-1][pos-1] + dp[step-1][pos] + dp[step-1][pos+1]

所以狀態轉移為:

```py
dp = [[0] * arrLen for _ in range(steps+1)]
for step in range(1, steps+1):
    for pos in range(arrLen):
        dp[step][pos] = dp[step-1][pos-1] + dp[step-1][pos] + dp[step-1][pos+1]
```

再來注意一下邊界條件
pos-1跟pos+1可能越界, 所以得稍微判斷一下

```py
dp = [[0] * arrLen for _ in range(steps+1)]
for i in range (1, steps+1):
    for pos in range(n):
        dp[i][pos] = ((dp[i-1][pos-1] if pos-1 >= 0 else 0) + 
                        dp[i-1][pos] + 
                        (dp[i-1][pos+1] if pos+1 < n else 0))
        dp[i][pos] %= mod
```

那最終答案就是dp[steps][0], 看steps步後, pos=0時有多少方法

但這樣會越界，但還記得我們一開始有想到說
其實我們只需要考慮`min(steps//2, arrLen)`這些位置即可
超出的範圍其實根本走不回`pos=0`的位置

所以我們不需要遍歷整個`arrLen`, 我們只需要遍歷`min(steps//2, arrLen)`這些位置即可

```py
dp = [[0]*(min(steps//2+1, n)+1) for _ in range(steps+1)]
for i in range (1, steps+1):
    for pos in range(min(steps//2+1, n)):
        dp[i][pos] = ((dp[i-1][pos-1] if pos-1 >= 0 else 0) + 
                        dp[i-1][pos] + 
                        (dp[i-1][pos+1] if pos+1 < n else 0))
        dp[i][pos] %= mod
return dp[steps][0]
```

然後別忘了邊界條件
我們steps是遍歷[1:steps], 為1-indexed
所以我們必須想一下dp[0][pos]的初始值為多少

只能走0步的時候:
dp[0][0] = 1
dp[0][pos] = 0 where pos > 0
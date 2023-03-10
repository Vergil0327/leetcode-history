# Intuition

對於每個i位置來說，都可以選擇要不要放上地毯，總共有`numCarpets`
很容易聯想到一個二維DP, DP狀態定義為

dp[i][j]: the maximum number of while tiles that are still visible by using `j` carpets  considering floor[:i]

初始值我們可以數一下總共有多少個白地板，最多就是每個都沒覆蓋到，所以初始值為`Counter[floor]["1"]`

因此整個dp框架會是兩層循環
外層循環為[0,n]個floor, 內層循環為使用[1,numCarpets]地毯
那對於dp[i][j]來說, 我們有兩種選擇:
1. 如果不在這放地毯，那麼dp[i][j] = dp[i-1][j]
2. 如果在這放上地毯，那麼dp[i][j] = (dp[i-carpetLen][j-1] if i-carpetLen >= 0 else totalWhiteTiles) - covered
   - ex. X X X X (i-carpetLen) [X X X X i], carpetLen = 5
   - covered就看[i-carpetLen+1, i]這段區間有多少個白地板可被覆蓋

然後我們就兩種決策取`min`即可

```py
totalWhite = Counter[floor]["1"]
for i in range(n):
    for j in range(1, numCarpets+1):
        covered = 0
        for k in range(max(0, i-carpetLen+1), i+1):
            if floor[k] == W:
                covered += 1
        dp[i][j] = min(dp[i-1][j], (dp[i-carpetLen][j-1] if i-carpetLen >= 0 else totalWhite) - covered)

return min(dp[n-1])
```

由於我們會需要反覆被carpet覆蓋的white tile區間和，所以我們可以事先計算presum，然後後續可以利用O(1)時間知道每個區間有多少white tiles被覆蓋

```py
presum = [0] * (n+1)
for i in range(1, n+1):
    presum[i] = presum[i-1]+(1 if floor[i-1] == W else 0)

totalWhite = presum[n]

# ...

for i in range(1, n):
    for j in range(1, numCarpets+1):
        # for k in range(max(0, i-carpetLen+1), i+1):
        #     if floor[k] == W:
        #         covered += 1

        # 上面可以替換成這行
        covered = presum[i+1]-presum[max(0, i-carpetLen+1)]
        dp[i][j] = min(dp[i-1][j], (dp[i-carpetLen][j-1] if i-carpetLen >= 0 else totalWhite) - covered)

return min(dp[n-1])
```
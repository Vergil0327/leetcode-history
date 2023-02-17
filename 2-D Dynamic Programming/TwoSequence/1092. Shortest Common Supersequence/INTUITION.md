# Intuition

要找length of Shortest Common Supersequence

XX[X]
YY[Y]
如果 X = Y, 那麼最後組成的SCS就加上X即可包含兩個字串，代表長度+1
如果 X != Y, 那們就是{XX...[X]}與{YY....}找出的SCS+[Y]和{XX....}與{YY...[Y]}找出的SCS+[X]兩種取最短SCS

也就是我們可以這樣定義dp:

`dp[i][j]: the length of shortest common supersequence considering str1[0:i] and str2[0:j]`

狀態轉移就如上分析:

```py
for i in range(1, m+1):
    for j in range(1, n+1):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
```

那最終結果就是 `dp[m][n]` 考慮m長度str1以及n長度str2的SCS

## base case
由於我們是從1-indexed開始，所以我們要考慮一下邊界條件，分別是:
1. dp[0][0]
2. dp[0][j]
3. dp[i][0]

兩邊都是empty string, 所以len(SCS) = 0
dp[0][0] = 0

一邊為empty string, 那們len(SCS)就為另外一邊的長度
for i in range(1, m+1):
    dp[i][0] = i

for j in range(1, n+1):
    dp[0][j] = j

如果我們再更新dp的時候同時存下構造的SCS，這樣會Memory Limit Exceeded，所以我們只能透過dp[m][n]這個資訊來構造

我們是bottom-up的方式求出dp[m][n]，現在我們可以反過來透過最佳解的選擇重構出最佳解的SCS

我們可以用雙指針來逐個比較str1[i]跟str2[j]以及利用dp[i][j]的資訊來反過頭來構造出最佳解

如果說最終結果`res`長度為dp[m][n], 我們可以反過來找出每個最佳解存到res裡

res = [""] * dp[m][n]
1. 如果 str1[i] == str2[j]，代表dp[i][j]是從dp[i-1][j-1]+1來的, 就代表res[i]是str1[i]
2. 如果 dp[i][j] == dp[i-1][j]+1, 代表res[i]是str1[i]
3. 如果 dp[i][j] == dp[i][j-1]+1, 代表res[i]是str2[j]

```py
while i > 0 and j > 0:
    if str1[i] == str2[j]:
        res[k] = str1[i]
        i, j, k = i-1, j-1, k-1
    elif dp[i][j] == dp[i-1][j]+1:
        res[k] = str1[i]
        i, k = i-1, k-1
    else: # dp[i][j] == dp[i][j-1]+1:
        res[k] = str2[j]
        j, k = j-1, k-1
```

當跳出循環後，可能是 i = 0或是 j= 0
把剩下的加回去res[i]裡即可
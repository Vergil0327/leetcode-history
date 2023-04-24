# Intuition

最初想到的是利用dp[i][j]來代表s[i:j]這區間內的最長palindrome長度
```
X [X X] X X X X X X X
i                   j

dp = [[-inf]*n for _ in range(n)]
for length in range(2, n+1):
    for i in range(n-length+1):
        j = i+legnth-1
        if s[i] == s[j]:
            dp[i][j] = max(dp[i][j], (dp[i+1][j-1] if i+1 < j-1 else 0)+2)
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
return dp[0][n-1]
```

但這題多了一個這個限制: No two consecutive characters are equal
所以如果我們要在dp[i+1][j-1]之上再加上s[i], s[j]
還得要求dp[i+1][j-1]這段區間的回文不可與s[i], s[j]相等

所以我們還得紀錄這狀態, 所以我們用dp[i][j][k]來紀錄dp[i][j]是結束在`k`這個character的最長回文長度

然後一樣分情況討論:

```
X {X X X X X X X X} X
i                   j

{X X X X X X X X X} X
i                   j

X {X X X X X X X X X}
i                  j
```

- if s[i] == s[j]
  - dp[i][j][s[i]] = max(dp[i][j][s[i]], dp[i+1][j-1][k]+2) where s[i] != k for k = a, b, c, d, ...., x, y, z
  - dp[i][j][k] = dp[i+1][j-1][k] where k != s[i] for k = a, b, c, d, ...., x, y, z
  
- if s[i] != s[j]
  - dp[i][j][s[i]] = dp[i][j-1][s[i]]
  - dp[i][j][s[j]] = dp[i+1][j][s[j]]
  - dp[i][j][k] = dp[i+1][j-1][k] where k != s[i] and k != s[j] for k = a, b, c, d, ...., x, y, z
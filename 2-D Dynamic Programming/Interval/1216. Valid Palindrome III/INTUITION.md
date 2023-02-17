# Intuition

目的是要找出一個長度為`n-k`的palindrome，所以我們只要看s的子序列中的最長palindrome長度為多少
如果總長度 `n` 減掉最長palindrome子序列長度小於等於`k`的話，代表s為k-palindrome

定義 dp[l][r]: the maximum length of palindrome which exists in `s`

狀態轉移方程為:

```py
for length in range(1, n+1):
    for l in range(l-length+1): # because r = l+length-1 < n
        r = l+length-1
        if s[l] == s[r]:
            dp[l][r] = dp[l+1][r-1] + 2
        else:
            dp[l][r] = max(dp[l][r-1], dp[l+1][r])
return n-dp[0][n-1] <= k
```
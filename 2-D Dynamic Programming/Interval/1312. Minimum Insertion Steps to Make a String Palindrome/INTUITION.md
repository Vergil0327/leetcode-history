# Intuition

對於一個回文串，左右兩個端點`s[l]`跟`s[r]`會相等，所以對一個string `s`來說:
1. 如果左右兩個端點相等的話，那就繼續考慮s[l+1:r-1]
2. 如果兩個不相等的話，那我們有兩種選擇：
   1. 在右側加上s[l] 然後繼續看s[l+1:r]是不是Palindrome
   2. 在左側加上s[r] 然後繼續看s[l:r-1]是不是Palindrome
   3. 那我們肯定是兩種決策選最佳

所以這會是個區間型Dynamic Programming，我們從小區間的子問題先解決然後再解決大區間
並且最關鍵的一點就是Hint 2
那當我們找出`s`裡的最長回文串後，需要插入的數量就是`n-最長回文串的長度`

所以我們可以這樣定義DP:

`dp[l][r]: the maximum length of palindrome which exists in s[l:r]`

那最長回文串的狀態轉移就是:

s[l]跟s[r]如果相等，長度+2
不相等就從s[l+1:r]跟s[l:r-1]裡找最長的回文串

```py
if s[l] == s[r]:
    dp[l][r] = max(dp[l][r], dp[l+1][r-1]+2)
else:
    dp[l][r] = max(dp[l+1][r], dp[l][r-1])
```

**base case**

起始值為0
length=1時，l==r, dp[l][r] = 1

**但這題也可以直接這麼定義DP**

`dp[l][r]: the maximum insertion to make 's' as a palindrome`

那這樣狀態轉移就會是:

```py
if s[l] == s[r]:
    dp[l][r] = dp[l+1][r-1] # 我們不用插入任何字
else:
    dp[l][r] = min(dp[l+1][r]+1, dp[l][r-1]+1) # 看一開始的分析，要麻左側加上s[r]、要麻右側加上s[l]，然後看另一側是不是Palindrome

return dp[0][n-1]
```

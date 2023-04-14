# Intuition

X X X X X X X X X X X X X X X X X X X X X
                        j               i

首先觀察後的想法是如果我們考慮第`i`個元素
如果他跟第j個相同，那我們就看s[j+1][i-1]有多少個palindrome subseq.再加2即可

如果s[i]不等於s[j], 那s[j:i]這段就看s[j:i-1]跟s[j+1:i]這兩段，取最大的palindrome subseq.

所以首先想到的狀態轉移方程為:

```py
if s[i] == s[j]:
    dp[j][i] = max(dp[j][i], dp[j+1][i-1] + 2)
else:
    dp[j][i] = max(dp[j+1][i], dp[j][i-1])
```

所以我們可以遍歷i然後再往前遍歷j來更新dp[j][i]
其中dp[j][i]: the maximum length of palindrome subseq. in s[j:i]

那要注意的是當`j+1 > i-1`的時候dp[j+1][i-1]是不合法的
所以我們得再加上個`if-else`

如果`j+1 > i-1`，那代表他的前驅狀態dp[j+1][i-1]為0

所以框架為:
```py
for i in range(n):
    for j in range(i-1, -1, -1):
        if s[i] == s[j]:
            if j+1 > i-1:
                dp[j][i] = max(dp[j][i], 2)
            else:
                dp[j][i] = max(dp[j][i], dp[j+1][i-1] + 2)
        else:
            dp[j][i] = max(dp[j][i-1], dp[j+1][i])
return dp[0][n-1]
```

那最終答案就是dp[0][n-1], 代表考慮s[0:n-1]的最長palindrome subseq.

至於dp[i][j]的初始狀態為1, 每個單獨字母都是palindrome
所以我們在遍歷`j`時, 也可以直接從`i-1`開始往前找


由於我們在更新dp[j][i]時會用到dp[j+1][i-1]
所以我們的`j`從後往回遍歷，這樣才能確保我們要更新dp[j][i]時dp[j+1][i-1]已經更新過了

# Complexity

- time complexity
$$O(n^2)$$

- space complexity
$$O(n^2)$$

# Space Optimization

由於dp[r]只跟dp[r-1]有關, 同理dp[l]也只跟dp[l+1]有關
我們可以用兩個一維數組來更新dp

所以這邊我們用兩個一維數組:
dp[l]跟prevdp[l]來代表dp[l][r]跟dp[l][r-1]

其中要注意的是dp[r]當前還未更新, 初始值應為1

```py
dp = [1] * n
prevdp = [1] * n

for r in range(n):
    dp[r] = 1
    for l in range(r-1, -1, -1):
        if s[r] == s[l]:
            if s[r] == s[l]:
                if l+1 > r-1:
                    # dp[l][r] = max(dp[l][r], 2)
                    dp[l] = max(dp[l], 2)
                else:
                    # dp[l][r] = max(dp[l][r], dp[l+1][r-1] + 2)
                    dp[l] = max(dp[l], prevdp[l+1] + 2)
        else:
            # dp[l][r] = max(dp[l][r-1], dp[l+1][r])
            dp[l] = max(prevdp[l], dp[l+1])
    dp, prevdp = prevdp, dp
return prevdp[0]
```
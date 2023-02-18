# Intuition

一旦nums1[i]跟nums2[j]連線，nums1[0:i]跟nums2[0:j]就決定了狀態並且無法更動，因為此時這段再與後面任一連線都會有交叉點存在
而前面nums1[0:i]跟nums2[0:j]的狀態會影響後面
有無後效性並且後面狀態取決於前面的狀態
所以我們可以用dynamic programming來試著找出最多的連線是多少

我們可以試著這樣定義dp:

`dp[i][j]: the maximum number of uncrossed lines considering nums1[0:i] and nums2[0:j]`

那狀態轉移方程則為:

nums1 = XXXXXXX[X]
                i
nums2 = YYYYY[Y]
              j
當我們考慮第i個nums1[i]跟第j個nums2[j]
如果 nums1[i] 跟 nums2[j] 相等，代表我們可以對他們連線，此時
dp[i][j] = dp[i-1][j-1] + 1

如果兩個不相等，那就看nums1[0:i]跟nums2[0:j-1]或nums1[0:i-1]跟nums2[0:j]誰有有更多的連線
dp[i][j] = max(dp[i-1][j], dp[i][j-1])

Let's see example 1 :

nums1 = [1,4,2]
nums2 = [1,2,4]
Output: 2

nums1[i] nums2[j]
   1        1     -> 1
   1        2     -> max(dp[0][2], dp[1][1]) = 1
   1        4     -> max(dp[0][3], dp[1][2]) = 1

   4        1     -> max(dp[2][0], dp[1][1]) = 1
   4        2     -> max(dp[2][1], dp[1][2]) = 1
   4        4     -> 1+1 = 2

   2        1     -> max(dp[2][0], dp[1][1]) = 1
   2        2     -> 1 + 1 = 2
   2        4     -> max(dp[2][3], dp[3][2]) = 2

因此狀態轉移方程為

```py
m, n = len(nums1), len(nums2)

# shift to 1-indexed
nums1 = [0] + nums1
nums2 = [0] + nums2

for i in range(1, m+1):
    for j in range(1, n+1):
        if nums1[i] == nums2[j]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
return dp[m][n]
```
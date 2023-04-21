# Intuition

```
X X X X [X] {X X X X} [X] 
i        k  k+1   j-1  j
```

首先這看起來是個區間型的dp
對於arr[i:j]來說, 我們在裡面找一個arr[k]:

如果arr[k] == arr[j], 代表這兩個可以組成palindrome, 可以一起刪除
我們先定義dp[i][j] = minimum moves for arr[i:j] (both inclusive)
所以狀態轉移則為:

```py
if arr[k] == arr[j]:
    # dp[i][j] = dp[i][k-1] + max(dp[k+1][j-1], 1)
    dp[i][j] = dp[i][k-1] + (dp[k+1][j-1] if k+1 <= j-1 else 0)
```
由於arr[k]跟arr[j]能與arr[k+1:j-1]的最後一次刪除一併刪除, 所以就看dp[i][k-1]跟dp[k+1][j-1]這兩段
但要注意的是如果當k+1 < j-1時, 此時dp[k+1][j-1]=0, 同時也代表這段區間不合法
但至少需要有一個刪除來移除arr[i]跟arr[j]
所以`max(dp[k+1][j-1], 1)` 或是的判段dp[k+1][j-1]不合法的情況

ex. arr[k:j] = 4 2 3 4
               i     j
dp[1][2] = 2 (刪除2, 刪除3), 在刪除3時arr[i], arr[j]能一併刪除

ex. arr[k:j] = 4 2 2 4 
               i     j
dp[1][2] = 1 (一次刪除22), 此時arr[i], arr[j]也能一併刪除

**edge case**

同時注意裡面有個`k-1`存在於dp[i][k-1]
所以也要特別判斷k-1是不是合法
- k-1必須不超過左邊界, 也就是`k-1 >= i`才合法
- 不然dp[i][k-1]相當於一段空的string, 此時`dp[i][k-1]=0`
# Intuition

看到example 3得知我們必須至少移除一個數
所以如果all(nums[i] == 1), 那就直接返回n-1

再來就是考慮有0的狀況
```
i-1 i
 1  1
 0  1
 1  0
 0  0
```

先假設dp[i]: the size of longest non-empty subarray considering nums[:i]
如果nums[i] == 1:
    - dp[i] = dp[i-1]+1
如果nums[i] == 0:
    - 如果前一位是0, 那麼dp[i]=0
    - 如果前一位是1
        - 那麼我們可以選擇刪除nums[i], 此時長度為dp[i-1]
        - 但我們也可以選擇不刪除nums[i], 此時長度為dp[i] = 0
        - 從這裡得知我們可能還必須紀錄狀態, 就是我們當前有沒有刪除過

所以我們定義:
    - dp[i][0]: the size of longest non-empty subarray considering nums[:i]
    - dp[i][1]: the size of longest non-empty subarray considering nums[:i] and already remove one element

那最終答案就是從dp[i][1]中找一個最大的

**base case**
由於我們dp[i]會需要dp[i-1]所以我們範圍從[1,n-1]開始
dp[0][0] = nums[0]
dp[0][1] = invalid = -inf

**edge case**
前面提到: `如果all(nums[i] == 1), 那就直接返回n-1`
如果最後dp[i][1]全部都為-inf的話, 那就直接返回n-1
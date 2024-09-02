# Intuition

首先, 先想如果不管queries[i]的話, 該如何計算XOR score?

```
XOR score:

nums[i]          nums[i+1]                 nums[i+2]          nums[i+3]
     nums[i]^nums[i+1]   nums[i+1]^nums[i+2]    nums[i+2]^nums[i+3]
         (nums[i]^nums[i+1])^(nums[i+1]^nums[i+2])
         上式最後等於nums[i]^nums[i+2]
```

因此: `XOR_SCORE(nums[i:j]) = XOR_SCORE(nums[i][j-1]) ^ XOR_SCORE(nums[i+1][j])`
相當於: `score[i][j] = score[i][j-1] ^ score[i+1][j]`

所以我們已經知道如何預先計算score[i][j]

```py
n = len(nums)
score = [[0]*n for _ in range(n)]
for i in range(n):
    score[i][i] = nums[i]

for length in range(2, n+1):
    for i in range(n-length+1): # j = i+length-1 < n
        j = i+length-1
        score[i][j] = score[i][j-1] ^ score[i+1][j]
```

那在有了所有xor_score後, 再來看該如何高效找出範圍內的最大值

首先想到的是：既然我們會求出所有score[i][j], 那麼我們能不能在求score[i][j]的同時計算出dp[i][j], 其中dp[i][j]定義為 the maximum score within nums[i:j]

對於區間型dp, dp[i][j], 常見地就是我們就看dp[i][j-1]跟dp[i+1][j]這兩個區間以及這整個區間的score[i][j]

首先base case: dp[i][i] = nums[i]

狀態轉移: dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1], score[i][j])

```py
n = len(nums)
score = [[0]*n for _ in range(n)]
dp = [[0]*n for _ in range(n)]
for i in range(n):
    score[i][i] = dp[i][i] = nums[i]

for length in range(2, n+1):
    for i in range(n-length+1): # j = i+length-1 < n
        j = i+length-1
        score[i][j] = score[i][j-1] ^ score[i+1][j]

        dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1], score[i][j])
        

return [dp[l][r] for l, r in queries]
```
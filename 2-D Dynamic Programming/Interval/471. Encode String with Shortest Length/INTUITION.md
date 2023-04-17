# Intuition

首先對於整個字串，我們要先找出可以encode的每個分段

s = X X X X X X X X X {[X X] [X X] [X X] [X X]}
                        i                   j

我們定義dp[i][j]為:
dp[i][j]: the shortest encoded string for s[i:j]

所以我們遍歷每個個分段試著找出他們的encode string

```py
n = len(s)
for length in range(1, n+1):
    for i in range(n-length+1): # j = i+length-1 < n
        j = i+length-1
        dp[i][j] = encode(i, j)
```

至於encode的方法則為:
1. 首先判斷能不能encode
2. 如果可以, 在看encoded string有沒有比原本的來得短
3. 找出全局最短的encoded string
4. 這裡最需要注意的是如何encoded string
   - 這邊的encoded string並不是原本的s[l:l+length], 而是dp[l:l+length-1] 
   - 因為如果這段本身可以被encoded, 我們應該就encoded後的部分繼續encoded
   - 從example 5可以看出會需要遞歸處理, 需要將大區間encoded string分解成小區間encoded string

```py
def encode(l, r):
    substr = s[l:r+1]
    m = len(substr)
    res = substr
    for length in range(1, m):
        # 如果不能整除, 代表無法分成repeated string
        if m%length != 0: continue

        repeated = True
        for i in range(0, m-length+1, length):
            if substr[i:i+length] != s[:length]:
                repeated = False
                break
        
        # !!! important
        encoded = f"{m//length}[{dp[l][l+length-1]}]"

        if repeated: # 如果可以encode, 再比較長度
            if len(encoded) < len(res):
                res = encoded
    return res
```

s = X X {X X X X X X X} {[X X] [X X] [X X] [X X]}
         i           k   k+1                  j

再來我們就還需要看對於s[i:j]這個區間, 能不能在分解成兩個encoded string組成的小區間

所以我們必須再遍歷分割點:
```py
for k in range(i:j):
    if len(dp[i][k]) + len(dp[k+1][j]) < dp[i][j]:
        dp[i][j] = dp[i][k] + dp[k+1][j]
```

那最終答案就是看整個長度的最短encoded string `dp[0][n-1]`
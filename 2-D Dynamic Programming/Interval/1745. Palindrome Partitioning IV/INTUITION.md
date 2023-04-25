# Intuition

```
X X X X X X X X {X X X X}
i                k     j
```

如果總共要分成m個palindrome substring
s[k:j]可以分成palinedrome的話, s[i:k-1]還要能分成m-1個palindrome

所以如果定義dp[i][j][m]代表s[i:j]能分成m個palindrome的話
我們就看s[i:k-1]能不能分成m-1個palindrome且s[k:j]是不是也是palindrome

`dp[i][j][m] = dp[i][k-1][m-1] and isPalindrome[k][j]`

那麼`isPalindrome`我們可以用O(n^2)時間來提前處理看s[i:j]是不是palindrome

```py
ispal = [[False]* n for _ in range(n)]
for length in range(1, n+1):
    for i in range(n-length+1):
        j = i+length-1
        if s[i] == s[j]:
            # length = 1: a
            # length = 2: aa
            # length = 3: aba
            ispal[i][j] = length <= 3 or ispal[i+1][j-1]
```

但這樣用三維dp來計算會超時(TLE)
```py
def checkPartitioning(self, s: str) -> bool:
    n = len(s)
    M = 3

    ispal = [[False]* n for _ in range(n)]
    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i+length-1
            if s[i] == s[j]:
                ispal[i][j] = length <= 3 or ispal[i+1][j-1]

    dp = [[[False] * (M+1) for _ in range(n)] for _ in range(n)]

    # m = 1, dp[i][j][1] = s[i:j]能不能分成1個palindrome
    for length in range(1, n+1):
        for i in range(n-length+1):
            j = i+length-1
            for k in range(j, i-1, -1):
                dp[i][j][1] = ispal[k][j]

    for m in range(2, M+1):
        for length in range(m, n+1):
            for i in range(n-length+1):
                j = i+length-1
                for k in range(j, i-1, -1):
                    dp[i][j][m] = dp[i][j][m] or (dp[i][k-1][m-1] and ispal[k][j])

    return dp[0][n-1][M]
```

但實際上我們不需要用m來逐次遍歷

```
[X X X X X X X] [X X X X X X] [X X X X X X X]
             i             j
```

我們可以直接在s裡利用`i`, `j`找出三段區間, 暴力搜索並且用預處理好的`ispal`來判斷這三段區間是不是都是palindrome
只要`ispal[0][i] and ispal[i+1][j] and ispak[j+1][n-1]`為**True**, 我們就直接返回True即可
這樣時間複雜度就只會是**O(n^2)**
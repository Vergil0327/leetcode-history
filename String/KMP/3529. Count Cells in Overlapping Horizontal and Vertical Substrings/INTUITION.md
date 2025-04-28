# Intuition

首先題目要row-by-row, column-by-column兩種方式去找出有沒有符合pattern的substring
那其實就是將整個grid分別沿著row方向, 以及column方向組成一個`s`後, 找出符合pattern的substing

=> 從string裡找出pattern的合法位置 => KMP algorithm

```py
def preprocess(s):
    n = len(s)
    lps = [0]*n

    for i in range(1, n):
        j = lps[i-1]
        while j >= 1 and s[i]!=s[j]:
            j = lps[j-1]
        lps[i] = j + int(s[i] == s[j])
    return lps

# return index of target in s
def kmp(s: str, target: str):
    n = len(s)

    # preprocess
    # longest prefix suffix
    lps = preprocess(target)

    # find target word in s
    res = []
    j = 0
    for i in range(n):
        while j > 0 and s[i] != target[j]:
            j = lps[j-1]
        j = j+int(s[i] == target[j])
        if j == len(target):
            j = lps[j-1]
            res.append(i-len(target)+1)
    return res

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])

        hozizontal = ""
        for i in range(m):
            for j in range(n):
                hozizontal += grid[i][j]

        vertical = ""
        for j in range(n):
            for i in range(m):
                vertical += grid[i][j]

        indice1 = kmp(hozizontal, pattern)
        indice2 = kmp(vertical, pattern)
```

那在有了`indice1`及`indice2`後

我們只要遍歷每個grid[i][j], 然後看該位置有沒有落在合法的`indice1`及`indice2`區間內即可

1. 將(i,j)轉換成**row-by-row string**的index: `pos1 = i*n+j`
2. 將(i,j)轉換成**column-by-column string**的index: `pos2 = i+j*m`
3. 利用binary search找出可能涵蓋(i,j)的區間
4. 若(i,j)被兩邊所涵蓋 => `res += 1`

```py
res = 0
for i in range(m):
    for j in range(n):
        pos1 = i*n+j
        idx1 = bisect_right(indice1, pos1)-1
        if idx1 >= 0 and indice1[idx1] <= pos1 < indice1[idx1]+len(pattern):
            pos2 = i+j*m
            idx2 = bisect_right(indice2, pos2)-1
            if idx2 >= 0 and indice2[idx2] <= pos2 < indice2[idx2]+len(pattern):
                res += 1
return res
```
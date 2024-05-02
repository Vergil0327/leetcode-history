# Intuition

# Intuition

ex1. "aa", "ac", "ad", ..., "az", "ca", "cc", ..., "cz", "da"
ex3. "gy", "gz"
ex2. "leetcode", "leetcodf", ... => 通通都含有evil => 0 valid string

=> think of digit DP intuitively

一開始是這麼想的, 就像digit DP那樣, 透過是不是已經**大於s1**跟**小於s2**來判斷我們可使用的character range
然後:
1. 如果ch == evil[j]: j += 1
2. 如果ch != evil[j]: reset j to 0
3. base case: if j == len(evil): return 0
4. base case: if i == n: return 1

```py
def dfs(i, j, gtS1, ltS2):
    """
    i: size of valid string size
    j: matched substring size of evil in current valid string
    """
    if j == len(evil): return 0
    if i == n: return 1

    start = ord("a") if gtS1 else ord(s1[i])
    end = ord("z") if ltS2 else ord(s2[i])
    res = 0
    for k in range(start, end+1):
        ch = chr(k)
        if ch == evil[j]:
            res += dfs(i+1, j+1, gtS1 or ch > s1[i],  ltS2 or ch < s2[i])
        else:
            res += dfs(i+1, 0, gtS1 or ch > s1[i],  ltS2 or ch < s2[i])

    return res
```

但這時會發現會fail: n=8, s1=pzdanyao, s2=wgpmtywi, evil=sdka
當下實在是想不出哪裡錯, 事後看討論才發現我們不能**reset j to 0 if ch != evil[j]**
這是因為:

In case the character you add to your dp solution doesn't match the last character of the prefix of evil you might need to increase j by more than 1.

例如evil="ababac", 而目前建構的string為"ababa"
下個字母`ch`我們選擇"b"的話, 變成: "ababa" + "b" = "ababab"
並且由於`b != c`, 也就是`b != evil[j]`, 所以我們下次dfs的時候reset j = 0

但其實此時的matched substring size of evil為"abab", 仔細看當前的string的suffix仍等於evil的prefix "abab"
所以直接reset j = 0這個邏輯是有盲點的

所以我們的j不該直接重設為0, 而是必須找出當前建構的string的suffix跟evil的prefix的共通長度
也就是必須找出common prefix suffix of string and evil
而這個common prefix suffix其實就是KMP的預處理部分, 所以這題除了digitDP外, 還必須利用KMP來計算`j`
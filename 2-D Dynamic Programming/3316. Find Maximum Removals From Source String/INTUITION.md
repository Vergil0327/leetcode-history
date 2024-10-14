# Intuition

`targetIndices`裡有些可用可不用, 首先想到的是top-down dp with take-or-skip strategy

首先先全部使用, 將`targetIndices[j]`替換成`#`

```py
n = len(source)

s = ""
j = 0
for i, ch in enumerate(source):
    if j < len(targetIndices) and i == targetIndices[j]:
        s += "#"
        j += 1
    else:
        s += ch
```

再來我們就定義dfs(i, j): the minimum number of removing operations we can't take considering s[:i] to contains pattern[:j]

對於每個s[i]我們可以選擇:
1. skip: 
   1. 那這樣假如s[i] == pattern[j], 也就是s[i]滿足pattern[j], 那狀態轉移就是dfs(i+1, j+1), 下個目標就是滿足pattern[j+1]
   2. 如果s[i] != pattern[j], 那就轉移dfs(i+1, j)
   3. 相當於dfs(i+1, j + (1 if j < len(pattern) and s[i] == pattern[j] else 0))
2. 如果s[i] == "#", 那我們可以選擇restore, 假如我們選擇restore, 那們s[i]就還原成source[i] 這下就看:
   - 假如source[i] == pattern[j], 也就是source[i]滿足pattern[j], 那狀態轉移就是dfs(i+1, j+1), 下個目標就是滿足pattern[j+1]
   - 如果source[i] != pattern[j], 那就轉移dfs(i+1, j)
   - 相當於dfs(i+1, j + (1 if j < len(pattern) and s[i] == pattern[j] else 0)) + 1

3. 邊界條件:
   - if j >= len(pattern): 代表當前`s`滿足pattern, `return 0`
   - if i >= len(s): 代表沒有滿足pattern, `return inf`

如此一來, `dfs(0, 0)`返回我們最小還原操作數
所以我們要的最大操作數相當於: `len(targetIndices) - dfs(0, 0)`
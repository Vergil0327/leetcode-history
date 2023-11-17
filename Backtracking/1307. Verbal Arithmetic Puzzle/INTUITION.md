# Intuition

一開始想了想, 好像只有backtracking(暴力搜索)求解一途
=> try to distribute 0-9 to every existing characters.

但要注意的是, 由於`sum(decode(words[i])) == sum(decode(result))`這個條件
所以我們在進行backtracking, 試著將0-9分配到每個words[i][j] character時, 其實就會同時確立result[j]了

亦即 (例如ex.2)
```
words[i]
- - - - - - - - - -
   SIX words[0]
 SEVEN words[1]
 SEVEN words[2]

TWENTY result

```

我們從個位數往上搜索
首先個位數: (X + N + N + carry)%10 = Y
再來十位數: (I + E + E + carry)%10 = T
再來百位數: (S + V + V + carry)%10 = N
...
過程中只要有任一等式失效, 那就是錯誤的

所以我們用個decode[ch] array紀錄當前`ch`代表的數值為`decode[ch]`

再來由於每個英文字母都是distinct number, 所以用`used[digit]`來紀錄當前`digit`有沒有被使用過

所以dfs batracking的框架為:

i代表當前words[i], j代表當前位數, 我們要從低位數往高位數開始
所以先把`result`跟`words[i]`都反轉一下讓i=0為個位數
```py
result = result[::-1]
for i in range(len(words)):
    if len(words[i]) > len(result): return False
    words[i] = words[i][::-1]
```

然後開始把0-9分配給words[i][j]
這邊有個**Edge Case**要注意的就是: words[i]不可以有leading zero

```py
decode = [-1]*26
used = [0]*10
key = lambda x: ord(x)-ord("A")

def dfs(i, j, total):
    ch = key(words[i][j])
    if decode[ch] != -1:
        if len(words[i]) > 1 and i == len(words[i])-1 and decode[ch] == 0: # leading zero
            return False
        return dfs(i+1, j, total + decode[ch])
    else:
        for d in range(10):
            if used[d]: continue
            if len(words[i]) > 1 and i == len(words[i])-1 and d == 0: continue # leading zero

            decode[ch] = d
            used[d] = 1
            if dfs(i+1, j, total + decode[ch]): return True
            decode[ch] = -1
            used[d] = 0
        return False
```

那dfs的base case就是:

1. 對當前位數`j`, words[i]已全部遍歷完的話就換到下一位數, 同時`sum(decode(words[i][j]))`的個位數數值必須跟`decode(result[j])`相等, 而十位數則會進到下一位

```py
if i == len(words):
    char = key(result[j])
    
    if decode[char] != -1:
        if decode[char] != total%10:
            return False
        else:
            return dfs(0, j+1, total//10)
    else:
        if used[total%10]: return False

        decode[char] = total%10
        used[total%10] = 1
        if dfs(0, j+1, total//10): return True
        decode[char] = -1
        used[total%10] = 0
        return False
```

2. 如果當前words[i]沒有這一位數, 那就換到words[i+1]

```py
if j >= len(words[i]):
    return dfs(i+1, j, total)
```

3. 如果搜索到最後一位, 那就判斷
   - result[-1]是不是為0, 一樣不可以有leading zero
   - total總和有沒有為0, 如果不為0代表words[i]加總後位數比result還多

```py
if j == len(result):
    if len(result) > 1 and decode[key(result[i-1])] == 0: # leading zero
        return False
    
    return total == 0
```
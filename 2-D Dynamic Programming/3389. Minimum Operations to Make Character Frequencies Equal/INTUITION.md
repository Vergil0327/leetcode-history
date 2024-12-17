# Intuition

3 operations:

1. freq[ch] += 1
2. freq[ch] -= 1
3. freq[ch]-1, freq[ch+1]+1

目標`freq[a...z] == constant | 0`

看題目求最小操作數, 首先想到binary search, 但由於沒有單調性質, 也就是操作x次不行不代表操作x+1次也不行
所以再來想到的就是dynamic programming (dp)

首先先依著題目要求的試著定義看看: `dp[i]: the minimum number of operations required to make s[:i] good`
而且我們也知道我們的狀態變化僅能透過上面三種操作
所以再來就看對於i-th character來說, 能否看出什麼狀態變化的規則

由於最後的constant可能是任何數, 所以可能也要加進到狀態裡: `dp[i][target]: the minimum number of operations required to make s[:i] good with "target" frequency`

但逐個從0到第i個看好像不太好考慮, 既然我們都假定目標要滿足`target`個了, 我們應該遍歷**a-z**來試著讓每個字母都是`0`或是`target`個才對
因此定義:

```
def dfs(ch, target): the minimum number of operations required to make frequency of `ch` equal target or 0
```

那麼狀態轉移為:

首先base case: `if ch == 26: return 0` 這邊我們遍歷**a-z**的方式改為遍歷**0-25**

```py
freq = [0] * 26
for ch in s:
    freq[ord(ch) - ord("a")] += 1

def dfs(ch, target):
    if ch == 26: return 0

    cnt = freq[ch]

    if cnt > target:
        dfs(ch+1, target) + (cnt-target) # op.2: deletion
    elif cnt < target:
        dfs(ch+1, target) + (target-cnt) # op.1: insertion
        
        changed =  ??? # op.3
```

上面會看到op.3還需要前一個`ch`的資訊, 如果前個`ch-1`刪除了**x**個, 那麼`ch`就可以透過op.3增加`x`個
因此我們在狀態上再額外加上這個資訊:

```py  
@cache
def dfs(ch, target, deletion):
    if ch == 26: return 0

    cnt = freq[ch]
    
    if cnt > target:
        delete = cnt-target
        return dfs(ch+1, target, delete) + delete # op.2: deletion
    elif cnt < target:
        # op.1: insertion
        res = dfs(ch+1, target, 0) + need

        # op.2: delete to 0
        res = min(res, dfs(ch+1, target, cnt) + cnt)
        
        # op.3: change ch-1 deletion to ch
        need = target-cnt
        res = min(res, dfs(ch+1, target, 0) + (need-min(deletion, need)))
        return res
    else: # already equals target
        return dfs(ch+1, target, 0)
```

那再來就是遍歷所有可能target constant找出最小操作數即可

time: O(max(frequency) * 26)
space: O(max(frequency) * 26 * max(frequency))
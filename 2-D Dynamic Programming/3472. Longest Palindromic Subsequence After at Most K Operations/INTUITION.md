# Intuition

first thought: use dfs (top-down dp) to explre every possible transformation

define: `dfs(l, r, k): the longest palindromic subsequence of s[l:r] that can be obtained after performing at most k operations`

then, we got state transition:

1. skip s[l]: `dfs(l+1, r, k)`
2. skip s[r]: `dfs(l, r-1, k)`

> these two states give us all possible combination (s[l], s[r]) pair

3. match s[l] & s[r]: `dfs(l+1, r-1, k-operations) + 2`

直接用cache decorator會Memory Limit Exceeded
需額外用3-d array去記憶才行

```py
@lru_cache(None)
def dfs(l, r, k):
    if l==r: return 1
    if l > r: return 0

    # skip s[l]
    res = dfs(l+1, r, k)
    
    # skip s[r]
    res = max(res, dfs(l, r-1, k))

    # two skip above make all possible (s[l],s[r]) combinations
    # then, we try match them under k operations
    # match s[l], s[r]

    x = ord(s[l])-ord("a")
    y = ord(s[r])-ord("a")
    # ex. x=a, y=z, two directions:
    # 0-25 = -25 = 1
    # 25-0 = 25
    op1 = x-y if x-y >= 0 else x-y+26
    op2 = y-x if y-x >= 0 else y-x+26
    if k >= min(op1, op2):
        res = max(res, dfs(l+1, r-1, k-min(op1, op2))+2)
    return res
return dfs(0, len(s)-1, k)
```
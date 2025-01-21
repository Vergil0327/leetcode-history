# Intuition

1. 兩端開始, 兩個equidistant houses必須不同顏色
2. 相鄰也必須不同顏色
3. 只有三種顏色

所以我們定義dfs(l, r, colorL, colorR): the minimum cost considering [0:l], [r:n-1] and node-{l-1} is colorL and node-{r+1} is colorR


所以我們就從兩端出發, 然後遍歷可能顏色嘗試所有組合即可

```py
def dfs(l, r, colorL, colorR):
    if l > r: return 0
    
    res = inf
    for color1 in range(3):
        if colorL == color1: continue
        for color2 in range(3):
            if color1 == color2: continue
            if colorR == color2: continue
            res = min(res, dfs(l+1, r-1, color1, color2) + cost[l][color1] + cost[r][color2])
    return res
```
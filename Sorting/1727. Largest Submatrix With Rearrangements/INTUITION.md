# Intuition

在一個0/1 matrix裡找最大矩形, 如果能聯想到`leetcode 85`的話會比較有方向
重點是在matrix裡想成histogram來求最大矩形面積

想法則是遍歷一個維度，然後再遍歷另個維度看能做什麼事
我們如果先遍歷row再遍歷col來建立histogram的話會是:
```py
hist = [0] * cols
for i in range(rows):
    for j in range(cols):
        if matrix[i][j]:
            hist[j] += 1
        else:
            hist[j] = 0
```

這樣我們就能求出histogram的每個bar的高度
例如.
```
1   1 
1 1 1 
1 1   1 1

-> hist = [3,2,0,1,1]
```

由於我們可以任意調換, 所以我們直覺肯定是依高度排序
讓高度相近的鄰接在一起來構成最大矩形
那如果我們高度由大到小排序的話 (`h = sorted(hist, reverse=True)`)
這時我們要求最大的histogram面積, 我們僅需要再遍歷一次
此時高度會遞減而寬度會遞增
- height = min(height, h[j])
- width = j+1
- where j from 0 to cols-1

```
1   1                           1       1
1 1 1     -> sort               1 1     1
1 1   1 1 -> h = [3,2,1,1,0] -> 1 1 1 1 
```

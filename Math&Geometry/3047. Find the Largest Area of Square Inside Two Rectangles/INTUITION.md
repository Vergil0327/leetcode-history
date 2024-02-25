# Intuition

找出交集區域, 我們可以用O(n^2)遍歷所有pair
然後以bottom-left來說, 我們找最右上的點`x`
以top-right來說, 我們找左下的點`y`

```py
for i in range(n):
    for j in range(i+1, n):
        (r1, c1), (r2, c2) = arr[i]
        (x1, y1), (x2, y2) = arr[j]


        x = [max(r1, x1), max(c1, y1)]
        y = [min(r2, x2), min(c2, y2)]
```
那這樣交集正方形的邊長, 就會是最短的那條邊: `side = min(y[0]-x[0], y[1]-x[1])`
由於有可能是負數(代表沒有交集), 我們取個`max(0, side)`
那這樣面積就是邊長的平方, 取全局最大即可


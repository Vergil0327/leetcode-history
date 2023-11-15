# Intuition

Great Explanation by [@HuifengGuan](https://www.youtube.com/watch?v=f8pRFDWFp54&ab_channel=HuifengGuan).

想法是利用2D的difference array將所有矩形標記起來

首先先把所有的點從grid上找出來, 並將X軸跟Y軸的點做排序
```py
rows = set()
cols = set()
for x1, y1, x2, y2 in rectangles:
    rows.add(x1)
    rows.add(x2)
    cols.add(y1)
    cols.add(y2)

rows = sorted(list(rows))
cols = sorted(list(cols))
```

再來我們要轉換一下, 將原本(x,y)座標轉換成(i,j)
然後用(rows[i], cols[j])計算2D diff array

```py
m, n = len(rows), len(cols)
X2idx = {rows[i]: i for i in range(m)}
Y2idx = {cols[i]: i for i in range(n)}
diff2D = Diff2D(m, n)
for x1, y1, x2, y2 in rectangles:
    i = X2idx[x1]
    j = Y2idx[y1]
    x = X2idx[x2]-1 # 將像素格子壓縮成點來計算面積
    y = Y2idx[y2]-1

    diff2D.set(i, j, x, y, 1)

diff2D.compute()
```

最後可以透過**diff2D.result[i][j]**是否大於0, 也就是(i,j)這個點有沒有被標記
以此來判斷有沒有被矩形覆蓋

覆蓋面積為而(i,j)這點的面積還原回去原格子(x,y)為:
```py
dx = rows[i+1]-rows[i]
dy = cols[j+1]-cols[j]
area = dx * dy
```

所以:
```py
res = 0
for i in range(m):
    for j in range(n):
        if diff2D.result[i][j] > 0:
            # 點還原成原圖的像素格子
            dx = rows[i+1]-rows[i]
            dy = cols[j+1]-cols[j]
            res = (res + dx*dy%mod)%mod
return res
```

# Other Solution

一開始其實是想到sweepline, 但該如何下手?

以example 1為例:

先從y=0開始往上掃

1. y=0:
   - x=[0,3]被矩形cover => current_x_coverage=3
2. y=1:
   - area += (1-0) * current_x_coverage = 3
   - x=[0,2], 更新current_x_coverage=2
3. y=2:
   - area += (2-1) * current_x_coverage = 2
   - x=[1,2], 更新current_x_coverage=1
4. y=3
   - area += (3-2) * current_x_coverage = 1
   - 更新current_x_coverage=0

```py
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        rows = sorted(set([x for x1, y1, x2, y2 in rectangles for x in [x1, x2]]))
        X2idx = {v: i for i, v in enumerate(rows)}
        
        sweepline = []
        for x1, y1, x2, y2 in rectangles:
            sweepline.append([y1, x1, x2, 1])  # start position in y-axis
            sweepline.append([y2, x1, x2, -1]) # end position in y-axis
        sweepline.sort()
        
        mod = 10 ** 9 + 7
        count = [0] * len(X2idx) # count[i]: the number of overlaps on the interval [x[i], x[i + 1]]
        cur_y = cur_x_sum = area = 0
        for y, x1, x2, sig in sweepline:
            area += (y - cur_y) * cur_x_sum % mod
            cur_y = y
            for i in range(X2idx[x1], X2idx[x2]):
                count[i] += sig

            cur_x_sum = sum(rows[i+1]-rows[i] for i in range(len(rows)-1) if count[i] > 0)

        return area % mod
```
# Intuition

Brute force的話, 我們對points由高到低排序
points[i]作為top-left, points[j]作為bottom-right的話
我們需要再對[points[i].x, points[j].x]這範圍內確認有沒有任何的點存在, 其中points[i].x <= points[j].x
那這樣是個O(n^3)

但如果我們遍歷過程中, 同時把x方向加入到有序容器裡的話
我們就能用binary search找出[points[i].x, points[j].x]這範圍間有沒有存在任何一個點
如果不存在任何一個點, 那就是合法矩形, `res += 1`

如此一來就能用O(nlogn + n^2logn)的時間複雜度求出解來

# Optimized

一樣先以top-left為基準排序
我們遍歷points[i]作為top-left, 然後再從bottom-left一路找回top-right找出合法bottom-left
算是以greedy的方式找合法矩形, 並用`y`紀錄舉行的下邊界避免後續找到重複

time: O(nlogn + n^2)

```py
def numberOfPairs(self, points: List[List[int]]) -> int:
    n = len(points)
    points.sort(key=lambda x: (x[0], -x[1]))
    res = 0
    for i in range(n):
        y = -inf
        for j in range(i + 1, n):
            if points[i][1] >= points[j][1] > y:
                res += 1
                y = points[j][1]
    return res
```
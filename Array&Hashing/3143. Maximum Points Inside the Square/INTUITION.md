# Intuition

能圈住points[i]的矩形邊長為: abs(max(points[i][0]), points[i][1])
由於我們不能圈住1個以上重複tag, 所以我們先對tag分類

```py
tag2points = defaultdict(list)
for pos, tag in zip(points, s):
    tag2points[tag].append(pos)
```

然後我們將點依據所需矩形邊長由小到大排序
```py
squareLength = lambda pos: max(abs(pos[0]), abs(pos[1]))
for arr in tag2points.values():
    arr.sort(key=squareLength)
```

由於我們不能圈到一個以上相同tag, 所以我們遍歷每個tag找出第二近的位置作為boundary, 然後找出全局最小
我們劃分的合法矩形只能小於這個boundary, 不然矩形內就會有重複tag

```py
boundary_len = inf
for arr in tag2points.values():
    if len(arr) > 1:
        x, y = arr[1]
        length = max(abs(x), abs(y))
        boundary_len = min(boundary_len, length)
```

那最後就看boundary內有多少個point即可
```py
res = 0
for arr in tag2points.values():
    x, y = arr[0]
    length = max(abs(x), abs(y))
    if length < boundary_len:
        res += 1
return res
```
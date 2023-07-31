# Intuition

我們要找每個points[i]被多少rectangles所包含, 所以很明顯的是我們要找出`l >= points[i].l and h >= points[i].h`.

很明顯的我們可以透過sort + binary search來達到這個目的
由於有兩個維度, 所以我們可以遍歷一個維度然後再透過binary search來找出有多少個rectangles不被points[i]所包含
這樣包含points[i]的rectangles就可以透過`len(rectangles) - bisect_left(points[i])`得知

所以我們可以遍歷h, 然後找在`points[i].h >= hi`的情況下有多少合法rectangles, 全部加總起來即為答案

由於`1 <= hi, yj <= 100`
所以首先我們要對rectangles[i].l排序, 然後以`hi`為key最多分成最多100 buckets
```py
buckets = defaultdict(list)
for l, h in rectangles:
    buckets[h].append(l)
```
再來每個bucket都要排序, 這樣我們等等才可以透過binary search來找說, 在`l`這個維度有多少合法rectangles
所以我們可以先對rectangles整體以`l`做個排序, 然在進行上一步
這樣就會依序append

所以high level來看就會是:
```py
rectangles.sort()
buckets = defaultdict(list)
for l, h in rectangles:
    buckets[h].append(l)

res = []
for point in points:
    res.append(count(point))
return res
```

那麼helper function `count`就是遍歷h找出合法的h下有多少合法的l
```py
def count(point):
    res = 0
    for h, rectangles in buckets.items():
        if h >= point[1]:
            i = bisect.bisect_left(rectangles, point[0])
            res += len(rectangles) - i
    return res
```
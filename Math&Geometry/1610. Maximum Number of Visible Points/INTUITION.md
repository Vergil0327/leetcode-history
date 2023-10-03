# Intuition

視線範圍:
d = 0-360
範圍[d, d+angle]

points = [x,y] => 轉換成極座標 => points = [x,y] = [r*cos(theta), r*sin(theta)] where r is radius theta is radian

因此可以將:
1. points以location為原點對角度theta排序, 這樣順序就會是由小到大逆時鐘排序, 如此一來就會是連續的array, 比較好判斷我們視野的涵蓋區域

2. 再來就只要維護一個sliding window [d, d+angle] 找出視野範圍內能有最多點的區間即可
   - 注意Edge Case: 當`poinsts[i] == location`時, 我們**永遠看得到**並且必須從原來points裡filter掉, 不然計算角度時會出問題

3. 這樣最終答案會是: `sliding_window.length + 與location重疊的點的個數`

由於我們只關注points[i]的角度(弧度), 所以先將全部座標作轉換, 轉換成弧度

**如何計算弧度(radian)?**
```py
# 以(0,0)為原點
x, y = points[i]
radian = math.atan2(y,x)
```

**座標轉換成弧度**
```py
extra = 0
angles = []
x0, y0 = location
for x, y in points:
    if x == x0 and y == y0:
        extra += 1
    else:
        angles.append(math.atan2(y-y0, x-x0))
angles.sort()
```

再來注意, 由於第四象限與第一象限相連, 為了解決橫跨第四與第一象限的視野問題
我們將額外重複一次points並將每個點的角度加上2*pi弧度 (亦即加上360度)
這樣在處理這段時兩點所構成的視野差值就不會出錯

> ex. 如果A點落在第一象限, 角度為40度 = 400度
> B點落在第四象限, 角度310度
> 那兩點間的夾角差應為**90度**而非**-270度**

```py
angles = angles + [x + 2.0 * math.pi for x in angles]
```

最後就是單純的sliding window, 別忘了將angle也轉換成弧度
```py
angle = (angle/360) * 2*math.pi
n = len(angles)
res = l = r = 0
while r < n:
    right = angles[r]
    r += 1
    while l < r and right-angles[l] > angle:
        l += 1
    res = max(res, r-l)
return res + extra
```
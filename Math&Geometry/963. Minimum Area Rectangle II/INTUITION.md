# Intuition

重點是找出目標形狀的特徵值
當我們遍歷一個點時, 直覺可以想到找出另一個點作為對角線
這時中心位置就是(x1+x2)/2, (y1+y2)/2, 然後兩點長度為sqrt((x1-x2)**2 + (y1-y2)**2)
那任意矩形的兩對角線長度會是相同且交集點也會在相同的中心位置
所以我們可以用個hashmap來以(中心位置, 對角線長度)作為key來紀錄任意pair

如此一來就能用O(n^3)來找出矩形的四個點
```py
iterate point1 in points:
    iterate point2 in points:
        key = (center, dist)
        iterate (point3, point4) in hashmap
             calculate area of rectangle which constructed from point1, point2, point3, point4
```
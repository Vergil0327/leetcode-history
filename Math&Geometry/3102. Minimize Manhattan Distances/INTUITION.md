# Intuition

首先先想關鍵的一步, 該怎麼從一堆點中搜索出maximum Manhattan distance?

brute force:
```py
for i in range(m):
    for j in range(i+1, m):
        res = max(res, abs(arr[j][0]-arr[i][0]) + abs(arr[j][1]-arr[i][1]))
                            +                           +
                            +                           -
                            -                           +
                            -                           -
```

當時卡在這步過不去, 後來才發現這是一個經典問題
首先看到abs, 我們先試著拆開他, 可拆出四種可能

```
abs(x1 - x2) + abs(y1 - y2) = (x1 - x2) + (y1 - y2)
                            = -(x1 - x2) + (y1 - y2)
                            = (x1 - x2) + (-(y1 - y2))
                            = -(x1 - x2) + (-(y1 - y2))
```

但因為我們最終要求的是: `max(abs(x1 - x2) + abs(y1 - y2))`
所以:

```
max(abs(x1 - x2) + abs(y1 - y2)) = max(
                                     x1 - x2 + y1 - y2,
                                    -x1 + x2 + y1 - y2,
                                     x1 - x2 - y1 + y2,
                                    -x1 + x2 - y1 + y2,
                                 )
                                 = max(
                                    (x1+y1) - (x2+y2),
                                    (-x1+y1) - (-x2+y2) = -(x1-y1) - (-(x2-y2))
                                    (x1-y1) - (x2-y2),
                                    (-x1-y1) - (-x2-y2) = -(x1+y1) - (-(x2+y2)) = -(x1+y1) - (-(x2+y2))
                                 )
                                 = max(sum1 - sum2, diff1 - diff2)
```

那既然最終其實是找max(sum1 - sum2, diff1 - diff2)
那其實我們可以遍歷(x, y)找出: maxSum, minSum, maxDiff, minDiff

那麼: max Manhattan distance = max(abs(x1 - x2) + abs(y1 - y2)) = max(maxSum - minSum, maxDiff - minDiff)

```py
def findMaxManhattan(arr, skip=-1):
    maxSum = maxDiff = -inf
    minSum = minDiff = inf
    for i in range(len(arr)):
        if i == skip: continue

        s = sum(arr[i])
        d = arr[i][0]-arr[i][1]
        maxSum = max(maxSum, s)
        minSum = min(minSum, s)
        maxDiff = max(maxDiff, d)
        minDiff = min(minDiff, d)
    return max(maxSum-minSum, maxDiff - minDiff)
```

那麼O(n^2) brute force:

```py
n = len(points)
res = inf
for skip in range(n):
    dist = findMaxManhattan(points, skip)
    res = min(res, dist)
return res
```

但根據constraint: 3 <= points.length <= 10^5, O(n^2)是會TLE的
而findMaxManhattan已經是最優解, 因此我們只能從skip這邊下手

這種跟大小有關且跟順序無關的, 可以先想一下排序有沒有幫助
然後在先不考慮skip的情況下: maxDist = findMaxManhattan(points)
這時如果要拔掉一個點使其max manhattan distance下降, 肯定是得拔掉最遠的左右兩端點其中一個
拔掉中間的點都沒用, maxDist不變

ex. points = X1 X X X X X X X X X X X X2, maxDist = |X2 - X1|

要選只能選skip X1 or X2
{X1 X X X X X X X X X X X} X2 or X1 {X X X X X X X X X X X X2}

根據max manhattan distance = max(maxSum-minSum, maxDiff - minDiff)
我們要做的是找出maxSum, minSum, maxDiff, minDiff各自所代表的點, 然後拿掉它
這樣我們僅需要四次即可找出最優的skip的點

可以用O(n)時間找出這四個點, 在findMaxManhattan裡找出max manhattan distance並在遍歷過程中紀錄maxSum, minSum, maxSum, minSum這四個點的index位置
然後看：
1. 如果maxSum-minSum等於max manhattan distance, 那就試著拿掉maxSum那點跟minSum那點試試
2. 如果maxDiff-minDiff等於max manhattan distance, 那就試著拿掉maxDiff那點跟minDiff那點試試

但也能簡單透過排序找出這四個點: O(nlogn)

```py
points.sort(key=lambda x: x[0]+x[1])
# 此時X1 = maxSum, X2 = minSum

points.sort(key=lambda x: x[0]-x[1])
# 此時X1 = maxDiff, X2 = minDiff
```


## Other Approach

遍歷每個點作為skip, 透過multiset以log(n)時間add/remove, 並以O(1)找出max manhattan distance

```c++
class Solution {
public:
    int minimumDistance(vector<vector<int>>& points) {
        multiset<int> x, y;
        for (auto p : points) {
            x.insert(p[0]-p[1]);
            y.insert(p[0]+p[1]);
        }
        int ans=1e9;
        for (auto p : points) {
            x.erase(x.find(p[0]-p[1]));
            y.erase(y.find(p[0]+p[1]));
            ans=min(ans, max(*x.rbegin()-*x.begin(), *y.rbegin()-*y.begin()));
            x.insert(p[0]-p[1]);
            y.insert(p[0]+p[1]);
        }
        return ans;
    }
};
```

```py
from sortedcontainers import SortedList
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        SUM, DIFF = SortedList(), SortedList()
        for x, y in points:
            SUM.add(x+y)
            DIFF.add(x-y)

        res = inf
        for x, y in points:
            SUM.remove(x+y)
            DIFF.remove(x-y)
            res = min(res, max(SUM[-1]-SUM[0], DIFF[-1]-DIFF[0]))
            SUM.add(x+y)
            DIFF.add(x-y)
        return res
```
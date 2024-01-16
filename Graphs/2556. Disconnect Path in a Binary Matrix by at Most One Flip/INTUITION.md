# 2 DFS

## Intuition

use floodfill technique

for first time DFS, if we can't reach (m-1, n-1), grid is already disconnected, return `True`

and let's flip the all the cell we visited to 0

then, for second time DFS, if we can reach (m-1, n-1), it means there exists another non-intersecting path, return `False`, else return `True`

## Complexity

- time complexity

$$O(M*N)$$
, since we only visited each cell once

- space complexity

$$O(1)$$

## Other Solution

1. 首先把無法抵達的點都全部翻為0
2. 再來把無法繼續往右往下走的點也都翻為0
3. 再來剩下的就是connected path，沿著左下角到右上角這條對角線來看，同條線上的點距離(0,0)都是一樣距離的. 只要有任一條對角線上只存在著一個點是可通過的，那代表只要阻斷那個點就無法抵達終點了，因此返回True，否則返回False
   - 撇除起點終點

ex. there is a grid like this:

```
XYZ
YZO
ZOM
```
任一條左下右上對角線上的點 ([X], [YY], [ZZZ], [OO], [M])，只要任一條線上能經過的點只有一個時，阻斷該點就無法抵達終點，但要撇除起點[X]跟終點[M]

```py
class Solution:
    def isPossibleToCutPath(self, A: List[List[int]]) -> bool:
        m, n = len(A), len(A[0])
        for r in range(m):
            for c in range(n):
                if r == c == 0 or A[r][c] == 0:
                    continue
                if (r == 0 or A[r - 1][c] == 0) and (c == 0 and A[r][c - 1] == 0):
                    A[r][c] = 0

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r == m - 1 and c == n - 1) or A[r][c] == 0:
                    continue
                if (r == m - 1 or A[r + 1][c] == 0) and (c == n - 1 or A[r][c + 1] == 0):
                    A[r][c] = 0

        count = Counter(r + c for r in range(m) for c in range(n) if A[r][c])
        return any(count[i] < 2 for i in range(1, n + m - 2))
```
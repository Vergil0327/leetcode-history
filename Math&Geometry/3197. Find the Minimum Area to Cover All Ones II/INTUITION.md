# Intuition

首先看到這數據量很小, **1 <= grid.length, grid[i].length <= 30**, 感覺會類似於暴力搜索
但實在沒啥想法

但這題正解的切入點是: 你要將一個矩形分成三塊, 必定是透過水平切分跟垂直切分來分出三個區域

```
vertical split:
X | O X X
O | X X O
O | O O X

X O | X X
O X | X O
O O | O X

X O X | X
O X X | O
O O O | X
      ->

horizontal split:
X O X X
- - - - 
O X X O
O O O X

X O X X
O X X O
- - - - 
O O O X
```

水平切分跟垂直切分組合起來, 將整個矩形分成三塊, 只會有六種情形

```
X | O | X X
O | X | X O
O | O | O X

X O X X
- - - - 
O X X O
- - - -
O O O X

X | O  X X        X | O  X X
   - - - -   or   - |
O | X  X O        O | X  X O
O | O  O X        O | O  O X


X O   X X
- - - - 
O X | X O
O O | O X

X O | X X
- - - - 
O X   X O
O O   O X
```

我們就在這所有情形裡, 分別在三塊區域找出min area 加總起來
再找出全局最小min area即可

所以整體框架會是:
```py
m, n = len(grid), len(grid[0])

res = m*n
# horizontal split
for split1 in range(1, m):
    # horizontal split
    for split2 in range(split1+1, m):
        area1 = findMinRect(0, split1-1, 0, n-1) # top
        area2 = findMinRect(split1, split2-1, 0, n-1) # middle
        area3 = findMinRect(split2, m-1, 0, n-1) # bottom
        res = min(res, area1+area2+area3)

# horizontal split
for split1 in range(1, m):
    # upper vertical split
    for split2 in range(1, n):
        area1 = findMinRect(0, split1-1, 0, split2-1) # top-left
        area2 = findMinRect(0, split1-1, split2, n-1) # top-right
        area3 = findMinRect(split1, m-1, 0, n-1)
        res = min(res, area1+area2+area3)

    # lower vertical split
        area1 = findMinRect(0, split1-1, 0, n-1) # top
        area2 = findMinRect(split1, m-1, 0, split2-1) # bottom-left
        area3 = findMinRect(split1, m-1, split2, n-1) # bottom-right
        res = min(res, area1+area2+area3)

# vertical split
for split1 in range(1, n):
    # vertical split
    for split2 in range(split1+1, n):
        area1 = findMinRect(0, m-1, 0, split1-1) # left
        area2 = findMinRect(0, m-1, split1, split2-1) # mid
        area3 = findMinRect(0, m-1, split2, n-1) # right
        res = min(res, area1+area2+area3)

# vertical split
for split1 in range(1, n):
    # left horizontal split
    for split2 in range(1, m):
        area1 = findMinRect(0, split2-1, 0, split1-1) # left-top
        area2 = findMinRect(split2, m-1, 0, split1-1) # left-bottom
        area3 = findMinRect(0, m-1, split1, n-1)
        res = min(res, area1+area2+area3)

    # right horizontal split
        area1 = findMinRect(0, m-1, 0, split1-1) # left
        area2 = findMinRect(0, split2-1, split1, n-1) # right-top
        area3 = findMinRect(split2, m-1, split1, n-1) # right-bottom
        res = min(res, area1+area2+area3)
return res
```

至於helper func `findMinRect`很簡單, 給定上下左右四個邊界後
遍歷一遍找出最小矩形的四個邊界即可

```py
def findMinRect(top, down, left, right):
    l, t, r, bot = inf, inf, -1, -1
    
    for i in range(top, down+1):
        for j in range(left, right+1):
            if grid[i][j] > 0:
                l = min(l, j)
                r = max(r, j)
                t = min(t, i)
                bot = max(bot, i)
    return (r-l+1) * (bot-t+1)
```

# Optimized

基於這樣的概念, [@lee215](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/solutions/5355610/python-two-cases-split-vertical-horizontal/)給出了更簡短的表達式
透過對原矩形`grid`進行rotation, 在配合vertical split跟horizontal split
切出所有情形

```py
def minimumSum(self, grid: List[int]) -> int:
    # Problem 3195
    def minimumArea(A):
        left, top, right, bottom = inf,inf,0,0
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j]:
                    left = min(left, j)
                    top = min(top, i)
                    right = max(right, j)
                    bottom = max(bottom, i)
        return (right - left + 1) * (bottom - top + 1)

    res = inf
    for _ in range(4):
        n, m = len(grid), len(grid[0])
        for i in range(1, n):
            a1 = minimumArea(grid[:i])
            for j in range(1, m):
                a2 = minimumArea([r[:j] for r in grid[i:]])
                a3 = minimumArea([r[j:] for r in grid[i:]])
                res = min(res, a1 + a2 + a3)

            for i2 in range(i + 1, n):
                a2 = minimumArea(grid[i:i2])
                a3 = minimumArea(grid[i2:])
                res = min(res, a1 + a2 + a3)

        grid = list(zip(*grid[::-1])) # rotate
    return res
```
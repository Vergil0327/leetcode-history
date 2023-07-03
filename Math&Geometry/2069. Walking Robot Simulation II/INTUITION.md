# Intuition

一開始brute force為:

```py
class Robot:

    def __init__(self, width: int, height: int):
        m = self.m = height
        n = self.n = width
        self.robot = [0,0]
        self.dirs = {
            (0,1): "East",
            (1,0): "North",
            (0,-1): "West",
            (-1,0): "South",
        }
        self.nextDir = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.dir = (0,1)


    def step(self, num: int) -> None:
        m, n = self.m, self.n
        r, c = self.robot

        while num > 0:
            dr, dc = self.dir
            row, col = r+dr, c+dc

            # counterclockwise if hit the wall
            # E -> N -> W -> S
            while row == -1 or row == m or col == -1 or col == n:
                self.dir = self.nextDir[self.dir]
                dr, dc = self.dir
                row, col = r+dr, c+dc
            
            step = inf
            if dr != 0:
                if dr > 0:
                    step = min(num, (m-1-r))
                else:
                    step = min(num, r)
                row, col = r+step*dr, c
            else:
                if dc > 0:
                    step = min(num, n-1-c)
                else:
                    step = min(num, c)
                row, col = r, c+step*dc

            r, c = row, col
            num -= step

        self.robot = [r, c]
        
    def getPos(self) -> List[int]:
        return reversed(self.robot)
        
    def getDir(self) -> str:
        return self.dirs[tuple(self.dir)]
```
但發現一步一步走會超時

仔細觀察會發現, robot只會在border上移動
如果width, height很小, 步數很多, 那即使我們每次模擬都盡可能走到底, 還是會需要轉很多圈
所以我們應該能計算多少步是會回到原點的

如果width = n, height = m
這樣的話如果步數是`2*m+2*n-4`, 那就會轉一圈回到原地. (ps. `-4`是因為四個角落會重複計算)
所以我們可以先用`num`對`2*m+2*n-4`取餘數

**edge case**

這邊有個edge case是這個例子
["Robot","getPos","getDir","step","step","getDir","getPos"]
[[97,98],[],[],[31652],[32038],[],[]]
[null,[0,0],"East",null,null,"South",[0,0]]

當我們一開始在角落, 然後num剛好是`2*m+2*n-4`的倍數時, 我們會轉一圈回到原地
但此時的方向會是前一個逆時針的方向, ex. 原本East會變South
由於想不到比較好handle這個edge case的方式, 所以在取餘數為0後，我們模擬移動一次來讓方位更新到正確的方位
因此我們在取完餘數後，再額外加一圈讓他模擬, 以避免num==0的edge case:
```py
num %= mod
if num == 0:
    num += mod
```

# Concise Solution

Credit to [Lee215](https://leetcode.com/problems/walking-robot-simulation-ii/solutions/1576036/python-easy-and-concise-solution/)

Generate all results for every position first.

Note that,
if robot moves, its direction for [0, 0] will be South.
While it starts at [0, 0] with East

```py
class Solution(object):

    def __init__(self, w, h):
        self.i = 0
        self.pos = [[0, 0, 'South']] + [[i, 0, 'East'] for i in range(1, w)] + \
            [[w - 1, i, 'North'] for i in range(1, h)] + \
            [[i, h - 1, 'West'] for i in range(w - 2, -1, -1)] +\
            [[0, i, 'South'] for i in range(h - 2, 0, -1)]

    def move(self, x):
        self.i += x

    def getPos(self):
        return self.pos[self.i % len(self.pos)][:2]

    def getDir(self):
        return self.pos[self.i % len(self.pos)][2] if self.i else 'East'
```
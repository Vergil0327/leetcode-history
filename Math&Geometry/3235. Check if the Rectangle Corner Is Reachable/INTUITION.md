# Intuition

1. path可以走曲線
2. 3 <= X, Y <= 10^9
這樣看來, 在這平面上直接DFS或BFS模擬是肯定不行

如果用上下左右四個點來表示一個圓, 一但兩圓相交, 相當於最上到最下, 最左到最右這範圍內路徑都被擋住
所以我們遍歷每個圓然後把相交的放到同個group來看
這部分可以透過union-find來先將有相交的circles[i]放到同個group裡, 並同時更新他的四個方向邊界
然後在遍歷沒有跟其他圈相交的孤兒的四個方向邊界
我們就看每個group的四個方向邊界minX, maxX, minY, maxY有沒有涵蓋整個範圍阻礙道路

涵蓋有可能:
1. 水平方向阻礙: [0, X]
2. 垂直方向阻礙: [0, Y]
3. 包圍起點: [0, 0]
4. 包圍終點: [X, Y]

但等到全部union-find完後遍歷判斷範圍, 實在太多edge case了, 尤其找不到合適方式去處理圓圈在(0,0) (X, Y)矩形範圍外的狀況:
ex. 
- X=4, Y=4, circles=[[5,5,1]] => True
- X=3, Y=3, circles=[[2,1000,997],[1000,2,997]] => True
- X=5, Y=8, circles=[[4,7,1]] => False

實際上這題最關鍵判斷我們能不能有條有效路徑的想法為: 

沒有路徑情況:
1. 左方border跟右方border union在一起
2. 左方border跟下方border union在一起
3. 上方border跟右方border union在一起
4. 上方border跟下方border union在一起

因此我們延續union-find的想法, 我們用parent[n]跟parent[n+1]代表兩組border: (左方/上方) 跟 (右方/下方)
這兩組任一配對都會造成路徑阻擋, 所以

我們把跟左方跟上方border相接觸的circles跟parent[n] union在一起
我們把跟下方跟右方border相接觸的circles跟parent[n+1] union在一起

那這樣我們就一樣能透過union-find判斷 find(n)跟find(n+1)有沒有union在一起, 如果有, 代表border已經透過circles[i] union在一起阻斷路徑
那就不可能有路徑可以連接(0,0)跟(X,Y)了

所以首先, 我們先遍歷每個circles[i], 看有沒有:
1. 包圍住destination (X,Y)
2. 包圍住(0,0)
3. 並把跟邊界相交的circles[i]跟border union在一起
    - [circle intersection](https://paulbourke.net/geometry/circlesphere/)

最後判斷`find(n)`跟`find(n+1)`有沒有連通在一起即可知道有沒有合法路徑了

但實際上建議這題直接跳過, 計算交集的方式沒特別查根本寫不出來

詳解: [solution by @zsq007](https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/solutions/5595662/python3-passed-all-testcases-check-intersection-points)


另外個詳解可參考`@Yawn_Sean`的解答

```py
class UnionFind:
    def __init__(self, n, size=None):
        self.parent_or_size = [-1] * n if size is None else [-x for x in size]
 
    def find(self, a):
        a = self.parent_or_size[a] if self.parent_or_size[a] >= 0 else a
        acopy = a
        while self.parent_or_size[a] >= 0:
            a = self.parent_or_size[a]
        while acopy != a:
            self.parent_or_size[acopy], acopy = a, self.parent_or_size[acopy]
        return a
 
    def merge(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb: return False
        if self.parent_or_size[pa] > self.parent_or_size[pb]:
            pa, pb = pb, pa
        self.parent_or_size[pa] += self.parent_or_size[pb]
        self.parent_or_size[pb] = pa
        return True
 
    def getSize(self, a):
        return -self.parent_or_size[self.find(a)]

class Solution:
    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        n = len(circles)
        for x, y, r in circles:
            if (x - X) * (x - X) + (y - Y) * (y - Y) <= r * r:
                return False
        
        union = UnionFind(n + 2)
        
        for i in range(n):
            x1, y1, r1 = circles[i]
            for j in range(i):
                x2, y2, r2 = circles[j]
                if circles[i] == circles[j]:
                    union.merge(i, j)
                    continue
                if (r1 - r2) * (r1 - r2) <= (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) <= (r1 + r2) * (r1 + r2):
                    dx = x2 - x1
                    dy = y2 - y1
                    t = math.atan2(dy, dx)
                    dis = dx * dx + dy * dy
                    a = math.acos((r1 * r1 - r2 * r2 + dis) / 2 / r1 / math.sqrt(dis))
                    x3, y3 = x1 + r1 * math.cos(t + a), y1 + r1 * math.sin(t + a)
                    x4, y4 = x1 + r1 * math.cos(t - a), y1 + r1 * math.sin(t - a)
                    if 0 <= x3 <= X and 0 <= y3 <= Y:
                        union.merge(i, j)
                    elif 0 <= x4 <= X and 0 <= y4 <= Y:
                        union.merge(i, j)
        
        for i in range(n):
            x, y, r = circles[i]
            # (0, 0), (0, y)
            if abs(x) <= r and (0 <= y - (r * r - x * x) ** 0.5 <= Y or 0 <= y + (r * r - x * x) ** 0.5 <= Y):
                union.merge(i, n)
            # (0, y), (x, y)
            elif abs(y - Y) <= r and (0 <= x - (r * r - (y - Y) * (y - Y)) ** 0.5 <= X or 0 <= x + (r * r - (y - Y) * (y - Y)) ** 0.5 <= X):
                union.merge(i, n)
            # (0, 0), (x, 0)
            if abs(y) <= r and (0 <= x - (r * r - y * y) ** 0.5 <= X or 0 <= x + (r * r - y * y) ** 0.5 <= X):
                union.merge(i, n + 1)
            # (x, 0), (x, y)
            elif abs(x - X) <= r and (0 <= y - (r * r - (x - X) * (x - X)) ** 0.5 <= Y or 0 <= y + (r * r - (x - X) * (x - X)) ** 0.5 <= Y):
                union.merge(i, n + 1)
        return union.merge(n, n + 1)

```
# 1st try - Normal BFS: TLE
class Solution_TLE:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0)])
        visited = set([0, 0])

        step = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == m-1 and j == n-1:
                    return step + 1

                for k in range(j+1, min(n, grid[i][j]+j+1)):
                    if (i,k) in visited: continue
                    visited.add((i, k))
                    queue.append((i, k))
                for k in range(i+1, min(m, grid[i][j]+i+1)):
                    if (k, j) in visited: continue
                    visited.add((k, j))
                    queue.append((k, j))
            step += 1
        return -1

# 2nd try - Hashset BFS: TLE
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 1)])

        rowSet, colSet = [set() for _ in range(m)], [set() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rowSet[i].add(j)
                colSet[j].add(i)

        while queue:
            for _ in range(len(queue)):
                i, j, step = queue.popleft()
                if i == m-1 and j == n-1:
                    return step

                tmp = rowSet[i].copy()
                for k in tmp:
                    if k <= j or k > grid[i][j]+j or k >= n: continue
                    rowSet[i].remove(k)
                    queue.append((i, k, step+1))

                tmp = colSet[j].copy()
                for k in tmp:
                    if k <= i or k > grid[i][j]+i or k >= m: continue
                    colSet[j].remove(k)
                    queue.append((k, j, step+1))
        return -1

# 3rd try SortedList BFS: TLE
from sortedcontainers import SortedList

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque([(0, 0, 1)])

        rowSL, colSL = [SortedList() for _ in range(m)], [SortedList() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rowSL[i].add(j)
                colSL[j].add(i)

        while queue:
            for _ in range(len(queue)):
                i, j, step = queue.popleft()
                if i == m-1 and j == n-1:
                    return step

                start = rowSL[i].bisect_right(j)
                end = rowSL[i].bisect_right(grid[i][j]+j)
                removeList = []
                for k in range(start, end):
                    queue.append((i, rowSL[i][k], step+1))
                    removeList.append(rowSL[i][k])
                for num in removeList:
                    rowSL[i].remove(num)

                start = colSL[j].bisect_right(i)
                end = colSL[j].bisect_right(grid[i][j]+i)
                removeList = []
                for k in range(start, end):
                    queue.append((colSL[j][k], j, step+1))
                    removeList.append(colSL[j][k])
                for num in removeList:
                    colSL[j].remove(num)
        return -1

# Optimized Hashset BFS - Accepted
from sortedcontainers import SortedList

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        rowSL, colSL = [SortedList() for _ in range(m)], [SortedList() for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rowSL[i].add(j)
                colSL[j].add(i)

        queue = deque([(0, 0, 1)])
        rowSL[0].remove(0)
        colSL[0].remove(0)
        while queue:
            for _ in range(len(queue)):
                i, j, step = queue.popleft()
                if i == m-1 and j == n-1:
                    return step

                start = rowSL[i].bisect_right(j)
                end = rowSL[i].bisect_right(grid[i][j]+j)
                removeList = []
                for k in range(start, end):
                    queue.append((i, rowSL[i][k], step+1))
                    removeList.append(rowSL[i][k])
                for k in removeList:
                    rowSL[i].remove(k)
                    colSL[k].remove(i)

                start = colSL[j].bisect_right(i)
                end = colSL[j].bisect_right(grid[i][j]+i)
                removeList = []
                for k in range(start, end):
                    queue.append((colSL[j][k], j, step+1))
                    removeList.append(colSL[j][k])
                for k in removeList:
                    colSL[j].remove(k)
                    rowSL[k].remove(j)
        return -1

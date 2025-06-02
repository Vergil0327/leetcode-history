from collections import defaultdict, deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        total_litter = sum(row.count('L') for row in classroom)
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def BFS(x, y):
            queue = deque([(x, y, energy, 0, 0)])  # (row, col, energy, state, step)

            visited = defaultdict(lambda: -1)
            visited[(x, y, 0)] = energy

            while queue:
                for _ in range(len(queue)):
                    x, y, egy, state, step = queue.popleft()
                    
                    if classroom[x][y] == 'L':
                        state |= 1 << (x*n+y)
                    elif classroom[x][y] == 'R':
                        egy = energy

                    count = state.bit_count()
                    if count == total_litter:
                        return step
                    
                    for dx, dy in dirs:
                        row, col = x+dx, y+dy
                        if row<0 or row>=m or col<0 or col>=n or classroom[row][col] == 'X' or egy <= 0:
                            continue
                        if visited[(row, col, state)] >= egy-1: continue
                        visited[(row, col, state)] = egy - 1
                        
                        queue.append([row, col, egy-1, state, step+1])
            return -1

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    return BFS(i, j)

        return -1
import heapq
from typing import List
from collections import deque

# Dijkstra
class Solution:
    def maximumMinimumPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        queue = [(-matrix[0][0], 0, 0)]
        visited = set([(0, 0)])
        dirs = [[0,1], [0,-1], [1,0], [-1,0]]
        res = float("inf")
        while queue:
            score, r, c = heapq.heappop(queue)
            res = min(res, -score)

            if r == ROWS-1 and c == COLS-1:
                break

            for dr, dc in dirs:
                row, col = r+dr, c+dc
                if row < 0 or row >= ROWS or col < 0 or col >= COLS: continue
                if (row, col) in visited: continue
                visited.add((row, col))
                heapq.heappush(queue, (-matrix[row][col], row, col))

        return res

# Binary Search
class BinarySearchSolution:
    def maximumMinimumPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        def existPath(score):
            queue = deque([(0, 0)])
            visited = set([(0, 0)])
            dirs = [[0,1], [0,-1], [1,0], [-1,0]]
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if r == ROWS-1 and c == COLS-1: return True

                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        if row < 0 or row >= ROWS or col < 0 or col >= COLS: continue
                        if matrix[row][col] < score: continue
                        if (row, col) in visited: continue
                        visited.add((row, col))
                        queue.append((row, col))

            return False
        
        l, r = 0, 0
        for row in matrix:
            for score in row:
                r = max(r, score)

        while l < r:
            mid = r - (r-l)//2
            if existPath(mid):
                l = mid
            else:
                r = mid-1
        return l
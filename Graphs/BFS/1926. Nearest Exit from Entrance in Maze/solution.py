# BFS
# time: O(E+V) + O(4*mn + mn ) = O(mn)
# space: O(mn)
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        visited = set([tuple(entrance)])
        for row in range(m):
            for col in range(n):
                if maze[row][col] == "+":
                    visited.add((row, col))

        queue = deque([tuple(entrance)])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        steps = 0
        while queue:
            sz = len(queue)
            for _ in range(sz):
                row, col = queue.popleft()

                if ((row == 0 or row == m-1) or (col == 0 or col == n-1)) and (row, col) != tuple(entrance):
                    return steps

                for dr, dc in dirs:
                    r, c = row + dr, col + dc
                    rowInBounds = r>=0 and r<m
                    colInBounds = c>=0 and c<n
                    if not (rowInBounds and colInBounds):
                        continue
                    if (r, c) not in visited:
                        visited.add((r, c))
                        queue.append((r, c))
            steps += 1
        return -1
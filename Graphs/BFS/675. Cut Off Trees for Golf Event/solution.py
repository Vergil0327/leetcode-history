# TLE for python
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        minHeap = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    heapq.heappush(minHeap, forest[i][j])
        
        queue = deque([(0,0)])
        steps = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while minHeap:
            # cut from smallest to tallest
            target = heapq.heappop(minHeap)

            # BFS for shortest path
            visited = set()
            cut = False
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()

                    if (r,c) in visited: continue
                    visited.add((r,c))

                    if forest[r][c] == target:
                        queue = deque([(r, c)])
                        cut = True
                        break

                    for dr, dc in dirs:
                        row, col = r+dr, c+dc
                        if row < 0 or row >= m or col < 0 or col >= n: continue
                        if forest[row][col] == 0: continue
                        if (row, col) in visited: continue
                        queue.append((row, col))
                if cut:
                    if not minHeap: return steps
                    break
                steps += 1
        return -1

# https://leetcode.com/problems/cut-off-trees-for-golf-event/solutions/107396/python-solution-based-on-wufangjie-s-hadlock-s-algorithm/
class Solution:
    def cutOffTree(self, forest):

        # Add sentinels (a border of zeros) so we don't need index-checks later on.
        forest.append([0] * len(forest[0]))
        for row in forest:
            row.append(0)

        # Find the trees.
        trees = [(height, i, j)
                for i, row in enumerate(forest)
                for j, height in enumerate(row)
                if height > 1]

        # Can we reach every tree? If not, return -1 right away.
        queue = [(0, 0)]
        reached = set()
        for i, j in queue:
            if (i, j) not in reached and forest[i][j]:
                reached.add((i, j))
                queue += (i+1, j), (i-1, j), (i, j+1), (i, j-1)
        if not all((i, j) in reached for (_, i, j) in trees):
            return -1

        # Distance from (i, j) to (I, J).
        def distance(i, j, I, J):
            now, soon = [(i, j)], []
            expanded = set()
            manhattan = abs(i - I) + abs(j - J)
            detours = 0
            while True:
                if not now:
                    now, soon = soon, []
                    detours += 1
                i, j = now.pop()
                if (i, j) == (I, J):
                    return manhattan + 2 * detours
                if (i, j) not in expanded:
                    expanded.add((i, j))
                    for i, j, closer in (i+1, j, i < I), (i-1, j, i > I), (i, j+1, j < J), (i, j-1, j > J):
                        if forest[i][j]:
                            (now if closer else soon).append((i, j))

        # Sum the distances from one tree to the next (sorted by height).
        trees.sort()
        return sum(distance(i, j, I, J) for (_, i, j), (_, I, J) in zip([(0, 0, 0)] + trees, trees))
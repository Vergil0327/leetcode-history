# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
since we want to find minimum steps to final destination, we can use **BFS** to explore this board.

# Complexity
- Time complexity:
$$O(V+E) = O(n^2 + 6n^2)$$

- Space complexity:
$$O(n^2)$$

# Other Solution

Dijkstra:

time: $O(n^2 * logn)$
space: $O(n^2)$

```
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None] * (n**2 + 1)
        label = 1
        columns = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for column in columns:
                cells[label] = (row, column)
                label += 1
            columns.reverse()
        dist = [-1] * (n * n + 1)
        dist[1] = 0
        q = [(0, 1)]
        while q:
            d, curr = heapq.heappop(q)
            if d != dist[curr]:
                continue
            for next in range(curr + 1, min(curr + 6, n**2) + 1):
                row, column = cells[next]
                destination = (board[row][column] if board[row][column] != -1
                               else next)
                if dist[destination] == -1 or dist[curr] + 1 < dist[destination]:
                    dist[destination] = dist[curr] + 1
                    heapq.heappush(q, (dist[destination], destination))
        return dist[n * n]
```
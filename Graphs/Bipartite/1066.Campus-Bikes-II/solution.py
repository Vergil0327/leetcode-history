from typing import List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m, n = len(bikes), len(workers)
        
        dist = [[-1]*n for _ in range(m)]
        for i in range(m):
            x, y = bikes[i]
            for j in range(n):
                a, b = workers[j]
                dist[i][j] = abs(x-a) + abs(y-b)

        tot = 1<<m
        dp = [float("inf")] * tot
        dp[0] = 0

        res = float("inf")
        for j in range(1, n+1): # j-th worker worker
            state = (1<<j)-1
            
            # iterate all the m-bit state where there are j 1-bits
            while state < tot:
                for i in range(m):
                    if (state>>i)&1 == 0: continue
                    dp[state] = min(dp[state], dp[state-(1<<i)]+dist[i][j-1])

                    if j == n:
                        res = min(res, dp[state])
                c = state & -state
                r = state+c
                state = (((r^state)>>2)//c) | r

        return res
    
import heapq
class Solution2:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        m, n = len(workers), len(bikes)

        dist = [[0]*n for _ in range(m)]
        for i, (x1, y1) in enumerate(workers):
            for j, (x2, y2) in enumerate(bikes):
                dist[i][j] = abs(x1 - x2) + abs(y1 - y2)

        pq = [[0,0]] # distance sum, state
        visited = set()
        while pq:
            distance, state = heapq.heappop(pq)
            if state in visited: continue
            visited.add(state)

            i = state.bit_count()
            if i == m: return distance

            for j in range(n):
                if (state>>j)&1: continue
                nxt = state | (1<<j)
                if nxt not in visited:
                    heapq.heappush(pq, [distance + dist[i][j], nxt])

        return 0
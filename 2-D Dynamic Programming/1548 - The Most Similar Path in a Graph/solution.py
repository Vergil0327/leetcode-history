from typing import List
from collections import defaultdict

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        m = len(targetPath)
        
        # dp[i][target] = dp[i-1][city] + (1 if target != targetPath[i] else 0) where city can reach target
        dp = [[float('inf')]*n for _ in range(m)]

        for i in range(n):
            dp[0][i] = 1 if names[i] != targetPath[0] else 0

        prev = [[-1]*n for _ in range(m)]
        for i in range(1, m):
            for target in range(n):
                for city in graph[target]:
                    dist = dp[i-1][city] + (1 if names[target] != targetPath[i] else 0)
                    if dist < dp[i][target]:
                        dp[i][target] = dist
                        prev[i][target] = city

        dist = float('inf')
        city = -1
        for i in range(n):
            if dp[m-1][i] < dist:
                dist = dp[m-1][i]
                city = i

        res = []
        for i in range(m-1, -1, -1):
            res.append(city)
            city = prev[i][city]
            
        return list(reversed(res))
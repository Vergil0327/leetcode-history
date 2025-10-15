from collections import Counter
from math import isqrt

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        keys = []
        for num in nums:
            remain_factors = []
            for i in range(2, isqrt(num)+1):
                if num%i == 0:
                    cnt = 0
                    while num%i == 0:
                        cnt += 1
                        num //= i
                    if cnt%2:
                        remain_factors.append(i)
            if num > 1:
                remain_factors.append(num)
            keys.append(tuple(remain_factors))
        
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.res = 0
        visited = Counter()
        def dfs(node, prev):
            ti = visited[keys[node]]
            if node > 0:
                self.res += ti

            visited[keys[node]] += 1
            for nxt in graph[node]:
                if nxt == prev: continue
                dfs(nxt, node)
            visited[keys[node]] -= 1

        dfs(0, 0)
        return self.res
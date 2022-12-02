from collections import defaultdict
import heapq
from typing import List

# Prim
class SolutionPrim:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, cost in pipes:
            graph[u].append([cost, v])
            graph[v].append([cost, u])

        # add dummy node [0,0]
        # turn wells into weighted edge from 0 to (idx+1)
        for idx, cost in enumerate(wells):
            house = idx+1
            graph[0].append([cost, house])

        minH = [[0, 0]] # [cost, house], where house from 0 to n
        visited = set()
        totalCost = 0
        while minH:
            cost, house = heapq.heappop(minH)
            if house not in visited:
                totalCost += cost
                visited.add(house)

                for neiCost, nei in graph[house]:
                    if nei not in visited:
                        heapq.heappush(minH, [neiCost, nei])
        return totalCost

# Kruskal
class SolutionKruskal:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        parent = [i for i in range(n+1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py: return False
            if px < py:
                parent[py] = px
            else:
                parent[px] = py
            return True

        for i, cost in enumerate(wells):
            pipes.append([0, i+1, cost])

        pipes.sort(key=lambda x:x[2])
        totalCost = 0
        for u, v, cost in pipes:
            if union(u, v):
                totalCost += cost
        
        return totalCost

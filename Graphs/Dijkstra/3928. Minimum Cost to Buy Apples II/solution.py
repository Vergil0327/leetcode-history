import heapq
from math import inf

class Solution:
    """
    The Breakthrough: Multi-Source Dijkstra
    The most efficient way to solve this is to realize that we can calculate the "forward" and "return" distances independently using Dijkstra's algorithm.

    1. Calculate All-Pairs Forward Distances: Since $n \le 1000$, we can run Dijkstra $n$ times (or use Floyd-Warshall, though Dijkstra is faster here) to find $D_{forward}(i, j)$ for all pairs.
    2. Reverse the Problem for Return: We need to find the minimum of $D_{forward}(i, j) + \text{Price}(j) + D_{return}(j, i)$.
    3. Multi-Source Dijkstra: Instead of calculating return paths for every $i$, we can start a single Dijkstra process where the initial state is every shop $j$ already has an apple.
        - The "starting cost" at each shop $j$ is $D_{forward}(i, j) + \text{Price}(j)$.
        - But wait, $D_{forward}(i, j)$ depends on the starting shop $i$. This is still $O(n^2)$.

    Actually, we can simplify further:
    The total cost is $D_{empty}(i, j) + \text{Price}(j) + D_{apple}(j, i)$.
    Because $n$ is relatively small (1000), and the number of roads is small (2000), $O(n \cdot (E \log V))$ is acceptable.

    The Optimized Approach

    1. Run Dijkstra once for each node $i$ to find the shortest "empty" distances to all other nodes $j$. Store this in a 2D array dist_empty[i][j].
    2. For each shop $i$, the "cost to have an apple at shop $j$ and be ready to return to $i$" is $f(i, j) = \text{dist\_empty}[i][j] + \text{prices}[j]$.
    3. For a fixed $i$, we want to find $\min_j (f(i, j) + \text{dist\_apple}(j, i))$.
    4. This is a standard Dijkstra. We put all $j$ into a priority queue with initial distance $f(i, j)$ and relax edges using the "taxed" weights ($cost \cdot tax$).
    """
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        graph_empty = [[] for _ in range(n)]
        graph_apple = [[] for _ in range(n)]
        
        for u, v, c, tax in roads:
            graph_empty[u].append((v, c))
            graph_empty[v].append((u, c))
            graph_apple[u].append((v, c * tax))
            graph_apple[v].append((u, c * tax))

        # 1. Precompute all-pairs shortest paths for "empty" travel
        # dist_empty[i][j] is the min cost to go from i to j without apples
        dist_empty = [[inf] * n for _ in range(n)]
        
        for start_node in range(n):
            dist_empty[start_node][start_node] = 0
            pq = [(0, start_node)]
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist_empty[start_node][u]: continue
                for v, weight in graph_empty[u]:
                    if dist_empty[start_node][v] > d + weight:
                        dist_empty[start_node][v] = d + weight
                        heapq.heappush(pq, (dist_empty[start_node][v], v))

        ans = []
        # 2. For each shop i, find the minimum total cost using multi-source Dijkstra
        for i in range(n):
            # Initial costs: min cost to get to shop j and buy apple
            # We treat all shops j as starting points for the return trip
            pq = []
            res_dist = [inf] * n
            for j in range(n):
                initial_cost = dist_empty[i][j] + prices[j]
                res_dist[j] = initial_cost
                heapq.heappush(pq, (initial_cost, j))
            
            # Dijkstra to find the min cost to return to shop i
            min_total = prices[i] # Default: buy locally
            while pq:
                d, u = heapq.heappop(pq)
                if d > res_dist[u]: continue
                if u == i:
                    min_total = d
                    break
                
                for v, weight in graph_apple[u]:
                    if res_dist[v] > d + weight:
                        res_dist[v] = d + weight
                        heapq.heappush(pq, (res_dist[v], v))
            ans.append(min_total)
            
        return ans
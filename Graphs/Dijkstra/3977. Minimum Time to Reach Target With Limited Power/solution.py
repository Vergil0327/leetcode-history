import heapq

class Solution:
    """
    由於初始電量 $\le 1000$，我們可以將狀態定義為 dist[node][power]，代表以恰好剩餘 power 的電量到達 node 所需的最短時間。
    
    在優先佇列中，我們儲存的元組為：(current_time, -remaining_power, node)。
    - 優先比較 time（由小到大）。
    - 若時間相同，比較 -power（由小到大，等同於電量由大到小）。
    
    在這題中，以較長的時間換取更多的電量到達同一個節點，在後續的路徑中可能是完全合法且更優的。因此，Dijkstra 的狀態不能只有 node，必須是二維的 (node, remaining_power)。
    由於這樣的排序設計，當我們第一次從 PQ 中彈出 target 節點時，它所攜帶的時間與電量就絕對是全域最優解，可以直接回傳！
    """
    def minTimeMaxPower(self, n: int, edges: list[list[int]], power: int, cost: list[int], source: int, target: int) -> list[int]:
        # 1. 建立鄰接表
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append((v, t))
            
        # 2. 初始化 2D 距離表：dist[node][remaining_power]
        # 電量的有效範圍是 0 到 power
        dist = [[float('inf')] * (power + 1) for _ in range(n)]
        dist[source][power] = 0
        
        # 優先佇列元素: (當前時間 time, 負的剩餘電量 -power, 當前節點 node)
        # 這樣寫可以確保 time 小的優先；time 相同時，真實 power 大的優先
        pq = [(0, -power, source)]
        
        while pq:
            t, neg_p, u = heapq.heappop(pq)
            p = -neg_p
            
            # 💥 終點直通防線：
            # 因為 PQ 的排序特性，第一次抓到 target 的狀態必定是「時間最短且電量最大」
            if u == target:
                return [t, p]
                
            # 剪枝：如果當前時間已經大於記錄的最短時間，直接跳過
            if t > dist[u][p]:
                continue
                
            # 檢查是否能夠離開當前節點 u（剩餘電量必須大於等於該節點的發射成本）
            if p < cost[u]:
                continue
                
            next_p = p - cost[u]
            
            # 探索鄰居
            for v, weight in graph[u]:
                next_t = t + weight
                
                # 鬆弛操作 (Relaxation)
                if next_t < dist[v][next_p]:
                    dist[v][next_p] = next_t
                    heapq.heappush(pq, (next_t, -next_p, v))
                    
        return [-1, -1]
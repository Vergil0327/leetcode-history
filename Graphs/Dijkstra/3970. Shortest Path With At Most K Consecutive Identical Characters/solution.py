import heapq

"""
我們可以將狀態定義為 dist[node][consecutive]，代表到達 node 且當前字元已連續出現 consecutive 次的最短路徑權重。
因為 $k \le 50$，所以每個節點最多隻有 $50$ 種狀態，總狀態數為 $N \times K \approx 2.5 \times 10^6$，完全可以在時間與空間限制內用標準 Dijkstra 輾過去。
"""
class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        # 1. 建立鄰接表
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            
        # 2. 初始化 Dijkstra 距離表：dist[node][consecutive]
        # consecutive 的範圍是 1 到 k
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        
        # 起點 0：連續計數為 1，距離為 0
        dist[0][1] = 0
        
        # 優先佇列元素: (當前總權重 weight, 當前節點 node, 當前字元連續次數 consecutive)
        pq = [(0, 0, 1)]
        
        while pq:
            wei, node, consecutive = heapq.heappop(pq)
            
            # 如果走到終點，因為 Dijkstra 的貪心特性，這一定是最短合法路徑
            if node == n - 1:
                return wei
                
            # 剪枝：如果當前彈出的權重已經大於記錄的最短距離，直接跳過
            if wei > dist[node][consecutive]:
                continue
                
            # 遍歷鄰居
            for nxt, w in graph[node]:
                # 根據下一個節點的字元與目前節點是否相同，決定新的連續計數
                if labels[nxt] == labels[node]:
                    nxt_consecutive = consecutive + 1
                else:
                    nxt_consecutive = 1
                    
                # 💥 核心防線：如果超過上限 k，此路不通，直接放棄該分支
                if nxt_consecutive > k:
                    continue
                    
                # 鬆弛操作 (Relaxation)
                if wei + w < dist[nxt][nxt_consecutive]:
                    dist[nxt][nxt_consecutive] = wei + w
                    heapq.heappush(pq, (wei + w, nxt, nxt_consecutive))
                    
        return -1
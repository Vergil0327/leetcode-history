"""
直覺想到利用binary search去猜threshold, 並用dijkstra判斷是否可以到達
"""
import heapq
class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        graph = [[]*n for _ in range(n)]

        max_threshold = 0
        for u, v, w in edges:
            max_threshold = max(max_threshold, w)
            graph[u].append([v, w])
            graph[v].append([u, w])

        def check(threshold):
            minHeap = [[0, source]] # step, threshold (should <= k), node
            visited = set()
            while len(minHeap) > 0:
                count, node = heapq.heappop(minHeap)
                if count > k: continue
                if node == target: return True
                if (count, node) in visited: continue
                visited.add((count, node))

                for nxt, w in graph[node]:
                    if (count + int(w > threshold), nxt) in visited: continue
                    heapq.heappush(minHeap, [count + int(w > threshold), nxt])
            return False

        l, r = 0, max_threshold+1
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        return -1 if l == max_threshold+1 else l

"""
Improved
"""
from collections import deque

class Solution:
    def minimumThreshold(self, n: int, edges: list[list[int]], source: int, target: int, k: int) -> int:
        if source == target:
            return 0
            
        graph = [[] for _ in range(n)]
        weights = set([0]) # Using a set of actual weights for binary search
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
            weights.add(w)

        # Sort weights to perform binary search on actual possible values
        sorted_weights = sorted(list(weights))

        def check(threshold):
            # dist[i] = minimum heavy edges to reach node i
            dist = [float('inf')] * n
            dist[source] = 0
            # 0-1 BFS using a deque
            queue = deque([source])
            
            while queue:
                curr = queue.popleft()
                
                if curr == target:
                    return dist[curr] <= k
                
                for nxt, w in graph[curr]:
                    # Cost is 0 if light (w <= threshold), 1 if heavy
                    weight = 0 if w <= threshold else 1
                    new_dist = dist[curr] + weight
                    
                    if new_dist < dist[nxt]:
                        dist[nxt] = new_dist
                        if weight == 0:
                            queue.appendleft(nxt) # Priority to light edges
                        else:
                            queue.append(nxt) # Heavy edges go to the back
            
            return dist[target] <= k

        # Binary Search on the sorted list of actual weights
        l, r = 0, len(sorted_weights) - 1
        ans = -1
        
        while l <= r:
            mid = (l + r) // 2
            if check(sorted_weights[mid]):
                ans = sorted_weights[mid]
                r = mid - 1
            else:
                l = mid + 1
                
        return ans
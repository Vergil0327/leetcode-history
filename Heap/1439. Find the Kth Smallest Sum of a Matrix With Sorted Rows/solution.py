class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])

        res = 0
        tot = sum(row[0] for row in mat)
        minHeap = [[tot, tuple([0]*m)]]
        visited = set()
        while k:
            tot, pick_idx = heapq.heappop(minHeap)
            if pick_idx in visited: continue
            visited.add(pick_idx)

            res = tot
            k -= 1

            for i in range(m):
                if pick_idx[i]+1 >= n: continue
                nxt = list(pick_idx)
                nxt[i] += 1
                key = tuple(nxt)
                if key in visited: continue
                heapq.heappush(minHeap, [tot + mat[i][nxt[i]] - mat[i][nxt[i]-1], key])
        
        return res

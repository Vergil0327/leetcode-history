class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor = [[0]*n for _ in range(m)]

        pq = []        
        for i in range(m):
            for j in range(n):
                # 2D prefix sum concept
                # prefixXOR[i][j] = prefixXOR[i-1][j]^prefixXOR[i][j-1]^prefixXOR[i-1][j-1]^matrix[i][j]
                cur = matrix[i][j]
                if j-1 >= 0:
                    cur ^= xor[i][j-1]
                if i-1 >= 0:
                    cur ^= xor[i-1][j]
                if i-1>=0 and j-1 >=0:
                    cur ^= xor[i-1][j-1]

                xor[i][j] = cur
                
                # find k-th largest by priority queue (min heap)
                heapq.heappush(pq, cur)
                if len(pq) > k:
                    heapq.heappop(pq)
        
        return pq[0]
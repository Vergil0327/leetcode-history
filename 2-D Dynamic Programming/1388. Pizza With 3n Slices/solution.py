class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        
        def house_robber(start, end, size):
            dp0 = [[0]*(size+1) for _ in range(end+1)]
            dp1 = [[0]*(size+1) for _ in range(end+1)]

            dp0[start][0] = 0
            dp1[start][1] = slices[start]

            for i in range(start+1, end+1):
                for m in range(1, min(size, i-start+1)+1):
                    dp0[i][m] = max(dp0[i-1][m], dp1[i-1][m])
                    dp1[i][m] = dp0[i-1][m-1] + slices[i]
            return max(dp0[end][size], dp1[end][size])


        return max(house_robber(0, n-2, n//3), house_robber(1, n-1, n//3))

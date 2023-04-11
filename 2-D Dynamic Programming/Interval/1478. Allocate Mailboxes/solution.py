class Solution:
    def minDistance(self, houses: List[int], K: int) -> int:
        houses.sort()

        n = len(houses)

        houses = [houses[0]] + houses # to 1-indexed
        dp = [[inf] * (K+1) for _ in range(n+1)]
        dp[0][0] = 0

        def distanceBetween(l, r):
            mid = (l+r)//2
            dist = 0

            for i in range(l, r+1):
                dist += abs(houses[i]-houses[mid])
            return dist

        for i in range(1, n+1):
            for k in range(1, min(i, K)+1):
                for j in range(i, k-1, -1):
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + distanceBetween(j, i))

        return dp[n][K]

# Optimized

class Solution:
    def minDistance(self, houses: List[int], K: int) -> int:
        houses.sort()

        n = len(houses)

        houses = [0] + houses # to 1-indexed
        dp = [[inf] * (K+1) for _ in range(n+1)]
        dp[0][0] = 0

        presum = [0] * (len(houses)+1)
        for i in range(1, len(houses)+1):
            presum[i] = presum[i-1] + houses[i-1]
        
        for i in range(1, n+1):
            for k in range(1, min(i, K)+1):
                for j in range(i, k-1, -1):
                    # dp[i][k] = min(dp[i][k], dp[j-1][k-1] + distanceBetween(j, i))
                    mid = (j+i)//2

                    distance = houses[mid]*(mid-j+1) - (presum[mid+1]-presum[j]) + (presum[i+1]-presum[mid]) - houses[mid]*(i-mid+1)

                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + distance)

        return dp[n][K]    
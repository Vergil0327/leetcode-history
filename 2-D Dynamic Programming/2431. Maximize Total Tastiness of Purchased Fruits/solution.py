from typing import List
from math import inf, floor

class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        n = len(price)

        dp = [[[-inf]*(maxCoupons+1) for _ in range(maxAmount+1)] for _ in range(n+1)]
        price = [0] + price
        tastiness = [0] + tastiness

        dp[0][0][0] = 0
        for i in range(1, n+1):
            p, t = price[i], tastiness[i]
            for j in range(maxAmount+1):
                for k in range(maxCoupons+1):
                    # don't pick
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k]) 
                    
                    # pick
                    if j-p >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-p][k]+t)
                
                    # pick with coupon
                    if j-(sp := p//2) >= 0 and k-1>=0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-sp][k-1] + t)

        return dp[n][maxAmount][maxCoupons]

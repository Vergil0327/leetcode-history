from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)

        dp = [inf] * n

        height = thickness = 0
        for i in range(n):
            height = max(height, books[i][1])
            thickness += books[i][0]
            if thickness <= shelfWidth:
                dp[i] = height
            else:
                break

        for i in range(n):
            height = thickness = 0
            for j in range(i, 0, -1):
                height = max(height, books[j][1])
                thickness += books[j][0]
                if thickness <= shelfWidth:
                    dp[i] = min(dp[i], dp[j-1] + height)
                else:
                    break

        return dp[n-1]
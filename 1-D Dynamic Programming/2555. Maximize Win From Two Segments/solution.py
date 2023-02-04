# DP + Binary Searchclass Solution:
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        n = len(prizePositions)
        dp = [0] * (n + 1) # dp[i]: the maximum number of covered prize for prizePositions[i:]
        
        res = 0
        for i in range(n - 1, -1, -1):
            j = bisect.bisect_right(prizePositions, prizePositions[i] + k)
            dist = j - i
            res = max(res, dist+dp[j]) # dist is maximum number of prize for [i:j),  dp[j] covered [j:]
            dp[i] = max(dist, dp[i + 1])
        return res

# DP + Sliding Window
class Solution:
    def maximizeWin(self, positions: List[int], k: int) -> int:
        n = len(positions)
        dp = [0] * (n+1)

        res = l = r = 0
        while r < n:
            num = positions[r]
            r += 1

            while l < r and num-positions[l] > k:
                l += 1

            dp[r] = max(dp[r-1], r-l)
            res = max(res, r-l + dp[l])
        return res
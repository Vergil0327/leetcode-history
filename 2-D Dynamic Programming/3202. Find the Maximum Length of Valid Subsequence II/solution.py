class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0]*k for _ in range(k)]

        res = 1
        for num in nums:
            x = num%k
            for m in range(k):
                prev = (m-num)%k
                dp[x][m] = max(dp[x][m], dp[prev][m]+1)
                res = max(res, dp[x][m])
        return res

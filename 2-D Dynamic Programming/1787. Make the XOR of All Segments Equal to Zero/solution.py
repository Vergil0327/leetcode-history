class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[inf]*1024 for _ in range(k)]
        totalCnt = [0] * k
        count = [[0]*1024 for _ in range(k)]

        for i in range(k):
            for j in range(i, n, k):
                totalCnt[i] += 1 # 第i個set的size
                count[i][nums[j]] += 1 # 第i個set裡有多少個nums[j]

        # base case: considering dp[0][target]
        for target in range(1024):
            dp[0][target] = totalCnt[0] - count[0][target]

        for i in range(1, k):
            minCost = inf
            x = None
            for target in range(1024):
                if dp[i-1][target] < minCost:
                    minCost = dp[i-1][target]
                    x = target

            for target in range(1024):
                v = target^x
                dp[i][target] = minCost + totalCnt[i] - count[i][v]

                for j in range(i, n, k):
                    v = nums[j]
                    dp[i][target] = min(dp[i][target], dp[i-1][v^target] + totalCnt[i] - count[i][v])
        return dp[k-1][0]

# bottom-up dp with max heap
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        # maxHeap, [max score, index]
        dp = [[-nums[0], 0]]
        
        for i in range(1, n):
            # pop out out-of-range dp state
            while i-dp[0][1] > k:
                heapq.heappop(dp)

            maxScore = -dp[0][0]
            heapq.heappush(dp, [-(maxScore+nums[i]), i])

        # find out dp[n-1]
        maxRslt = -inf
        for score, i in dp:
            if i == n-1:
                maxRslt = max(maxRslt, -score)

        return maxRslt

# bottom-up DP TLE
class Solution_TLE:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # dp[i]: maximum scores for nums[:i]
        dp = [-inf] * n
        
        # base case
        dp[0] = nums[0]

        for i in range(1, n):
            for j in range(1, k+1):
                if i-j < 0: continue
                dp[i] = max(dp[i], dp[i-j]+nums[i])

        return dp[n-1]
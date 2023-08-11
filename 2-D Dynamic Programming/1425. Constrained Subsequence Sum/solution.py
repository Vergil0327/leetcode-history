class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        dp = [-inf] * n
        window = [] # maxHeap
        for i in range(n):
            dp[i] = max(dp[i], nums[i])

            while window and window[0][1] < i-k:
                heapq.heappop(window)
            
            if window:
                dp[i] = max(dp[i], dp[i] + (-window[0][0]))

            heapq.heappush(window, [-dp[i], i])
            # for j in range(i-1, i-k-1, -1):
            #     dp[i] = max(dp[i], dp[j] + nums[i] if dp[j] != -inf else nums[i])
        return max(dp)

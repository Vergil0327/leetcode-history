class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [[-inf, -inf] for _ in range(n+1)]

        nums = [0] + nums
        for i in range(1, n+1):
            if nums[i] > dp[i-1][0]:
                dp[i][0] = nums[i]
            else:
                dp[i][0] = inf

            # delete nums[i]
            dp[i][1] = dp[i-1][0]
            # preserve nums[i]
            if nums[i] > dp[i-1][1]:
                dp[i][1] = min(dp[i][1], nums[i])
                
            if dp[i][1] == inf: return False

        return any(num != inf for num in dp[n])
    
# LIS Solution
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        LIS = []

        for i in range(n):
            j = bisect.bisect_left(LIS, nums[i])
            if j == len(LIS):
                LIS.append(nums[i])
            else:
                LIS[j] = nums[i]

        return len(LIS) >= n-1
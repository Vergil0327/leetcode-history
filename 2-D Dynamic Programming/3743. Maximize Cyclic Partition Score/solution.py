
# solution by @0x3f: https://www.youtube.com/watch?v=pUxUijP_R4w
# solution by @灵茶山艾府: https://leetcode.com/problems/maximize-cyclic-partition-score/solutions/7337261/transform-to-best-time-to-buy-and-sell-s-zpn0
# Where to Break the Cycle?
# Let M=nums[i] be the maximum value in nums. If there are multiple occurrences of the maximum, pick any one of them.

# Suppose we already have an optimal partition. Consider the subarray that contains M, and let the minimum value in this subarray be at index j.

# If i≤j, we can assign the elements to the left of i to the previous subarray without making the result worse. In this case, M is at the leftmost position of its subarray.
# If i≥j, we can assign the elements to the right of i to the next subarray without making the result worse. In this case, M is at the rightmost position of its subarray.
# Therefore, there always exists an optimal partition in which M is either at the leftmost or rightmost end of a subarray.

# In other words, we can break the circular array either between (i−1,i) or between (i,i+1), thus converting it into a non-circular problem. The final answer is the maximum result obtained from these two breaking options.

# Non-Circular Array
# For each partitioned subarray:

# If the minimum value is to the left of the maximum value, it can be viewed as a buy low, sell high transaction.
# If the maximum value is to the left of the minimum value, it can be viewed as a short high, cover low transaction.
# The problem restricts the total number of subarrays to at most k, which corresponds to at most k transactions.

# This is exactly the same as 3573. Best Time to Buy and Sell Stock V.
class Solution:
    # 3573. Best Time to Buy and Sell Stock V
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[-inf] * 3 for _ in range(k + 1)]
        for j in range(1, k + 1):
            dp[j][0] = 0
        for p in prices:
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], max(dp[j][1] + p, dp[j][2] - p))
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - p)
                dp[j][2] = max(dp[j][2], dp[j - 1][0] + p)
        return dp[-1][0]

    def maximumScore(self, nums: List[int], k: int) -> int:
        max_i = nums.index(max(nums))
        ans1 = self.maximumProfit(nums[max_i:] + nums[:max_i], k)  # nums[max_i] is the first element.
        ans2 = self.maximumProfit(nums[max_i + 1:] + nums[:max_i + 1], k)  # nums[max_i] is the last element.
        return max(ans1, ans2)

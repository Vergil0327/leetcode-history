class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        mx = max(nums)

        dp = [[0]*(mx+1) for _ in range(mx+1)]

        for diff in range(mx+1):
            dp[nums[0]][diff] = 1

        for num1 in nums[1:]:
            for diff in range(mx+1):
                # abs(num1-num2) = diff
                # num2 = diff+num1 or num1-diff
                curr  = 0
                if (num2 := diff+num1) <= mx:
                    curr = max(curr, dp[num2][diff]+1)

                if (num2 := num1-diff) >= 0:
                    curr = max(curr, dp[num2][diff]+1)

                dp[num1][diff] = max(dp[num1][diff], curr)

            # remember our definetion: dp[num][diff], the longest length of subseq. ending at num with diffrence **less than or equal to** `diff`
            for diff in range(mx-1, -1, -1):
                dp[num1][diff] = max(dp[num1][diff], dp[num1][diff+1])

        return max(dp[num][diff] for num in nums for diff in range(mx+1))

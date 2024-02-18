class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = defaultdict(int)
        res = 1
        for num in nums:
            dp_next = defaultdict(int)
            dp_next[num] = 1
            dp_next[num+1] = 1

            dp_next[num-1] = dp[num-1]
            dp_next[num] = max(dp_next[num], dp[num])

            if num-1 in dp:
                dp_next[num] = max(dp_next[num], dp[num-1]+1)
                res = max(res, dp_next[num])

            if num in dp:
                dp_next[num+1] = max(dp_next[num+1], dp[num]+1)
                res = max(res, dp_next[num+1])
            
            dp = dp_next

        return res
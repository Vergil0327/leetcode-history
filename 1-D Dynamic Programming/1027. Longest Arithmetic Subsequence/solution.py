class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [defaultdict(lambda: 1) for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                diff = nums[i]-nums[j]
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)

        res = 1    
        for m in dp:
            res = max(res, max(m.values()))
        return res
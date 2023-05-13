class Solution:
    def maximumOr(self, nums: List[int], K: int) -> int:
        n = len(nums)

        prefix = [0] * (n+1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] | nums[i-1]
        
        suffix = [0] * (n+1)
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] | nums[i]

        res = 0
        for i in range(n):
            curr = nums[i]<<K
            
            # for j in range(i):
            #     curr |= nums[j]
            curr |= prefix[i]
            
            # for j in range(i+1, n):
            #     curr |= nums[j]
            curr |= suffix[i+1]

            res = max(res, curr)
        return res

class Solution_TLE:
    def maximumOr(self, nums: List[int], K: int) -> int:
        n = len(nums)

        nums = [0] + nums
        dp = [[0]*(K+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for k in range(K+1):
                for prevk in range(k+1):
                    dp[i][k] = max(dp[i][k], dp[i-1][prevk] | (nums[i]<<(k-prevk)))
                
        return dp[n][K]
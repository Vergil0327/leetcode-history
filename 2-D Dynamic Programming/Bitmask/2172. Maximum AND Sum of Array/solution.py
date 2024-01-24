class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        
        @cache
        def dfs(i, bitmask):
            if i == n: return 0
            
            # 找出當前各slot_size
            state = [0]*numSlots
            bit = bitmask
            for j in range(numSlots):
                state[j] = bit%3
                bit //= 3

            res = 0
            for slot in range(1, numSlots+1):
                if state[slot-1] >= 2: continue
                res = max(res, dfs(i+1, bitmask + pow(3, slot-1)) + (nums[i]&slot))

            return res
        return dfs(0, 0)

class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)

        mxState = pow(3, numSlots)
        dp = [[0]*mxState for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for state in range(mxState):
                for slot in range(1, numSlots+1):
                    if (state//pow(3, slot-1)) % 3 == 0: continue
                    dp[i][state] = max(dp[i][state], dp[i-1][state-pow(3, slot-1)] + (nums[i-1]&slot))

        return dp[n][mxState-1]
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = [-1]*n
        upper = SortedList()
        lower = SortedList()
        sum_upper = sum_lower = 0 
        for i, v in enumerate(nums): 
            if not upper or upper[0] <= v: 
                upper.add(v)
                sum_upper += v
            else: 
                lower.add(v)
                sum_lower += v

            if i >= x: 
                if nums[i-x] >= upper[0]: 
                    upper.remove(nums[i-x])
                    sum_upper -= nums[i-x]
                else: 
                    lower.remove(nums[i-x])
                    sum_lower -= nums[i-x]

            # balance upper and lower size
            while len(upper) > len(lower)+1: 
                v = upper[0]
                upper.remove(v)
                sum_upper -= v
                lower.add(v)
                sum_lower += v
            while len(upper) < len(lower): 
                v = lower[-1]
                lower.remove(v)
                sum_lower -= v
                upper.add(v)
                sum_upper += v

            if i >= x-1:
                vals[i-x+1] = abs(sum_upper - upper[0] * len(upper)) + abs(sum_lower - upper[0]*len(lower))

        dp = [[inf]*(k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1, n+1): 
            for j in range(1, k+1): 
                if i >= j*x: 
                    dp[i][j] = min(dp[i-1][j], vals[i-x] + dp[i-x][j-1])

        return dp[n][k]

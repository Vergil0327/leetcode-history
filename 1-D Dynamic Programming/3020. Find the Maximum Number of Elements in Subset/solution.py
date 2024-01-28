class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        count = Counter(nums)
        res = 1

        for num in sorted(count.keys()):
            if count[num] >= 2:
                dp[num] = 2

            x = int(sqrt(num))
            if pow(x, 2) == num and x != num:
                if count[num] >=2 and count[x] >= 2:
                    dp[num] = max(dp[num], dp[x]+2)
                res = max(res, dp[x]+1)
            
        one = (count[1]-1)//2
        return max(res, one*2+1)

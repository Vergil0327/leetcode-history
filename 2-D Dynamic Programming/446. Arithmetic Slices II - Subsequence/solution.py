class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        
        # dp[i][diff] : # of slices which last element is i-th elements and difference is diff
        dp = defaultdict(lambda: defaultdict(int))
        
        total = 0
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                total += dp[j][diff]
                
                if diff not in dp[j]: # create a arithmetic seq. shoe length = 2. compose of nums[j] & nums[i]
                    dp[i][diff] = 1
                else: # found a arithmetic seq. whose length equals 2. 2 plus current one forms a valid arithmetic array
                    dp[i][diff] += dp[j][diff] + 1
                
        return total

class SolutionTLE:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        
        @functools.lru_cache(None)
        def dfs(last, diff, i):
            if i == n: return 0

            cnt = dfs(last, diff, i+1)
            if nums[i]-last == diff:
                cnt += 1 + dfs(nums[i], diff, i+1)
            return cnt
            
        res = 0
        for i in range(n-1):
            for j in range(i+1, n):
                res += dfs(nums[j], nums[j]-nums[i], j+1)
        return res
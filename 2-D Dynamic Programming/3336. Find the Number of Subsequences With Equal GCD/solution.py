class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        @cache
        def dfs(i, gcd1, gcd2):
            if i >= n: return int(gcd1 == gcd2 and gcd1 > 0 and gcd2 > 0)

            return (dfs(i+1, gcd1, gcd2) + dfs(i+1, gcd(gcd1, nums[i]), gcd2) + dfs(i+1, gcd1, gcd(gcd2, nums[i]))) % mod
        return dfs(0, 0, 0)
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = int(1e9+7)

        # C m 取 n = 包含元素x + 不包含元素x = C m-1 取 n-1 + C m-1 取 n
        # m! / n! / (m-n)!
        @lru_cache(None)
        def Cmn(m, n):
            if n > m-n:
                return Cmn(m, m-n)
            if n == 0: return 1
            if n == 1: return m
            return (Cmn(m-1, n-1) + Cmn(m-1, n))%MOD

        def dfs(nums):
            if len(nums) < 3: return 1

            root = nums[0]
            left, right = [], []
            for num in nums[1:]:
                if num < root:
                    left.append(num)
                else:
                    right.append(num)
            m, n = len(left), len(right)

            l = dfs(left)
            r = dfs(right)
            return l * r * Cmn(m+n, m) % MOD
        return dfs(nums)-1
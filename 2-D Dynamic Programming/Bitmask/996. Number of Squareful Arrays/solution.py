class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        finalState = (1<<n)-1

        nums.sort()

        valid = set()
        # dfs(state, prev)
        def dfs(state, prev):
            if state == finalState:
                return 1

            for i in range(n):
                if (state>>i)&1: continue

                squareRoot = sqrt(prev+nums[i])
                if squareRoot == int(squareRoot) and squareRoot**2 == (prev+nums[i]):
                    dfs(state | (1<<i), nums[i])

        res = 0
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            res += dfs(1<<i, nums[i])
        return res

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)

        memo = [[[0] * 3 for _ in range(3)] for _ in range(n+1)]
        def dfs(i, p1, p2):
            if i >= n:
                if p1 != 2 or p2 != 2:
                    return 1
                return 0
            if memo[i][p1][p2] != 0: return memo[i][p1][p2]
            
            memo[i][p1][p2] = dfs(i+1, p1, p2)

            p = nums[i]%2
            if not (p1 == p2 == p):
                memo[i][p1][p2] += dfs(i+1, p2, p)
            return memo[i][p1][p2]%mod

        return dfs(0, 2, 2)
    

class Solution:
    def threeConsecutive(self, nums: List[int]) -> int:
        mod = 1000000007
        dpEven = [0] * 3
        dpOdd = [0] * 3

        for num in nums:
            currDp = dpEven if num % 2 == 0 else dpOdd
            numOpp = dpOdd if num % 2 == 0 else dpEven

            currDp[2] += currDp[1]
            currDp[1] += 1 + numOpp[1] + numOpp[2]

            currDp[1] %= mod
            currDp[2] %= mod

        return (dpEven[1] + dpEven[2] + dpOdd[1] + dpOdd[2]) % mod
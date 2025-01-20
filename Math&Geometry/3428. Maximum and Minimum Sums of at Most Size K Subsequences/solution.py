m, n = 100001, 71
comb = [[0]*n for _ in range(m)]

for i in range(m):
    if i < min(m, n):
        comb[i][i] = 1
    comb[i][0] = 1
    for j in range(1, i):
        if j >= n: break
        comb[i][j] = comb[i-1][j-1] + comb[i-1][j]

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        
        nums.sort()
        n = len(nums)

        res = 0
        for i in range(n):
            numberOfSubsequences = 0
            for t in range(k):
                if i >= t:
                    numberOfSubsequences += comb[i][t]
                    numberOfSubsequences %= mod
            res += (nums[i] + nums[n-i-1]) * numberOfSubsequences
            res %= mod
        return res
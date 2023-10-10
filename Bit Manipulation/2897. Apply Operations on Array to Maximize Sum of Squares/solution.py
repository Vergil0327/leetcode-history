class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7

        count = [0] * 32
        for num in nums:
            for i in range(32):
                if (num>>i)&1:
                    count[i] += 1

        res = 0
        for _ in range(k):
            cur = 0
            for i in range(32):
                if count[i] > 0:
                    count[i] -= 1
                    cur += 1<<i
            res += cur**2 % mod
        return res%mod

class Solution:
    def sumOfFlooredPairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        
        N = max(nums)
        count = [0] * (N+1)
        for num in nums:
            count[num] += 1

        presum = [0] * (N+1)
        for i in range(1, N+1):
            presum[i] = presum[i-1] + count[i]

        res = 0
        seen = set()
        for num in nums:
            if num in seen: continue
            seen.add(num)
            ans = 0
            for k in range(1, ceil(((N+1)/num)-1)+1):
                ans += k * (presum[min(N, num*(k+1)-1)] - presum[num*k-1]) % mod
                ans %= mod

            res = (res + ans*count[num])%mod
        return res

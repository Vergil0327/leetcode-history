class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)

        N = max(nums)
        mod = 10**15+7
        powmod = [pow(N, i, mod) for i in range(n)]

        res = 0
        for length in range(1, n+1):
            distinct = set()

            # rolling hash
            RH = divisible = 0
            for i in range(n):
                if i-length >= 0:
                    RH -= nums[i-length] * powmod[length-1] # pow(N, length-1, mod)
                    RH = (RH+mod)%mod
                    if nums[i-length]%p == 0:
                        divisible -= 1

                RH = RH*N + nums[i]
                RH = (RH+mod)%mod
                if nums[i]%p == 0:
                    divisible += 1

                if i >= length-1 and RH not in distinct:
                    distinct.add(RH)
                    if divisible <= k:
                        res += 1
        return res

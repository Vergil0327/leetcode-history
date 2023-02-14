class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        MOD = int(1e9+7)
        primeFactors = [2,3,5,7,11,13,17,19,23,29]

        def encode(num):
            bitmask = 0
            for i, factor in enumerate(primeFactors):
                if num%factor == 0:
                    bitmask |= (1<<i)
                    num //= factor
                if num%factor == 0:
                    return -1 # it has duplicate prime factor
            return bitmask

        counter = Counter(nums)

        n = len(primeFactors)
        dp = [0] * (1<<n)
        dp[0] = 1

        for num, cnt in counter.items():
            if num == 1: continue

            bit = encode(num)
            if bit == -1: continue
            for state in range((1<<n)-1, 0, -1):
                # check if bit is subset of state
                # if (state-bit) == (state^bit):
                if bit&state == bit:
                    dp[state] = (dp[state] + dp[state-bit] * cnt) % MOD

        # we can't just sum(dp). dp[0] is invalid because `0` means empty subset.
        res = 0
        for state in range(1, 1<<n):
            res  = (res + dp[state])%MOD

        power2 = 1
        for _ in range(counter[1]):
            power2 = power2 * 2 % MOD
        return (res * power2) % MOD
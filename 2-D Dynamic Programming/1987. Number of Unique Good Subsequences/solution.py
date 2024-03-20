class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        # dp0: the number of unique good subseq ending with 0
        # dp1: the number of unique good subseq ending with 1

        dp0 = dp1 = zero = 0
        mod = 10**9 + 7
        for i in range(len(binary)):
            if binary[i] == "0":
                dp0 = (dp0 + dp1) % mod
                zero = 1
            else:
                dp1 = (dp0+dp1+1) % mod
        return (dp0 + dp1 + zero)%mod
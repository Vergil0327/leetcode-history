class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        presum0, presum1 = [0]*(n+1), [0]*(n+1)

        for i in range(n):
          presum0[i+1] = presum0[i] + int(s[i] == "0")
          presum1[i+1] = presum1[i] + int(s[i] == "1")

        res = 0
        for i in range(1, n-1):
          if s[i] == "0":
            # only 101 valid
            res += presum1[i] * (presum1[n] - presum1[i+1])
          else:
            # only 010 valid
            res += presum0[i] * (presum0[n] - presum0[i+1])
        return res

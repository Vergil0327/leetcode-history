mod = 10**9 + 7
class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
 
        presum = [0]* (n+1)
        for i in range(n):
            presum[i+1] = presum[i] + int(s[i] == "1")

        if presum[n] == 0:return comb(n-1, 2) % mod
        if presum[n]%3: return 0

        consecutive0Right = [0] * (n+1)
        for i in range(n-1, -1, -1):
            if s[i] == "0":
                consecutive0Right[i] = consecutive0Right[i+1] + 1

        consecutive0Left = [0] * n
        for i in range(n):
            if s[i] == "0":
                consecutive0Left[i] = (consecutive0Left[i-1] if i-1>=0 else 0) + 1
        
        res = 0
        r = n-1
        for l in range(n):
            if s[l] == "0": continue

            left = presum[l+1]
            while l < r and presum[n]-presum[r] < left:
                r -= 1
            right = presum[n] - presum[r]
            middle = presum[n] - left - right
            if left == middle == right:
                res += (consecutive0Right[l+1]+1) * (consecutive0Left[r-1]+1)
                res %= mod
        return res
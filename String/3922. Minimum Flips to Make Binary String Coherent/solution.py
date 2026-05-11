"""
IQ Quest

4 cases:

    1. all 0
    2. all 1
    3. only one 1 and all remain 0
    4. start 1 and end 1 in between all 0
"""
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        if n < 3: return 0
        if n == 3:
            return 1 if s in {"110", "011"} else 0
        zero = s.count('0') # check all 1
        one = s.count('1') # check all zero
        res = min(zero, one)
        
        count0 = count1 = cur = 0
        # single 1, other zeros
        for i in range(n):
            if s[i] == '0':
                count0 += 1
            else:
                count1 += 1

            if count1 > 1:
                count1 -= 1
                cur += 1
        res = min(res, cur)

        count0 = count1 = cur = 0
        # 1 00000...0000 1
        cur += (s[0] == '0') + (s[-1] == '0')
        for i in range(1, n-1):
            if s[i] == '1':
                cur += 1
        return min(res, cur)
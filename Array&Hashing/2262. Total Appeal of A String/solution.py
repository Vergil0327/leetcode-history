class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)

        res = 0
        lastPos = [-1] * 26
        for i in range(n):
            ch = ord(s[i])-ord("a")
            res += (i-lastPos[ch]) * (n-i)
            
            lastPos[ch] = i
        return res

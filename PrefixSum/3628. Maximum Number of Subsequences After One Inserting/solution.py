class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        
        LC = [0] * n
        L = [0] * n    
        CT = [0] * (n+1)
        T = [0] * (n+1)
        
        for i in range(n):
            L[i] = (L[i-1] if i-1>=0 else 0) + int(s[i] == "L")
            LC[i] = L[i] * int(s[i] == "C")

        for i in range(n-1, -1, -1):
            T[i] = T[i+1] + int(s[i] == "T")
            CT[i] = int(s[i] == "C") * T[i]

        # base number of LCT subseq.
        res = 0
        for i in range(n-1):
            res += LC[i] * T[i+1]

        # insert "L" or "T"
        gain = max(sum(CT), sum(LC))
        
        # insert C
        for i in range(n-1):
            gain = max(gain, L[i] * T[i+1])
        return res + gain
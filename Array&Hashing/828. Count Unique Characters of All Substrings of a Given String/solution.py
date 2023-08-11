class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        nextCharIdx = [[n] * 26 for _ in range(n)]
        for i in range(n-1, 0, -1):
            for ch in range(26):
                if ch == ord(s[i])-ord("A"):
                    nextCharIdx[i-1][ch] = i
                else:
                    nextCharIdx[i-1][ch] = nextCharIdx[i][ch]
        
        lastCharIdx = [-1] * 26
        res = 0
        for i in range(n):
            ch = ord(s[i])-ord("A")
            left = i-lastCharIdx[ch]
            right = nextCharIdx[i][ch]-i

            res += left * right

            lastCharIdx[ch] = i
        return res
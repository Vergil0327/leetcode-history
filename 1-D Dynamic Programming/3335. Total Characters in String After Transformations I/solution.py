class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        length = [0] * 26

        for i in range(len(s)):
            key = ord(s[i])-ord("a")
            length[key] += 1

        for _ in range(t):
            nxt = [0] * 26
            for i in range(26):
                if i == 0: # a
                    nxt[i] += length[-1]
                elif i == 1: # b
                    nxt[i] += length[i-1] + length[-1]
                else: # c~z
                    nxt[i] += length[i-1]
                nxt[i] %= mod
            length = nxt
        return sum(length)%mod

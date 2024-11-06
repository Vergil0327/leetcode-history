class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        m, n = len(s), len(t)
        if m != n: return False
        moves = [0] * 26
        for i in range(n):
            if s[i] == t[i]: continue

            x = ((ord(t[i]) - ord(s[i]))+26)%26
            moves[x] += 1
            
            if x + 26 * (moves[x]-1) > k: return False
            
            
        return True

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frogs = c = r = o = a = k = 0
        for ch in croakOfFrogs:
            if ch == "c":
                c += 1

            if ch == "r":
                c -= 1
                r += 1
                if c < 0: return -1
                
            if ch == "o":
                r -= 1
                o += 1
                if r < 0: return -1
                
            if ch == "a":
                o -= 1
                a += 1
                if o < 0: return -1
                
            if ch == "k":
                a -= 1
            
            frogs = max(frogs, c + r + o + a)
        return frogs if c == r == o == a == 0 else -1

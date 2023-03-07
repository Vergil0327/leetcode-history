class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        counter = Counter(croakOfFrogs)
        if counter["c"] != counter["r"] or counter["r"] != counter["o"] or counter["o"] != counter["a"] or counter["a"] != counter["k"]: return -1

        maxFrogs = 0
        frogs = c = r = o = a = k = 0
        for ch in croakOfFrogs:
            if ch == "c":
                if c < r or c < o or c < a or c < k: return -1
                c += 1
                frogs += 1

            if ch == "r":
                if r < o or r < a or r < k: return -1
                r += 1
                
            if ch == "o":
                if o < a or o < k: return -1
                o += 1
                
            if ch == "a":
                if a < k: return -1
                a += 1
                
            if ch == "k":
                c, r, o, a = c-1, r-1, o-1, a-1
                frogs -= 1
            maxFrogs = max(maxFrogs, frogs)    
        return maxFrogs
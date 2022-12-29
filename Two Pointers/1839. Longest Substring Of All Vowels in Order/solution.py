class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        longest = 0
        l = 0
        # [l,r), r exclusive
        while l < n:
            if word[l] == "a":
                r = l+1
                while r < n and word[r] == "a":
                    r += 1
                if r == n: break
                if word[r] != "e":
                    l = r
                    continue

                while r < n and word[r] == "e":
                    r += 1
                if r == n: break
                if word[r] != "i":
                    l = r
                    continue
                    
                while r < n and word[r] == "i":
                    r += 1
                if r == n:break
                if word[r] != "o":
                    l = r
                    continue
                
                while r < n and word[r] == "o":
                    r += 1
                if r == n: break
                if word[r] != "u":
                    l = r
                    continue
                
                while r < n and word[r] == "u":
                    r += 1
                longest = max(longest, r-l)
                l = r
            else:
                l += 1
        return longest

# Concise version
    def longestBeautifulSubstring(self, word: str) -> int:
        seen = set()
        l, longest = -1, 0
        for r, ch in enumerate(word):
            if r > 0 and ch < word[r - 1]:
                seen = set()
                l = r - 1
            seen.add(ch)
            if len(seen) == 5:
                longest = max(longest, r - l)
        return longest
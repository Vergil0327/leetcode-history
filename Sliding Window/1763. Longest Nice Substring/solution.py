class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        res = ""
        for m in range(1, 26+1):
            l = r = 0
            window = defaultdict(int)
            count = defaultdict(int)
            
            while r < n:
                count[s[r]] += 1
                window[s[r].lower()] += 1
                r += 1

                while l < r and len(window) > m:
                    count[s[l]] -= 1
                    window[s[l].lower()] -= 1
                    if count[s[l]] == 0: del count[s[l]]
                    if window[s[l].lower()] == 0: del window[s[l].lower()]
                    l += 1
                
                if r-l > len(res) and len(window) == m and all((count[ch.lower()]> 0 and count[ch.upper()]) for ch in window):
                    if len(s[l:r]) > len(res):
                        res = s[l:r]
        return res
    

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        characters = set(s)
        for i, ch in enumerate(s):
            if ch.lower() not in characters or ch.upper() not in characters:
                # res1 = self.longestNiceSubstring(s[:i])
                # res2 = self.longestNiceSubstring(s[i+1:])
                # if len(res1) >= len(res2): # 注意這裡是 >=, 因為相同的話要返回res1 (first occurence)
                #     return res1
                # else:
                #     return res2
                return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key=len)
        return s

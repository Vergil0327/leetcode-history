class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        counter = Counter(s)
        if counter["a"] < k or counter["b"] < k or counter["c"] < k:
            return -1
        
        l, r = 0, 0
        maxLen = 0
        while r < n:
            ch = s[r]
            if ch == "a":
                counter["a"] -= 1
            elif ch == "b":
                counter["b"] -= 1
            else:
                counter["c"] -= 1
            r += 1
            
            while counter["a"] < k or counter["b"] < k or counter["c"] < k:
                c = s[l]
                if c == "a":
                    counter["a"] += 1
                elif c == "b":
                    counter["b"] += 1
                else:
                    counter["c"] += 1
                l += 1
            maxLen = max(maxLen, r-l)

        return n-maxLen

# Brute Force
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        
        counter = Counter(s)
        if counter["a"] < k or counter["b"] < k or counter["c"] < k: return -1
        
        @lru_cache(None)
        def dfs(l, r, a, b, c):
            if a >= k and b >= k and c >= k:
                return 0
            if l > r: return inf
            
            
            minutes = inf
            if s[l] == "a":
                minutes = min(minutes, dfs(l+1, r, a+1, b, c)+1)
            elif s[l] == "b":
                minutes = min(minutes, dfs(l+1, r, a, b+1, c)+1)
            elif s[l] == "c":
                minutes = min(minutes, dfs(l+1, r, a, b, c+1)+1)
                
            if s[r] == "a":
                minutes = min(minutes, dfs(l, r-1, a+1, b, c)+1)
            elif s[r] == "b":
                minutes = min(minutes, dfs(l, r-1, a, b+1, c)+1)
            elif s[r] == "c":
                minutes = min(minutes, dfs(l, r-1, a, b, c+1)+1)
                
            return minutes

        minMinute = dfs(0, n-1, 0, 0, 0)
        return minMinute if minMinute != inf else -1
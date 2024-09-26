class Solution:
    def splitString(self, s: str) -> bool:
        @cache
        def dfs(l, r):
            cur = int(s[l:r+1])
            remain = s[r+1:]
            if not remain : return True

            for i in range(n):
                if cur - int(remain[:i+1]) == 1: # descending order and difference = 1
                    if dfs(r+1, r+1+i): return True
            return False


        n = len(s)
        for i in range(n-1):
            if dfs(0, i): return True
        return False

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        def rotate(s):
            res = [""] * n
            for i, c in enumerate(s):
                res[(i+b)%n] = c
            return "".join(res)

        def inc(s):
            res = ""
            for i, c in enumerate(s):
                if i%2 == 1:
                    res += str((int(c)+a)%10)
                else:
                    res += c
            return res

        seen = set()
        res = s
        def dfs(s):
            nonlocal res
            
            if s in seen: return
            seen.add(s)

            res = min(res, s)
            
            dfs(rotate(s))
            dfs(inc(s))
        dfs(s)
        return res

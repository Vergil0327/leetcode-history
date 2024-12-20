class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        @cache
        def check(s, j):
            if j >= len(pattern):
                while s and s[0].islower():
                    s = s[1:]
                return not s

            if pattern[j].isupper():
                while s and s[0].islower():
                    s = s[1:]
                if not s: return False

                if s[0] == pattern[j]:
                    return check(s[1:], j+1)
                else:
                    return False
            else:
                while s and s[0].islower():
                    if s[0] == pattern[j]:
                        j += 1
                        return check(s[1:], j)
                    
                    s = s[1:]
                return False

        for s in queries:
            res.append(check(s, 0))
        return res

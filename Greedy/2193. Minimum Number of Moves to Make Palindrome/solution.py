# class Solution:
#     def minMovesToMakePalindrome(self, s: str) -> int:
#         s = list(s)

#         res = 0
#         while s:
#             idx = s.index(s[-1])
#             if idx == len(s)-1: # single character, the middle of palindrome
#                 res += idx//2
#                 s.pop()
#             else:
#                 res += idx
#                 s.pop(idx)
#                 s.pop()

#         return res

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)

        @cache
        def dfs(s):
            if len(s) <= 2: return 0

            # swap s[0] to become s[-1]
            # or swap s[-1] to become s[0]
            n = len(s)
            res = inf
            L, R = 0, len(s)-1
            l, r = 0, len(s)-1
            swap = 0
            while s[l] != s[R] and s[r] != s[L]:
                swap += 1
                l, r = l+1, r-1
            if s[l] == s[R] and s[r] == s[L]:
                # swap s[l] to s[0]
                s1 = s[:l] + s[l+1:n-1]
                res = min(res, dfs(s1)+swap)

                # swap s[r] to s[-1]
                # s2 = s[1:r] + s[r+1:]
                # res = min(res, dfs(s2)+swap)
                
                # don't need to, just choose any of them
                # res = min(res, dfs(s1)+swap, dfs(s2)+swap)
            elif s[l] == s[R]:
                s1 = s[:l] + s[l+1:n-1]
                res = min(res, dfs(s1) + swap)
            else:
                s2 = s[1:r] + s[r+1:]
                res = min(res, dfs(s2) + swap)

            return res

        return dfs(s)


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)

        res = 0
        while s:
            idx = s.index(s[-1])
            if idx == len(s)-1: # single character, the middle of palindrome
                res += idx//2
                s.pop()
            else:
                res += idx
                s.pop(idx)
                s.pop()

        return res

from collections import Counter
import string

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        self.res = ""
        def dfs(i, strictGreater, perm):
            if i >= n:
                if strictGreater:
                    self.res = perm
                    return True
                return False

            res = 0
            for c in string.ascii_lowercase:
                if count[c] == 0: continue
                count[c] -= 1
                if strictGreater or c >= target[i]:
                    if dfs(i+1, strictGreater or c > target[i], perm + c): return True
                count[c] += 1
            return res
        dfs(0, False, "")
        return self.res
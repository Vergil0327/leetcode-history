class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]: return False
                l, r = l+1, r-1
            return True

        res = []
        def dfs(state, s):
            if not s:
                res.append(state.copy())
                return

            for i in range(len(s)):
                left, right = s[:i+1], s[i+1:]
                if isPal(left):
                    state.append(left)
                    dfs(state, right)
                    state.pop()
        dfs([], s)
        return res
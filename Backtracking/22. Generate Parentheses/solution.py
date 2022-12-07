class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(state, l, r):
            if l == n and r == n:
                res.append(state)
                return
            if l < n:
                state += "("
                dfs(state, l+1, r)
                state = state[:-1]
            if r < l and r < n:
                state += ")"
                dfs(state, l, r+1)
                state = state[:-1]
        dfs("", 0, 0)
        return res
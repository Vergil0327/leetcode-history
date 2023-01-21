class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n > 12: return []

        res = []
        def dfs(state, i, dots):
            if dots == 0 and i == n:
                res.append(".".join(state))
                return
            if dots < 0 or i > n: return

            for j in range(i, min(i+3, len(s))):
                addr = s[i:j+1]
                if len(addr) > 1 and addr[0] == "0": continue
                if int(addr) > 255: continue

                state.append(addr)
                dfs(state, j+1, dots-1)
                state.pop()

        dfs([], 0, 4)
        return res
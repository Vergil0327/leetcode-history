class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        cookies.sort()
        
        self.res = inf
        state = [0]*k
        def dfs(i):
            if i == n:
                self.res = min(self.res, max(state))
                return
            if max(state) >= self.res: return

            flag = 0
            for kid in range(k):
                if state[kid] == 0:
                    if flag == 1: continue
                    flag = 1

                state[kid] += cookies[i]
                dfs(i+1)
                state[kid] -= cookies[i]
        dfs(0)
        return self.res
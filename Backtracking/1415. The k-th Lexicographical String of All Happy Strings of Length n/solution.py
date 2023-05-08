class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        chs = ["a", "b", "c"]

        self.count = 0
        res = ""
        def dfs(state, i):
            nonlocal res
            
            if i == n:
                self.count += 1 # 每當找到符合條件的state, 便計數器加一

                if self.count == k: # found k-th happy string
                    res = "".join(state)
                    return True
                return False

            for ch in chs:
                if state and state[-1] == ch: continue

                # backtracking
                state.append(ch)
                if dfs(state, i+1): return True
                state.pop()
            return False
        dfs([], 0)
        return res
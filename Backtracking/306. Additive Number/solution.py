# brute force - DFS backtracking
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(state, num):
            if len(state) > 2 and state[-1] != state[-2] + state[-3]: return False
            if not num:
                return True if len(state) > 2 else False
            
            for i in range(1, len(num)+1):
                if len(num[:i])>1 and num[:i][0] == "0": continue
                if len(state) > 2 and i < len(str(state[-1]+state[-2])): continue
                
                state.append(int(num[:i]))
                if dfs(state, num[i:]): return True
                state.pop()
            return False

        return dfs([], num)
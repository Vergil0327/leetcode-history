class Solution:
    def diffWaysToCompute(self, expr: str) -> List[int]:
        def dfs(i, j):
            res = []
            for k in range(i, j+1):
                if expr[k] in {"+","-","*"}:
                    left = dfs(i, k-1)
                    right = dfs(k+1, j)
                    # print(left, expr[k], right)
                    if expr[k] == "+":
                        for a in left:
                            for b in right:
                                res.append(a+b)
                    elif expr[k] == "-":
                        for a in left:
                            for b in right:
                                res.append(a-b)
                    else:
                        for a in left:
                            for b in right:
                                res.append(a*b)
            if i == j:
                res.append(int(expr[i:j+1]))
            if not res: # edge case: append num to res if there is no operator in expr. ex. expr="21"
                res.append(int(expr[i:j+1]))
            return res
        return dfs(0, len(expr)-1)

class OptimizedSolution:
    def diffWaysToCompute(self, expr: str) -> List[int]:
        memo = {}
        def dfs(i, j):
            if expr[i:j+1] in memo:
                return memo[expr[i:j+1]]

            res = []
            for k in range(i, j+1):
                if expr[k] in {"+","-","*"}:
                    left = dfs(i, k-1)
                    right = dfs(k+1, j)
                    # print(left, expr[k], right)
                    if expr[k] == "+":
                        for a in left:
                            for b in right:
                                res.append(a+b)
                    elif expr[k] == "-":
                        for a in left:
                            for b in right:
                                res.append(a-b)
                    else:
                        for a in left:
                            for b in right:
                                res.append(a*b)
            if i == j:
                res.append(int(expr[i:j+1]))
            if not res: # edge case: append num to res if there is no operator in expr. ex. expr="21"
                res.append(int(expr[i:j+1]))
            
            memo[expr[i:j+1]] = res
            return res
        return dfs(0, len(expr)-1)

class OptimizedSolution:
    def diffWaysToCompute(self, expr: str) -> List[int]:
        @lru_cache(None)
        def dfs(i, j):

            res = []
            n = len(expr)
            for k in range(i, j+1):
                if expr[k] in {"+","-","*"}:
                    left = dfs(i, k-1)
                    right = dfs(k+1, j)
                    # print(left, expr[k], right)
                    if expr[k] == "+":
                        for a in left:
                            for b in right:
                                res.append(a+b)
                    elif expr[k] == "-":
                        for a in left:
                            for b in right:
                                res.append(a-b)
                    else:
                        for a in left:
                            for b in right:
                                res.append(a*b)
            if i == j:
                res.append(int(expr[i:j+1]))
            if not res: # edge case: append num to res if there is no operator in expr. ex. expr="21"
                res.append(int(expr[i:j+1]))
            
            return res
        return dfs(0, len(expr)-1)
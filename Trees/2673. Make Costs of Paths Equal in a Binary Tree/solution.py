class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.res = 0
        cost = [0] + cost
        h = floor(log2(n))

        def dfs(node):
            if node >= 2**h:
                if node > n:
                    return cost[0]
                return cost[node]
            
            left = dfs(2*node)
            right = dfs(2*node+1)
            self.res += abs(left-right)

            return cost[node] + max(left, right)
        dfs(1)
        return self.res

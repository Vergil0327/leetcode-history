from typing import List

"""
Knapsack Merge, dp
"""
def knapsack_merge(A, B):
    C = [-inf] * len(A)
    for budget1, p in enumerate(A):
        for budget2 in range(len(A) - budget1):
            C[budget1 + budget2] = max(C[budget1 + budget2], p + B[budget2])
    return C

class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:

        graph = [[] for _ in range(n)]
        for u, v in hierarchy:
            u, v = u-1, v-1
            graph[u].append(v)

        def dfs(node, prev):
            child_dp0 = [0] * (budget + 1) # max profit for budget b with no discount
            child_dp1 = [0] * (budget + 1) # max profit for budget b with this node discounted
            for child in graph[node]:
                if child != prev:
                    # res0[b] : max profit for budget b with no discount
                    # res1[b] : max profit for budget b with this node discounted
                    res0, res1 = dfs(child, node)
                    child_dp0, child_dp1 = knapsack_merge(child_dp0, res0), knapsack_merge(child_dp1, res1)

            # buy without discount, parent didn't buy the stock
            ans0 = child_dp0[:]
            cost = present[node]
            for b in range(cost, budget + 1):
                ans0[b] = max(ans0[b], child_dp1[b - cost] + future[node] - cost)

            # buy when parent bought the stock
            ans1 = child_dp0[:]
            cost //= 2
            for b in range(cost, budget + 1):
                ans1[b] = max(ans1[b], child_dp1[b - cost] + future[node] - cost)

            return ans0, ans1

        no_discount, discount = dfs(0, -1)
        return max(no_discount)

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in hierarchy:
            graph[u - 1].append(v - 1)

        dp = [[[0] * (budget + 1) for _ in range(2)] for _ in range(n)]
        self.dfs(0, present, future, graph, dp, budget)
        return max(dp[0][0])

    def dfs(self, node, present, future, graph, dp, budget):
        children = graph[node]
        child_dps = []
        for v in children:
            self.dfs(v, present, future, graph, dp, budget)
            child_dps.append((dp[v][0], dp[v][1]))

        for parentBought in range(2):
            price = present[node] // 2 if parentBought else present[node]
            profit = future[node] - price

            # Option 1: not buying u
            base = [0] * (budget + 1)
            for c0, _ in child_dps:
                next_base = [0] * (budget + 1)
                for b in range(budget + 1):
                    if base[b] == 0 and b != 0:
                        continue
                    for k in range(budget - b + 1):
                        next_base[b + k] = max(next_base[b + k], base[b] + c0[k])
                base = next_base

            curr = base[:]

            # Option 2: buying u
            if price <= budget:
                base = [0] * (budget + 1)
                for _, c1 in child_dps:
                    next_base = [0] * (budget + 1)
                    for b in range(budget + 1):
                        if base[b] == 0 and b != 0:
                            continue
                        for k in range(budget - b + 1):
                            next_base[b + k] = max(next_base[b + k], base[b] + c1[k])
                    base = next_base

                # compare 2 options
                for b in range(price, budget + 1):
                    curr[b] = max(curr[b], base[b - price] + profit)

            dp[node][parentBought] = curr
# Intuition

def dfs(node, prev) = res0, res1, where:
- res0[b] : max profit for budget b with no discount
- res1[b] : max profit for budget b with this node discounted

Consider all direct children v of u. We have to aggregate all v.res0 and v.res1 together, since either we purchase stock u and all these v's are discounted, or we don't and they aren't.

### knapsack aggregation/merge

The aggregation is done using C := merge(A, B). A[b1] and B[b2] represent possible choices to spend budgets b1 and b2 and C[b1+b2] = max(A[b1] + B[b2], ...) is the best choice.

state transition:

```py
# Knapsack Merge
dp = [-inf] * len(dpA)
for budget1, p in enumerate(dpA):
    for budget2 in range(len(dpA) - budget1):
        dp[budget1 + budget2] = max(dp[budget1 + budget2], p + dpB[budget2])
return dp
```

Afterwards, we have to account for purchasing at node u, which adds cost to the budget. There are two cases, full cost and half cost, depending on if we got the discount from the parent.


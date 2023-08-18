# Intuition

houses: X X X X X X X X X
each houses[i] must have one of color 1~n and we want `target` neighborhood

I think we can use dp to solve it, so... try to define dp and required state.

first, dp[i]: the minimum cost of painting houses[:i]
and we probably also need to know the houses[i-1]'s color to check if we form a new neighborhood
and we also need to know how many neighborhood we have so far

dp[i][j][k]: the minimum cost of painting houses[:i] ended at j color and there are k neighborhoods right now.

then try to infer state-transfer fn.

1. if houses[i] == 0:
    - dp[i][j][k] = dp[i-1][j'][k] + cost[i][j] if j == j'
    - dp[i][j][k] = dp[i-1][j'][k-1] + cost[i][j] if j != j' => form new neighborhood
    - choose strategy with minimum cost
2. if houses[i] != 0: (already painted)
    - dp[i][j][k] = dp[i-1][j'][k] if j == j'
    - dp[i][j][k] = dp[i-1][j'][k-1] if j != j' => form new neighborhood
    - choose strategy with minimum cost

then final answer should be min(dp[n][j][target]) where j can ended at any color from 1~n
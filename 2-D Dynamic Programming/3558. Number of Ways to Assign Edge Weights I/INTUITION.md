# Intuition

想到BFS + DP, 從跟節點出發, parity可以是0或1, 此時方法數為1
再來就透過BFS直到結束, 狀態變化為:

定義`dp[node, prev, parity]`: the ways to reach `node` from `prev` with `parity`, 其中(node, prev) 其實就是edge

```py
if node == 1: # base case
    next_dp[neighbor, node, parity] = 1
    next_dp[neighbor, node, parity^1] = 1
else:
    next_dp[neighbor, node, parity] += dp[node, prev, parity]
    next_dp[neighbor, node, parity] %= 1000000007

    next_dp[neighbor, node, parity^1] += dp[node, prev, parity]
    next_dp[neighbor, node, parity^1] %= 1000000007
```

最後我們在找到最深的leaf node的方法數即可
由於深度相同, 經過的邊的數目也相同, 所以返回任意一個最深的葉子節點方法數即可:

```py
res = 0
for node, prev, parity in dp:
    if node in deepest and parity==1:
        return dp[node, prev, parity]
return res
```
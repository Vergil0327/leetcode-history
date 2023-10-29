# Intuition

兩種操作:
op1. coins[node] - k
op2. coins[node] << t
  - 另外, 由於 coins[i] <= 10^4 => log2(10000) = 13.2877123795 < 14
  - 所以當t >= 14時, coins[node] = 0, 沒法再獲得points

再來我們可以用top-down dp (DFS) 來模擬
並且對於當前coins[node], 我們必須知道到目前為止前面做了幾次op2操作, 所以我們還必須記錄狀態`t`

所以我們的dfs狀態會是: `def dfs(node, prev, t): the maximum point collected until current node when we execut t times operation 2`

那麼對於當前node來說, 當前point = coins[node]>>t
1. 如果當前選擇op1, 那麼dfs(node, prev, t) = point - k + sum(dfs(child, node, t) for child in graph[node])
2. 如果當前選擇op2, 那麼dfs(node, prev, t) = point>>1 + sum(dfs(child, node, t+1) for child in graph[node])

返回兩者中較大的即為當前最佳解
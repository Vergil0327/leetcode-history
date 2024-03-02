# Intuition

2 <= n <= 1000 => time complexity可以O(n^2)
先直觀來看怎麼解, 對於每個root節點
我們希望能找到每個subtree有多少個path_sum%signalSpeed == 0的節點
res[root] += 任兩個不重複subtree的有效節點數相乘

所以我們可以遍歷root node
我們用dfs計算出當前subtree有多少有效節點, 並持續紀錄過往有多少有效節點個數
那麼對於當前subtree如果有`cnt`個有效節點, 他跟過往所有subtree能組成的pair為`cnt` * `presum_cnt`

整體框架為:

```py
res = [0] * n
for root in range(n):
    presum_cnt = 0
    for wei, nxt in graph[root]:
        cnt = dfs(nxt, root, wei)
        res[root] += presum_cnt * cnt
        presum_cnt += cnt
```

那計算當前subtree有效節點個數則為:
```py
def dfs(node, prev, pathSum):
    cnt = pathSum % signalSpeed == 0
    for wei, nxt in graph[node]:
        if nxt == prev: continue
        cnt += dfs(nxt, node, pathSum+wei)
    return cnt
```
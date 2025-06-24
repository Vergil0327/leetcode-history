# Intuition

直覺想到用post-order DFS找出每個子路徑的分數總和為多少, 以及當前的最大子路徑分數
然後計算有多少小於**最大子路徑分數**的子路徑需要額外加上分數

遍歷整棵樹一遍後即可知道數量

```py
self.res = 0
def dfs(node, parent):
    cur = cost[node]
    childs = []
    mx = 0
    for nxt in graph[node]:
        if nxt != parent:
            x = dfs(nxt, node)
            childs.append(x)
            mx = max(mx, x)
    self.res += len(list(filter(lambda x: x != mx, childs)))
    return cur+mx
```
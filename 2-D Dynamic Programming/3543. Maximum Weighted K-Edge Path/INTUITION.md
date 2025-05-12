# Intuition

試著用dfs模擬可能選擇並挑出minimum sum, 由於每個節點都可能是起始點, 所以全部節點都進行一次dfs

由於edge比需剛好是`k`個, 所以我們在dfs上紀錄這個訊息以及當前節點, 定義:

dfs(node, edge): the minimum sum when current node is `node` and edge's count is `edge`

再來就試著dfs往外擴展, 這邊我們返回所有**小於t**的可能答案, 因為不一定哪個會是最佳解, 所以用array全存著, 並且在用一個`boolean`去表示當前這些是否有剛好`k`個edges

所以主要框架為:

```py
for node in range(n):
    ans, valid = dfs(node, 0)
    if valid and ans:
        res = max(res, max(ans))
```

而DFS遍歷細節就如題意限制去走就好:

```py
@lru_cache(None)
def dfs(node, edge):
    if edge == k:
        return [0], True

    res = set()
    state = False
    for nxt in graph[node]:
        arr, valid = dfs(nxt, edge+1)
        if valid:
            state = True
            for x in arr:
                if x+graph[node][nxt] < t:
                    res.add(x+graph[node][nxt])

    return res, state
```
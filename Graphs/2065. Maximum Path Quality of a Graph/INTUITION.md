# Intuition

先找出unreachable nodes, 並把他們從graph中剔除

這題比較關鍵的constraint是:
`10 <= timej, maxTime <= 100`

會發現最多就只會走10步, 那由於每個節點最多四條邊
所以$4^10$約為$10^6$時間複雜度
因此我們可以用DFS遍歷每個可能path然後挑最大的即可

1. 首先建立adjacency list, 然後想到的是透過BFS先找出最遠能抵達到哪些node, 存進hashset裡. 然後再把不在這hashset裡的節點從adjacency list中移除

```py
graph = defaultdict(set)
n = len(values)

times = [[0] * n for _ in range(n)]
for u, v, t in edges:
    graph[u].add(v)
    graph[v].add(u)
    times[u][v] = times[v][u] = t

queue = deque([[0,0]])
visited = set()
while queue:
    node, curT = queue.popleft()
    if node in visited: continue
    visited.add(node)
    for nei in graph[node]:
        if (t := curT + 2*times[node][nei]) <= maxTime:
            queue.append([nei, t])

for node in range(n):
    if node not in visited:
        for nei in graph[node]:
            graph[nei].remove(node)
        del graph[node]
```

2. 再來遍歷所有path, 這時唯一的邊界條件就是時間, **maxTime**. 我們任意進行DFS, 一但回到根節點, 代表我們找到一個可行路徑, 更新res = max(res, path_sum)

```py
ROOT = 0
def dfs(node, visited, time):
    cur = sum(values[node] for node in visited) if node == ROOT else 0

    for nei in graph[node]:
        if time >= times[node][nei]:
            cur = max(cur, dfs(nei, visited | {nei}, time - times[node][nei]))
    return cur
```

但實際上我們只受限`maxTime`, 所以可以不用第一步, 直接進行DFS即可
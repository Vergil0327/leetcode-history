# Intuition

每個query包含三個值分別是[start, end, node]
我們要根據每個query，找出從`start`節點到`end`節點路徑上離`node`最近的節點

這題的標準解法是:

首先我們可以對每個節點進行dfs，找出以每個節點為起點離各個節點的距離

```py
distMatrix = [[0]*n for _ in range(n)]
def dfs(root, node, parent, dist):
    for nei in graph[node]:
        if nei != root and distMatrix[root][nei] != 0: continue
        if nei == parent: continue
        distMatrix[root][nei] = dist+1
        dfs(root, nei, node, dist+1)

for node in range(n):
    dfs(node, node, node, 0)
```

找出來後我們可以遍歷每個query，然後從`start`節點開始BFS
如果整個路徑的距離長度是`distMatrix[start][end]`，那麼`start`往`end`的下個節點離end的的距離必定是`distMatrix[start][end] - 1`，也就是`distMatrix[next][end]+1 = distMatrix[start][end]`

透過這個條件，我們便能透過BFS找出下個節點，然後依序前進
然後我們在比較路徑上的每個節點與目標`node`節點間的距離，找出最近的加入到答案當中即可

```py
res = []
for start, end, node in query:
    # BFS
    queue = deque([start])
    minDist = float('inf')
    closestNode = None
    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if distMatrix[node][curr] < minDist:
                minDist = distMatrix[node][curr]
                closestNode = curr
            if curr == end: break

            for nei in graph[curr]:
                if distMatrix[nei][end] + 1 == distMatrix[curr][end]:
                    queue.append(nei)
    res.append(closestNode)
```
# Intuition

整個special path從root往下, 必須都是distinct values, 要找最長的depth-first path, 並且cost最低
如果不是顆樹的話, 而是個array的話, 我們可以用sliding window去找出longest distinct path
所以同理, 這個問題就是要在這棵樹上進行sliding window

在樹上進行slinding window, 同樣得紀錄左右端點, 左端點`start`, 右端點`cur_depth`
那這樣該window size即為`cur_depth-start`

```py
graph = defaultdict(lambda: defaultdict(int))
for u, v, w in edges:
    graph[u][v] = w
    graph[v][u] = w
    
self.res = [0, 1] # longest length, minimum number of nodes in longest path
depth = defaultdict(int)

def dfs(node, parent, start, cur_depth):
    # update sliding window left endpoint: `start`
    prev_depth = depth[nums[node]]
    depth[nums[node]] = cur_depth
    start = max(start, prev_depth)

    length = cur_depth-start
    if window_weight > self.res[0]:
        self.res = [window_weight, length]
    elif window_weight == self.res[0]:
        self.res[1] = min(self.res[1], length)

    for nxt in graph[node]:
        if nxt == parent: continue
        dfs(nxt, node, start, cur_depth+1)

    depth[nums[node]] = prev_depth
```

看上面主框架會發現, 我們還差個window_weight要維護
所以就像sliding window一樣, 我們必須額外維護個prefix_sum, 使得`window_cost = prefix_sum[-1] - prefix_sum[start]`可以用O(1)時間查詢
那維護這個prefix sum的概念就像backtracking

```py
self.res = [0, 1] # longest length, minimum number of nodes in longest path
depth = defaultdict(int)
self.prefix_sum = [0]

def dfs(node, parent, start, cur_depth):
    prev_depth = depth[nums[node]]
    depth[nums[node]] = cur_depth
    start = max(start, prev_depth)

    length = cur_depth-start
    window_weight = self.prefix_sum[-1] - self.prefix_sum[start]
    if window_weight > self.res[0]:
        self.res = [window_weight, length]
    elif window_weight == self.res[0]:
        self.res[1] = min(self.res[1], length)

    for nxt in graph[node]:
        if nxt == parent: continue

        self.prefix_sum.append(self.prefix_sum[-1] + graph[node][nxt]) # <- append new value to prefix_sum
        dfs(nxt, node, start, cur_depth+1)
        self.prefix_sum.pop() # <- pop up value with backtracking

    depth[nums[node]] = prev_depth

dfs(0, -1, 0, 1)
return self.res
```

這樣就完成了, 這個程式遍歷每個節點, 所以時間複雜度是O(n), 空間上也是
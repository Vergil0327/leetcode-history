# Intuition

從node-0反方向出發考察? => BFS能確認是否能與其他每個節點相通 (查看我們是否能訪問到每個節點即可, len(visited) == n)

但要如何決定消除哪個edge?
我們要找出minimum value of maximum wei, 要找這種min max感覺可以試試用binary search去猜猜看
那這樣的話, 對於當前猜測的`w`, 代表在w以上的wei都是得removed掉的

這樣一想, 整個框架就都有了:

search space: 
```py
# search space: 由於1 <= Wi <= 10^6, 所以我們上限設10^6+1, 一但最終答案超出upperbound, 代表找不到合法解
l, r = 1, 1_000_001

while l < r:
    m = l + (r-l)//2
    if check(m):
        r = m
    else:
        l = m+1
return l if l < 1_000_001 else -1
```

那helper function `check`, 就利用BFS即可

```py
graph = defaultdict(lambda: defaultdict(lambda: inf))
for u, v, w in edges:
    graph[v][u] = min(graph[v][u], w) # 重複edge取最小weight

def check(wei):
    queue = deque([0])
    visited = set()

    while queue:
        node = queue.popleft()
        if node in visited: continue
        visited.add(node)

        for nxt in graph[node]:
            if graph[node][nxt] > wei: continue
            queue.append(nxt)

    return len(visited) == n
```

但這時發現我們還有個條件沒用到: Each node has at most `threshold` outgoing edges.
但在我們的helper function `check`裡, 對於每個節點BFS只會訪問一次, 代表節點連接也只會用到一個邊, 其餘都用不到
因此對於每個BFS遍歷到的節點, 我們outgoing edge都只會有一條, 而`1 <= threshold`, 所以代表不管threshold多少, 都一定能符合
所以我們可以無視threshold這個限制

# Intuition 2

看到這解法整個驚醒, 其實我們只需要從節點0出發, 利用dijkstra找出所需的最小權重
如果找到權重的同時, 所有節點都還能抵達, 那代表當前最小權重即為答案

而threshold也同上述, 由於我們節點間都只需要一條邊, 所以一定能符合
# Intuition

這題想法很直覺:
1. 先用DFS找出leaf node, 並建立adjacency list
2. 利用BFS從每個leaf node出發, 紀錄steps, 直到steps > distance結束
   - 每當行程leaf node pair, 我們就加進hashset, 最終hashset.size即為答案
   - 過程中我們為了避免重複, 我們在第一步dfs的時候, 順便對每個node給定一個id

### 第一段DFS:

```py
self.leaf = set()
self.graph = defaultdict(set)
_id = {}
id = 0

def dfs(node, parent):
    nonlocal id
    if not node: return
    _id[node] = id
    id += 1

    if not node.left and not node.right:
        self.leaf.add(node)

    if node.left:
        self.graph[node].add(node.left)
        self.graph[node.left].add(node)
        dfs(node.left, node)
    if node.right:
        self.graph[node].add(node.right)
        self.graph[node.right].add(node)
        dfs(node.right, node)
dfs(root, None)
```

### 第二段 BFS:

```py
queue = deque()
for node in self.leaf:
    queue.append([node, _id[node]])

pair = set()
seen = set()
while distance >= 0 and queue:
    for _ in range(len(queue)):
        node, start_id = queue.popleft()
        if (_id[node], start_id) in seen or (start_id, _id[node]) in seen: continue
        seen.add((_id[node], start_id))

        if node in self.leaf and _id[node] != start_id:
            pair.add((min(_id[node], start_id), max(_id[node], start_id)))

        for nxt in self.graph[node]:
            if nxt in _id and _id[nxt] == start_id: continue
            queue.append([nxt, start_id])

    distance -= 1

return len(pair)
```

# Intuition 2

另外看到個更優秀的one pass DFS解法是:

我們的dfs返回每個leaf node走的步數, 當走到leaf node時, 我們返回[1]
然後在post-order DFS的地方, 去計算左右兩節點的距離之和, 是否小於對於**distance**, 如果是, 那就找到1合法pair

之後我們返回左右節點的**所有步數+1**, 並汰除掉步數超過**distance**的可能, 然後遞歸計算

```py
res = 0
def dfs(node) -> list[int]:
    if not node: return []
    if node.left is node.right: # it means node is leaf node since leaf.left == leaf.right == None
        return [1]

    right = dfs(node.right)
    left = dfs(node.left)

    nonlocal res
    for r in right:
        for l in left:
            if l + r <= distance:
                res += 1
    leaves = []
    for x in right + left:
        x += 1
        if x < distance:
            leaves.append(x)
    return leaves

dfs(root)
return res
```
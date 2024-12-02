# Intuition

能直覺想出brute force solution:

- tree1對每個節點找出even edges的target
- tree2對每個節點找出odd edges的target (這樣兩棵樹連接後, 該節點的奇數距離target就會是tree1的偶數距離target)

```py
def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
    graph1, graph2 = defaultdict(list), defaultdict(list)
    for u, v in edges1:
        graph1[u].append(v)
        graph1[v].append(u)

    for u, v in edges2:
        graph2[u].append(v)
        graph2[v].append(u)

    n, m = len(edges1)+1, len(edges2)+1

    @cache
    def dfs1(node, prev, isEven):
        res = isEven
        for nxt in graph1[node]:
            if nxt == prev: continue
            res += dfs1(nxt, node, 1-isEven)
        return res

    @cache
    def dfs2(node, prev, isEven):
        res = isEven
        for nxt in graph2[node]:
            if nxt == prev: continue
            res += dfs2(nxt, node, 1-isEven)
        return res

    count1 = Counter()
    for node in range(n):
        count1[node] = dfs1(node, -1, 1)

    count2 = Counter()
    for node in range(m):
        count2[node] = dfs2(node, -1, 0)
    
    best = max(count2.values())
    return [count1[node] + best for node in range(n)]
```

但看到限制2 <= n, m <= 10^5, 因此當前想法的O(n^2)時間複雜度會超時

看到這種要更換節點然後又要降低複雜度的, 首先想到Re-Root
會看到我們在計算**tree1的root0**的偶數距離節點時, 它的鄰接節點的偶數距離節點其實就是全部**tree1**節點減去root0的偶數節點

同樣地, 我們要計算**tree2的root0**的奇數距離節點時, 鄰接節點的奇數距離節點就是全部**tree2**節點數減去root0的奇數節點(也就是root0的偶數節點)

那這樣我們僅需要O(n + m)的時間就能求出:
- tree1每個節點的偶數距離節點
- tree2的每個節點的奇數距離節點

再來我們找出tree2裡的最佳connect node, 也就是奇數距離節點最多的節點後:

`answer = (countEven[node] + best_in_tree2) for node in tree1`

```py
@cache
def dfs2(node, prev, isEven):
    res = isEven
    for nxt in graph2[node]:
        if nxt == prev: continue
        res += dfs2(nxt, node, 1-isEven)
    return res

def reroot2(node, prev, count):
    for nxt in graph2[node]:
        if nxt == prev: continue
        countOdd[nxt] = m-count
        reroot2(nxt, node, m-count)

countOdd = Counter()
countOdd[0] = dfs2(0, -1, 0)
reroot2(0, -1, countOdd[0])

best = max(countOdd.values())
```
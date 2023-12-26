# Intuition

```
source = X {X X X X X} X X X
            j       i
```

如果定義dp[i]: the smallest cost to change the first i characters (prefix) of source into target, leaving the suffix untouched

那麼狀態轉移方程可以為:

1. 首先看以i為結尾往前找個j使得source[j:i]出現在original裡, 且target[j:i]出現在changed裡, 那麼:

**dp[i] = dp[j-1] + cost[source[j:i]][target[j:i]]**

2. 但如果source[i] == target[i], 那我們就有另一個選擇是不換, 此時:

**dp[i] = dp[i-1] if source[i] == target[i]**

那cost[s][t]該怎麼求得?
結合original[i], changed[i], cost[i], 其實就是個有權重的directed graph
由於`1 <= cost.length == original.length == changed.length <= 100`, 所以我們可以用O(n^3)的Floyd-Warshall找出任意兩點的最短路徑(最小cost)

那這樣我們就能更新dp[i]了, 最終結果為dp[n] (1-indexed)

```py
dp = [inf] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    # case 1
    for s in dist:
        if i >= len(s) and source[i-len(s):i] in dist and target[i-len(s):i] in dist[source[i-len(s):i]]:
            dp[i] = min(dp[i], dp[i-len(s)] + dist[source[i-len(s):i]][target[i-len(s):i]])
    # case 2
    if source[i-1] == target[i-1]:
        dp[i] = min(dp[i], dp[i-1])
```

# Optimized

要再更加優化時間複雜度的話必須使用**Trie** ([詳細說明 by HuifengGuan](https://www.youtube.com/watch?v=pQ_gRovgx70))

```
source = XXXXX{XXXX}
               j  i
```

由於original.length <= 100, 所以我們從這裡面去找符合的source[j:i]跟target[j:i]很快
但有個更快的方式是我們`j`從後往前找回去, 持續檢查source[j:i]跟target[j:i]在不在Trie裡
一但不在那也不用再繼續往後找了, 可以直接break loop

整體框架會是

```py
dp = [inf] * (n+1)
dp[0] = 0
for i in range(1, n+1):
    # case 1
    root1 = root()
    root2 = root()
    for j in range(i, 0, -1):
        if source[j] not in root1: break
        if target[j] not in root2: break
        root1 = root1.next[source[j]]
        root2 = root2.next[target[j]]

        if root1.idx != -1 and root2.idx != -1:
            dp[i] = min(dp[i], dp[j-1] + dist[root1.idx][root2.idx])
    
    # for s in dist:
    #     if i >= len(s) and source[i-len(s):i] in dist and target[i-len(s):i] in dist[source[i-len(s):i]]:
    #         dp[i] = min(dp[i], dp[i-len(s)] + dist[source[i-len(s):i]][target[i-len(s):i]])
    
    # case 2
    if source[i-1] == target[i-1]:
        dp[i] = min(dp[i], dp[i-1])
```

```py
class TrieNode:
    def __init__(self):
        self.next = {}
        self.idx = -1

root = TrieNode()
MAP = dict()
idx = 0
for word in set(original + changed):
    MAP[word] = idx

    node = root
    # 由於我們substring是由後往前, source[j:i], target[j:i] where j from i to 1
    # 因此我們在建構Trie時也必須由後往前建構
    for ch in word[::-1]:
        if ch not in node.next:
            node.next[ch] = TrieNode()
        node = node.next[ch]
    node.id = idx

    idx += 1
```

dist[src][dst]也得改成dist[src.idx][dst.idx]
由於我們前面已經對original[i], changed[i]裡的string做上0-indexed的標記
所以floyd-warshall algorithm得改成:

```py
SET = set(source + changed)
m = len(SET)
dist = [[inf]*m for _ in range(m)]
for i in range(m):
    dist[i][i] = 0

for s, t, c in zip(original, changed, cost):
    dist[MAP[s]][MAP[t]] = min(dist[MAP[s]][MAP[t]], c)

for k in range(m):
    for i in range(m):
        for j in range(m):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
```
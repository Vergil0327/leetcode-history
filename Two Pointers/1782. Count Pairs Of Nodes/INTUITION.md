# Intuition

1 <= queries.length <= 20 => 這資料量特別小, 先特別記著說不定有能運用的地方

brute force: $O(n^2)$

```py
connEdges = defaultdict(set)
for i, (u, v) in enumerate(edges):
    connEdges[u].add(i)
    connEdges[v].add(i)

incidents = []
for i in range(1, n+1):
    for j in range(1, i):
        incidents.append(len(connEdges[i] | connEdges[j]))
incidents.sort()

return [len(incidents) - bisect_right(incidents, q) for q in queries]
```

其中還能再優化的是我們可以直接計數, 因為兩節點間會重複的邊就是他們倆之間有多少個相連的邊
ps. 這題的edges可能會有duplicates

```py
connected = defaultdict(int)
degrees = [0]*(n+1)
for i, (u, v) in enumerate(edges):
    connected[(min(u, v), max(u, v))] += 1
    degrees[u] += 1
    degrees[v] += 1

incidents = []
for i in range(1, n+1):
    for j in range(1, i):
        incidents.append(degrees[i] + degrees[j] - connected[j, i])
incidents.sort()

return [len(incidents) - bisect_right(incidents, q) for q in queries]
```

由於constraints:
- 2 <= n <= 2 * 10^4
- 1 <= edges.length <= 10^5

代表我們需要用接近O(n)的方式去計算, 那就是得看每個節點的貢獻度，然後再加總起來
對於節點`i`來說, 有多少個合法節點`j`是符合queries[k]要求的

這邊的突破口是, 如果我們先不考慮shared edges, 只希望找出`degrees[i] + degrees[j] > q`的話該怎麼做?
很直覺能想到的是我們可以先排序, 然後遍歷一遍用binary search找q-degrees[i]來找出合法的degrees[j]有哪些
或是先排序後用雙指針找出合法節點`j`

就像這樣:
- 先對degrees排序
- 雙指針, 遍歷`i`, 然後`j`從後往前單調移動
- 對於`i`來說, 有`n-j`個節點都可以跟`i`節點組成pair滿足count[i]+count[j] > q
- 一但i >= j, 代表`i`可以跟後面的`i+1`組成合法pair

```py
count = sorted(degrees)
valid = 0
j = n
for i in range(1, n+1):
    if i >= j:
        valid += n-i
        continue

    while j > i and count[i] + count[j] > q:
        j -= 1
    valid += n-j
```

那找完之後的valid數目, 還得再判斷有多少個(i,j) pair在扣掉shared edges後會不滿足**degrees[i] + degrees[j] - connected[j, i] > q**
所以我們在遍歷全部edges一遍, 我們已經找出**degrees[u] + degrees[v] > q**了
我們要扣掉的是那些扣除shared edges後就<= q的pairs, 所以:

```py
edgeCount = defaultdict(int)
for u, v in edges:
    edgeCount[min(u,v), max(u,v)] += 1

for u, v in edgeCount:
    if degrees[u] + degrees[v] > q and degrees[u] + degrees[v] - edgeCount[u,v] <= q:
        valid -= 1
```

扣除後即為答案

time: $O(nlogn + queries.size * (n + edges.size)))$
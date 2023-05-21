# Intuition

這題通過率只有8%, 一開始想到說用BFS來找最短路徑
那cost為`-1`的邊相當於未定權重, 我們可任意給定`[1,2*10^9]`內的值
因此想到是說那我們就全部給1, 最後一條前往`destination`給`target-cost_until_now`這樣

但很快就被這個case給擋住, 加上腦袋打結就這麼卡死在這邊
```
# test case 1
n = 4
edges = [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]]
source: 2
destination: 3
target: 8
```
這個test case指的是, 已經存在`source -> destination`的最短路徑, 其路徑為`7`
但我們要求的`target=8`, 代表我們在這題找到一個符合`target=8`的路徑(實際上確實找得到)
但他依舊不是最低權重的最短路徑, 因此這個test case應該返回`[]`

解決之後又很快的被這兩個test case給卡死

```
# test case 2
4
[[3,0,-1],[1,2,-1],[2,3,-1],[1,3,9],[2,0,5]]
0
1
7
```
這兩個test case說明的是, 如果我們存在著一個最短路徑
我們每個未定權重的邊, 亦即`cost = -1`的邊都給最低值`1`
如此一來`source -> destination`所需的最短距離依舊大於`target`的話
這時我們無法找到一個最短路徑等於`target`的路徑
因此應該一樣返回`[]`

```
# test case 3
5
[[0,2,5],[2,1,-1],[2,4,3],[3,4,5],[4,0,1],[0,3,-1],[2,3,-1]]
0
1
9
```
而再來這個test case則是說明

如我我們`source -> destination`存在著一條最短路徑, 且一路上有許多未定權重的邊及分岔
這實在最短路徑以外的值, 我們應該給定一個足夠大的權重使得我們不會走向分岔
這意味著我們應該紀錄我們的最短路徑是怎麼走的, 然後將最段路徑以外的未定權重都設為上限值`2 * 10**9`
因此我們需要一個**hashmap** `prev`來儲存我們走的路徑

綜合以上討論, 我們整個大框架為

1. 用dijkstra找出是不是已經存在一個最短路徑 (skip all the edges with `-1` weight)
   - 這邊要注意的是我們是從destination -> source找最短路徑
    ```py
    distReverse, _ = dijkstra(destination, graph, skip_negative=True)
    if distReverse[source] < target: return []
    ```
2. 用dijkstra判斷存不存在最短路徑 (所有未定權重的邊都賦值`1`)
    ```py
    dist, prev = dijkstra(source, graph, skip_negative=False)
    if dist[destination] > target: return []
    ```
3. 將最短路徑的總和已知必須為`target`, 將target分配在各個邊上. 並且將所有分岔且未定權重的邊都給定上限值`2 * 10**9`

透過dijkstra可還原我們的最短路徑
```py
path = [destination]
while path[-1] != source:
    path.append(prev[path[-1]])

path = path[::-1] # shortest path
```

再來是最重要的一步, 我們該如何分配target到我們的最短路徑`path`的每條邊上?

首先我們先存下每條邊的權重
```py
weight = defaultdict(lambda: defaultdict(lambda: -1))
for u,v,w in edges:
    weight[v][u] = weight[u][v] = w
```

再來我們儲存我們最短路徑當前已經分配了多少距離, 我們紀錄在`walked`這個變數裡
所以每次`walked`都會加上邊的全中, `walked += weight[u][v]`

那如果當前的邊應該分配多少呢?
首先知道的是當前我們能分配的距離有`target-walked`

那透過前面第一次dijkstra求的`distReverse`, 我們可以知道:
節點`v`走到終點所需的最短路徑是`distReverse[v]`
所以`u->v`這段邊應該為`target-walked-distReverse[v]`

```
總路徑長為`target`
到`u`為止的路徑為`walked`

X X X X -> u -> [v ->->-> destination]
 walked          這段路徑為distReverse[v]
```

那如果`distReverse[v]==inf`時, 代表後面這段距離尚未給定
這時我們就賦予當前的邊為`1`, 然後剩下的分配給後面的邊

```py
walked = 0
for i in range(len(path)-1):
    u, v = path[i], path[i+1]
    if weight[u][v] == -1:
        weight[v][u] = weight[u][v] = max(target-walked-distReverse[v], 1)
    walked += weight[u][v]
```

那最後我們weight[u][v]就存有所有`u -> v`的權重了
我們就將`weight`的結果更新回`edges[i][2]`即可

這時如果還存在著`weight[u][v] == -1`, 代表這條邊是我們不會走到的岔路
應該對這條邊給定一個上限值`2 * 10**9`

```py
for i in range(len(edges)):
    u,v = edges[i][0], edges[i][1]
    if weight[u][v] == -1:
        edges[i][2] = 2 * 10**9
    else:
        edges[i][2] = weight[u][v]
return edges
```
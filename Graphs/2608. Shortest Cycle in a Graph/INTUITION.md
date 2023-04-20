# DFS

## Intuition

這題一開始想到的是用DFS遍歷每個節點，然後我們可以用hashmap記錄走到每個節點時的size
如果我們走到一個節點他已經紀錄過size了，那代表我們找到一個環
此時環的起點終點正是我們當前的節點跟下一個節點，兩個size相減即得當前這個環的大小

```py
if cycle[nei] != -1: # found cycle
    self.res = min(self.res, cycle[node]+1-cycle[nei])
    continue
```

以下圖為例

```
0-1-2-3-4-5
|_ _|_ _ _|
```

當我們從0出發一路走到5再走回0後, 我們會找到第一個cycle
接下來當我們遍歷到從5往0走時，又會再次發現目標`cycle[nei] ！= -1`, 所以我們會在計算一次
但實際上這是相同的cycle只是方向相反, 所以這邊我們在更新`self.res`時，我們只要其中一個方向即可(或是取絕對值)

```py
if cycle[nei] != -1:
    if cycle[node] >= cycle[nei]:
        self.res = min(self.res, cycle[node]+1-cycle[nei])
    continue
# or
if cycle[nei] != -1:
    self.res = min(self.res, abs(cycle[node]-cycle[nei])+1)
    continue
```

再來有個很重要的點是
當初有想到說要用個`visited` hashset來記錄我們走過的節點
然後避免重複計算

但實際上不能這麼做，因為這會讓我們的DFS少算到某個情況
以這個例子來看
```
0-1-2-3-4-5
|_ _|_ _ _|
```
節點0他其實參與了兩個環, 0-1-2跟0-1-2-3-4-5
如果我們用個visited hashset紀錄的話，在當我們第一次走完0-1-2-3-4-5後
我們之後如果遍歷到i=2, 我們就會skip掉2-1-0這個環了

所以我們不能用

```py
visited = set()
for node in range(n):
    if node in visited: continue
    cycle = [-1] * n
    dfs(node, node, 0) # add node to `visited` in dfs
```

## Complexity
- time complexity
由於每個節點都要DFS一次
$$O(n^2)$$

# BFS

## Intuition

這題一開始想說要detect cycle所以直接想到了DFS配合hashset
但實際上這題要找的是最小size的環，所以我們其實用BFS會更快
一但我們BFS找到環，那麽這個環肯定是最小的環

那方法一樣是遍歷每個節點，然後用BFS來搜尋
然後我們可以用個hashset或是array來記錄走到當前節點時的size

大致框架如下:
```py
for node in range(n):
    queue = deque([node])
    prev = list(range(n))
    size = [inf] * n
    size[node] = 0
    foundCycle = False
    # start BFS
```

**初始狀態**
一開始位於起點時，size[node] = 0
然後我們把起點加入到queue裡
另外在用`foundCycle`作為flag
一但我們發現環，我們就設`foundCycle = True`, 然後一路跳出iteration

**那什麼情況下代表我們找到了環?**
觀察一下圖可發現，一樣，當我們發現下一個節點的size[neighbor_node] != inf時，代表我們發現了環
此時環的大小就是`size[node] + size[neighbor_node] + 1`

BFS的實作如下:

這邊要注意的是
我們在進行BFS時，我們一樣不希望我們走回頭路
所以我們額外用個`prev`array紀錄我們前一個節點是什麼
如果我們下個節點等同於我們的前一個節點，那我們就skip掉
相當於無向圖中的`dfs(node, prev)`
```py
def dfs(node, prev):
    for nei in graph[node]:
        if nei == prev: continue # <- 相當於這一行
```

### BFS
```py
while queue:
    for _ in range(len(queue)):
        node = queue.popleft()

        for nei in graph[node]:
            if prev[node] == nei: continue
            if size[nei] != inf:
                self.res = min(self.res, size[nei] + size[node] + 1)
                foundCycle = True
                break

            prev[nei] = node
            size[nei] = size[node]+1
            queue.append(nei)
        if foundCycle: break
    if foundCycle: break
```

# Other Solution - Still BFS

但其實這題有個更優雅的解法
不太好想，但如果知道了的話就非常簡單

首先我們有這麼這些`edges`
我們其實可以遍歷這些edges, 然後看當前的edges[i]有沒有參與環

位於`edges[i]`連接的兩個節點`u`跟`v`, 我們可以先斷開`edges[i]`這個邊然後用**BFS**來找出他的最短路徑
當我們找到最短路徑，此時再加上我們斷掉的邊，那就形成`u`, `v`兩節點間的最小的環
如果抵達不了, 代表這個邊沒有參與環
所以我們全部edges遍歷一遍並透過BFS找出每個最小環即可知道全局最小的環

high level的框架如下:

```py
graph = defaultdict(set)
for u, v in edges:
    graph[u].add(v)
    graph[v].add(u)

res = inf
for u, v in edges:
    # 斷掉當前這個edges[i]
    graph[u].remove(v)
    graph[v].remove(u)

    # 找出最小環的大小
    res = min(res, BFS(u, v))

    # 記得還原
    graph[u].add(v)
    graph[v].add(u)
return res if res != inf else -1
```

那BFS實作如下:
由於我們外層取`min()`, 所以如果找不到環, 那我們返回**inf**
如果找到, 那麼我們走的路徑再加上斷掉的那條邊(edges[i]), 就是環的大小
```py
def BFS(start, target):
    queue = deque([start])
    visited = set([start])

    step = 0
    while queue:
        for _ in range(len(queue)):
            node = queue.popleft()
            if node == target: return step+1 # steps+1 = cycle size
            for nei in graph[node]:
                if nei in visited: continue
                visited.add(nei)
                queue.append(nei)
        step += 1
    return inf
```
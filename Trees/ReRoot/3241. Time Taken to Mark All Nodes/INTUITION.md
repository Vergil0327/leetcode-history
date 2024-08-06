# Intuition

Brute Force還是比較好想的

遍歷每個節點作為起始點, 此時t=0
再來開始traverse tree, 看標記整棵樹需要多少時間
- 下個節點如果是奇數節點, 時間t, 那他的鄰接節點必須至少有一個在`t-1`時間已被標記
- 下個節點如果是偶數節點, 時間t, 那他的鄰接節點必須至少有一個在`t-2`時間已被標記

所以我們用dfs去遍歷的話:
- 下個鄰接節點如果是奇數, 那就可以直接標記並且時間`t+1`
- 下個鄰接節點如果是偶數, 那就必須等到`t+2`才可以標記

由於我們要的是標記所有節點的時間, 所以最終我們對時間取全局max, 即為當前節點`node`作為起點所需的標記時間

```py
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

time = [0]*(len(edges)+1)
def dfs(node, prev):
    t = 0
    for nxt in graph[node]:
        if nxt == prev: continue
        t = max(t, dfs(nxt, node) + (1 if nxt%2 == 1 else 2))
    return t

for node in range(len(edges)+1):
    time[node] = dfs(node, -1)
return time
```

上述時間複雜度為O(n^2), 從constraint來看`2 <= n <= 10^5`必須是O(n)時間才行
所以得想辦法優化時間複雜度

由於我們要遍歷每個節點作為起始點的所需時間, 直覺想到reroot感覺應該可行

用example3, 視覺化來看

```
    0
1       2
    3       4

定義subtree_time[from][to] = traverse_time

subtree_time[0] = [0, 1, 2]
subtree_time[1] = [0, 0, 0]
subtree_time[2] = [0, 0, 0]
```

其中subtree_time可以用dfs預處理

```py
subtree_time = [defaultdict(int) for _ in range(n)] # subtree_time[node][child]: time from node to other child node
def dfs(node, prev):
    t = 0
    for nxt in graph[node]:
        if nxt == prev: continue
        subtree_time[node][nxt] = dfs(nxt, node) + (1 if nxt%2 == 1 else 2)
        t = max(t, subtree_time[node][nxt])
    return t
```

有了subtree_time[node][nxt]這資訊後, 對於每個節點作為根節點, 我們可以透過對底下子樹所需的遍歷時間就是對每個路徑取max, 求出最長時間

```py
children_time = [[t, i] for i, t in subtree_time[node].items()]
children_time.sort(reverse=True)
longest_time = children_time[0][0] if children_time else 0
```

考慮完子樹後, 對於節點`node`來說, 就剩下父節點那條路徑的所需時間, 假設該時間為`time_parent`
那麼當前節點`node`所需的標記時間即為`time[node]=max(time_parent, longest_time)`

所以我們在re-root過程中, 我們從節點`node`轉移到`neighbor`時, 例如上面例子我們從node-0到node-2
我們僅需維護好`time_parent`, 而neighbor底下子樹所需時間則透過children_time排序即可知道

所以我們用上面例子來看, 利用re-root從node-0轉移到node-2時:
首先我們計算從node-2往node-0出發所需耗費的時間為: **1 if node-0%2 else 2**

再來對於node-2來說, `time_parent`就是往node-0遍歷的所需時間, 這時間為: `(1 if node-0%2 else 2) + max(subtree_time[neighbors of node-0 exclude node-2])`

也就是re-root過程中, 我們找出node的每個子節點所需時間(排除掉下個re-root的根節點), 取最大值後加上`1 if node-0%2 else 2`, 即為下個根節點的`time_parent`

那麽re-root後, 對於新的根節點求標記時間也是一樣, 可以透過`max(time_parent, children_time[0][0] if children_time else 0)`得知
所以reroot框架如下

```py
def reroot(node, prev, time_parent):
    # 計算根節點node的總遍歷時間, 子節點時間跟父節點時間取max
    children_time = [[t, i] for i, t in subtree_time[node].items()]
    children_time.sort(reverse=True)

    time[node] = max(time_parent, children_time[0][0] if children_time else 0)

    # 計算re-root後的time_parent
    for nxt in graph[node]:
        if nxt == prev: continue
        
        # 找出排除下個根節點nxt, node其他子節點的耗費時間取最大
        # 下個nxt節點的time_parent就是當前節點的max(time_parent, time_neighbor)再加上nxt->node的這段時間`1 if node%2 else 2`
        time_neighbor = 0
        if len(children_time) > 0:
            i = 0
            if children_time[i][1] == nxt:
                i += 1
            if i < len(children_time):
                time_neighbor = children_time[i][0]

        reroot(nxt, node, max(time_parent, time_neighbor) + (1 if node%2 else 2))
```


這邊要注意, 一開始subtree_time是用二維矩陣

```py
subtree_time = [[0]*n for _ in range(n)] # subtree_time[node][child]: time from node to other child node
```

但這樣後續計算children_time會超時, 而且實際上每個節點也不會有n個子節點, 所以用hashmap代替array會大幅降低運算時間
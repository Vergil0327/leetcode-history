# Intuition

這題難度分高達**3018**, 在`1 <= pairs.length <= 10^5`這限制下實在是毫無頭緒

- A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi.

ex.1 pairs = [[1,2],[2,3]]
只能是2 -> 1 & 3
不能是1 -> 2 -> 3, 這是因為沒有[1,3]pair讓1也是3的ancestor

ex. pairs=[[1,2],[2,3],[1,3]]

1-2現在要加入3:
如果只有[2,3]: 1-2-3, root=2, root.left=1, root.right=3
如果只有[1,3]: 3-1-2, root=1, root.left=3, root.right=2
如果同時有[2,3]跟[1,3], 3就必須是{1,2}的ancestor或child


```py
n = len(pairs)

connected = defaultdict(set)
for x, y in pairs:
    connected[x].add(y)
    connected[y].add(x)

for node in connected:
    try node as root
    此時:
    size = len(connected[node])
    有size個節點可以是node的children
    numAncestor = 0

    有len(connected) - 1 - size - numAncestor個節點不能是node的children => 不然就違反node as root => node is invalid
    那如果node可以作為root node, 那就再遍歷子節點看能不能作為root node of subtree
    for nei in connected[node]:
        recursion checkAsRoot(nei)

    所以這時會看到: 當子節點`nei`的len(connected[nei]) > len(connected[node])時, 代表該`node`是invalid root node, 因為肯定存在至少一個節點的ancestor不能是`node`
```

整體感覺必須透過recursion去一一檢查能不能建構出合法tree or subtree來
但即使如此, 也會是O(n^2)

```py
res = sum(checkAsRoot(node) for node in connected)
```

但我們這邊其實不用計算出詳細有多少合法建構方式, 所以我們可能要想的是能不能建構出**一個**或是**更多**就好

從前面觀察到len(connected[root])必須 **>=** len(connected[neighbor]), 否則root不合法
如果只是要看能不能建構出合法rooted tree的話, 用這條件應該能判斷出可以或不可以

想法是: 我們試著**greedily**的選擇max(len(connected[node]))作為root node, 這樣的話:
- 如果該node不合法, 那肯定就是0 valid root tree的狀況, 因為就算選擇其他作為root node, 那麼當該node作為neighbor時, 肯定存在len(connected[root]) < len(connected[node])的狀況
- 還有個比較難想到的是如果A, B兩節點的degree是相同的, len(connected[A]) == len(connected[B]), 那麼在建構的時候他們兩其實是可以試著互換然後看能不能成功建構出valid rooted tree的, ex. Root - A - B - ..., Root - B - A - ..., 那這樣就能在建構過程中就能利用這點來判斷是不是能建構1個以上的合法tree

但當初也沒能想到該如何去greedily選擇並試著確認是否能合法建構, 就卡在這了
因為如果有多個節點的degree都是max且相同的話, 那該怎辦? 假設對於root來說有三個neighbor的degree都是max那他們是該作為單鏈還是作為分支

但實際上想到這邊思路其實已經正確，只差後面檢驗了
這題解法是我們遍歷每個節點, 找出他的父節點
而他的父節點其實就是我們依照degree(edges count)由小到大排序之後, 第一個跟該節點有連接的節點

這是因為我們前面已經推論出, 作為一個合法rooted tree, 建構出來後從根節點一路往下, 他的degree一定是逐漸遞減的, 反之從任意node一路往上肯定是non-decreasing
所以我們在排序後, 從nodes[i]往後找, 所找到的第一個有相互連接的節點就是node[i]的父節點
那我們先把這關係存在`childred[nodes[i]]: [nodes[j], nodes[k], ...]`裡

```py
connected = defaultdict(list)
isConnected = [[False]*501 for _ in range(501)]
for x, y in pairs:
    connected[x].append(y)
    connected[y].append(x)
    isConnected[x][y] = True
    isConnected[y][x] = True

nodes = list(sorted(connected.keys(), key=lambda x: len(connected[x])))

n = len(nodes)
children = defaultdict(list)

flag = 1
root = None
for i in range(n):
    # find father of nodes[i]
    j = i+1
    while j < n and not isConnected[nodes[i]][nodes[j]]:
        j += 1
    if j < n:
        children[nodes[j]].append(nodes[i])
        if len(connected[nodes[i]]) == len(connected[nodes[j]]):
            flag = 2
    else:
        if root is None:
            root = nodes[i]
        else:
            return 0
```

後續我們再用dfs來檢驗該adjacency list `children`是不是合法rooted tree
確認方式就是`node`的子節點個數以及ancestors個數加總起來是不是等同於一開始題目所給的pairs數目

```py
visited = set()
def dfs(node, depth):
    nonlocal flag

    if flag == 0: return -1
    if node in visited: # cycle
        flag = 0
        return -1

    visited.add(node)
    childCnt = 0
    for child in children[node]:
        childCnt += dfs(child, depth+1)

    if childCnt+depth != len(connected[node]):
        flag = 0
        return -1
    return childCnt+1
dfs(root, 0)
return flag
```

總結一下:

這題必須先理解到從根節點一路往下, degrees只會遞減
因此我們依照degree由小到大排序後, 對於nodes[i]來說, 從i+1開始往後找到的第一個相連的節點就會是父節點
這樣就能一路找出adjacency list

然後再利用題目所給的pairs, 我們在用dfs檢驗是不是每個節點的pairs數目都跟我們得到的adjacency list相符

至於flag = 1 or 2, 則是看有沒有兩節點他們的degree是相同的情況發生
有的話就類似topological order那樣, 兩個degree相等, 在建構tree上可互換位置
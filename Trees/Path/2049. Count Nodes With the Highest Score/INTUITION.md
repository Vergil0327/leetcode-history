# Intuition

觀察一下會發現我們分數是這樣來的:

`score = left_subtree.size * right_subtree.size * (n-1-left_subtree.size-right_subtree.size) if value is non-zero value`

左子樹的大小 * 右子樹大小 * 上頭父子樹的大小，其中三者都不可為零
而父子樹的大小其實就是整棵樹的大小`n`減去左右子樹大小跟當前節點: `n-1-left_subtree.size-right_subtree.size`

那左右子樹的大小很好求，一個Post-order DFS即可求出，其中base case為抵達leaf node的時候返回零

leaf node: `len(children[node]) == 1 and children[node] == prev`

```py
def dfs(node, prev):
    nonlocal highest
    if len(children[node]) == 1 and children[node] == prev:
        return 0
    
    size = 0
    for child in children[node]:
        if child == prev: continue
        childSize = dfs(child, node)
        size += childSize
    
    return size + 1
dfs(0, -1)
```

而題目給的parent並不好使用，遞歸需要的是知道每個節點的子節點，因此可以把它轉成一般常用的adjacency list

```py
children = defaultdict(list)
for child, parent in enumerate(parents):
    if parent != -1:
        children[parent].append(child)
```

再來就是計算分數了

我們用一個變數`highest`來記錄最高分數，並且題目要求的是返回最高分的節點有幾個，因此在用一個hashmap `counter` 來存

在每次遞歸的時候，我們找出不為零的左右子樹大小以及父子樹的大小，存到`scores`裡

```py
def dfs:
    # ...

    size = 0
    scores = []
    for child in children[node]:
        if child == prev: continue
        childSize = dfs(child, node)
        if childSize > 0:
            scores.append(childSize)
        size += childSize

    parentSubtreeSize = n-1-size
    if parentSubtreeSize > 0:
        scores.append(parentSubtreeSize)
```

然後再計算當前節點的分數

```py
score = 1
for subscore in scores:
    score *= subscore
counter[score] += 1
highest = max(highest, score)
```

這樣dfs跑完後，我們要的結果也有了，就是`counter[highest]`

# Summary

if we remove current node, it'll split into `left_subtree`, `right_subtree`, `parent_subtree`,
and `parent_subtree.size = total_size - left_subtree.size - right_subtree.size - 1(current node)` 

thus, score = left_subtree.size * right_subtree.size * (n-1-left_subtree.size-right_subtree.size) if value is non-zero value

# Complexity

- time complexity
$$O(n)$$

- space complexity
$$O(n)$$
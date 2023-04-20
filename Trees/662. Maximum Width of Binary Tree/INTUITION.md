# Intuition

the width is the number of nodes at current level including None.
or we can say, width is `rightmost node's index - leftmost node's index`

therefore, we can tag index to each node by DFS and store in hashmap level by level

hashmap: {level: [index1, index2, ...]}
```py
def dfs(root, idx, level):
    if not root: return

    width[level].append(idx)
    dfs(root.left, 2*idx, level+1)
    dfs(root.right, 2*idx+1, level+1)
```

then we can iterate each level and use `max_index - min_index + 1` to get width
```py
res = 0
for arr in width.values():
    mx, mn = max(arr), min(arr)
    res = max(res, mx-mn+1)
```

# Optimization

since we use preorder DFS traversal, the array we store indexes at each level would be sorted in increasing order already.

thus,
```py
res = 0
for arr in width.values():
    res = max(res, arr[-1]-arr[0]+1)
```
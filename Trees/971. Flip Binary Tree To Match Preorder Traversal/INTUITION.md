# Intuition

由於voyage是preorder的我們要的順序，我們可以直接進行preorder dfs比對看看

如果最後dfs返回`True`, 代表我們能透過flip來獲得voyage
如果返回`False`, 代表我們不能透過flip來獲得voyage

high level的核心框架為:
```py
if dfs(root):
    return res # 儲存flip nodes
else:
    return [-1]
```

那接下來我們就依據題意來判斷需不需要進行flip

首先用一個global variable `self.i`來記錄我們目前preorder DFS要比對的是哪個voyage[self.i]

如果我們preorder到最後空節點，代表一切順利，返回`True`
如果`root.val != voyage[self.i]`，那返回`False`

那什麼時候要flip呢?
仔細想想條件非常直觀，如果我們的右節點等於下一個voyage[self.i+1]時，那我們就該flip, 所以:

```py
if root.right and root.right.val == voyage[self.i+1]:
    res.append(root.val) # bug here

    isLeftValid = dfs(root.right)
    isRightValid = dfs(root.left)
    return isLeftValid and isRightValid
```

如果不是，那就繼續常規preorder DFS

```py
else:
    left = dfs(root.left)
    right = dfs(root.right)

    return left and right
```

但上面第28行的`res.append(root.val)`其實是有誤的
想想這個case: root = [1,null,2], voyage = [1,2]

如果我們左節點為空時，其實我們並不需要flip
preorder DFS的順序一樣會跳過null而得到正確的voyage

因此上面應改為:

```py
if root.right and root.right.val == voyage[self.i+1]:
    if root.left:
        res.append(root.val) # now we are good

    isLeftValid = dfs(root.right)
    isRightValid = dfs(root.left)
    return isLeftValid and isRightValid
```

只有左節點存在時，我們才真正有翻轉到兩節點
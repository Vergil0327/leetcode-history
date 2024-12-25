# Intuition

遞歸去想, 首先對於整個preorder範圍[l,r]
當前node必定為preorder[l], 然後底下preorder[l+1, r]為子節點

所有preorder[i] < node.val的都會在左子樹, 如此一來就能得到:

```py
def dfs(l, r):
    if l > r: return None
    if l == r: return TreeNode(preorder[l])

    node = TreeNode(preorder[l])

    for i in range(l+1, r+1):
        if preorder[i] > node.val:
            node.left = dfs(l+1, i-1)
            node.right = dfs(i, r)
            return node
    return node
```

那麼如果是沒有右子樹的情況呢? ex. preorder = [4,2]
也就是如果我們遍歷`for i in range(l+1, r+1)`找不到分界點時, 那代表剩下的節點就都會是左子樹, 我們就依序形成子節點即可

```py
for i in range(l+1, r+1):
    if preorder[i] > node.val:
        node.left = dfs(l+1, i-1)
        node.right = dfs(i, r)
        return node
    
node.left = dfs(l+1, r)
return node
```

time: O(n^2)
space: O(n)
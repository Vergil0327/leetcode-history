# Intuition

首先判斷能不能刪的前提是root-to-leaf路徑和小於`limit`

所以我們用preorder dfs來記錄到當前為止的路徑和

- 一但抵達leaf node, 我們返回`accumulate_sum < limit`, 這樣一來我們便能在post-order的位置判斷左右子樹能不能刪除
- 那對於leaf node以外的節點, 他們能刪除的條件是左右子樹都能刪除的話, 那代表他也是位於在insufficient node的路徑上, 並且沒有跟其他合法路徑交集, 所以也可刪除
  - 所以對於其他節點, 我們返回`dfs(root.left, accu) and dfs(root.right, accu)`

那最後別忘了, 如果根節點的左右子樹都是insufficient, 那根節點本身也得刪除

```py
canDel = dfs(root, 0)
if canDel: return None
return root
```

# Other Solution

我們遞歸來看左右子樹, 當前的數值為root.val, 那代表左右子樹的和僅需滿足`limit - root.val`
再來一路遞歸到leaf node, 我們判斷看他是不是insufficient:
    - 如果leaf node的root.val < limit, 那代表可以刪除, 我們返回None
    - 如果leaf node的root.val >= limit, 代表合法
    ```py
    if not root.left and not root.right:
        return TreeNode(root.val) if root.val >= limit else None
    ```


那對於其他節點來說, 在post-order位置由於我們已經刪除所有insufficient node
如果左右節點都為空的話, 代表他沒有跟任何合法路徑有交集, 一樣可刪除
```py
if not root.left and not root.right:
            return None
        return root
```


```py
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return TreeNode(root.val) if root.val >= limit else None
        
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)
        if not root.left and not root.right:
            return None
        return root
```
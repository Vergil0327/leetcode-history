# Intuition

首先題目說所有給的trees[i]都是獨特的，然後看最後能不能全部合成一個大的BST

首先如果trees[i]有這些: {1,2,3,4,5,6} 作為最後大BST的possible roots
那每個trees[i]的leaf node為: { X, X, X, X, X, X, X, X, X, X, X}

如果最後要merge成一個BST，那麼possibles roots[i]跟leaves[i]必定能互相對應，然後最後只剩下一個possible roots[i]不出現在leaves裡

如果我們在possible roots裡找到一個以上不包含在leaf nodes裡的話，那這兩個最後也無法merge在一塊
所以可以直接返回 `None`

同時也代表，我們可以找到我們最後的根節點然後直接進行merge
這是最重要的一點

所以透過根節點跟葉子節點我們能找到最後的root
```py
possibleRoots = {}
leaves = set()
for tree in trees:
    possibleRoots[tree.val] = tree
    if tree.left:
        leaves.add(tree.left.val)
    if tree.right:
        leaves.add(tree.right.val)

roots = []
for root in possibleRoots.keys():
    if root not in leaves:
        roots.append(possibleRoots[root])
if len(roots) != 1: return None

root = roots[0]
```

再來進行merge就簡單了

我們進行preorder DFS, 每當我們走到葉子節點(左右子節點皆為None)時，我們就從possible roots裡找
如果有找到，那就merge，同時從hashmap中刪除
然後繼續遞歸下去

```py
def dfs(root):
    if not root: return root
    
    # leaf node
    if root and not root.left and not root.right:
        if root.val in possibleRoots:
            merge = possibleRoots[root.val]
            del possibleRoots[root.val]

            merge.left = dfs(merge.left)
            merge.right = dfs(merge.right)
            return merge
        return root

    root.left = dfs(root.left)
    root.right = dfs(root.right)
    return root
```

等到merge完後，possibleRoots應該只會剩下我們的根節點，其他都被刪除
如果還有其他不能merge的，那代表我們無法將全部合成一個BST，返回`None`

等到全部都merge完後，記得再檢查一下他是不是個合法的BST即可
```py
def isValidBST(root, l, r):
    if not root: return True

    if l < root.val < r:
        return isValidBST(root.left, l, root.val) and isValidBST(root.right, root.val, r)
    else:
        return False
```
例 Example 2, 就算能merge在一塊，但他並不是個合法BST
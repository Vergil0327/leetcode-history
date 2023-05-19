# Intuition

幾乎所有跟Tree有關的題目都可以用recursion來解, 因為Tree就是遞歸定義的結構
這題目標是要找出兩個root, 一個所有的數都大於`v`, 另一個則小於等於`v`

由於root是個BST, 我們可以用binary search來判斷每個節點

- 如果當下節點`root.val > v`, 代表整個右子樹都會是大於`v`的
所以這時我們的split位置就該往左邊找

- 反之如果`root.val <= v`, 那整個左子樹都會是小於`v`的, 這時我們的split位置又該往右邊找

那這題難點是我們split的位置是沿著`v`的位置垂直切一刀
如下圖, 我們沿著`v`垂直切一刀後, `8`這個節點屬於右半邊子樹, 必須接回去


```
v = 7

          10
        /   \
      2      12
     / \    /  \
    1   7  11    13
       / \
      6   8

becomes:
          10
        /   \
      8      12
            /  \
          11    13
  
      2
     / \
    1   7
       /
      6
```

所以我們在post-order DFS的位置

我們定義`dfs`返回`[<=v的root_node, >v的root_node]`

那麼**base case**就是當`root == None`時, 左右子樹都為`[Node, None]]`

而其他情況對於當前的根節點`root`來說:
- 如果`root.val > v`, 代表此時的根節點是歸屬在`>v`的Tree中
  - 此時他的`root.left = dfs(root.left)[1]`
  - 並且這時應該返回`[dfs(root.left)[0], root]`, 因為當前的root為下一輪遞歸時的所有數值大於`v`子樹的根節點

- 而當`root.val <= v`時, 此時根節點歸屬在`<=v`的Tree中
  - 此時他的`root.right = dfs(root.right)[0]`
  - 並且這時應該返回`[root, dfs(root.right)[1]]`, 因為當前節點為下一輪中, 所有數值`<=v`的根節點

相當於我們利用post-order以bottom-up的方式重新建構`>v`跟`<=v`兩棵樹

```
def dfs(root, v):
    if not root: return [None, None] # [<=v , >v]

    if root.val > v:
        l, r = dfs(root.left, v)
        root.left = r
        return [l, root]
    else:
        l, r = dfs(root.right, v)
        root.right = l
        return [root, r]
```

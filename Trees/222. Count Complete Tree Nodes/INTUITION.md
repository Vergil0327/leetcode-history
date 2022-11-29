## Binary Search

if we label every nodes from index `1` to `n`, just like `Example 1`,
we can use binary search to guess `how many nodes in this complete tree` since this binary tree is complete tree

- how to guess K if K is total number of nodes?
  1. if our label starts from 1 to n, we can see that:

        - left-child's index = root's index * 2
        - right-child's index = root's index * 2 + 1
        - then we can build a path from root to K by
      ```python
      k //= 2 -> k //= 2 -> ... -> root

      # left-child is 2*root.val
      # right-child is 2*root.val+1
      pathToK = []
      while k > 0:
          pathToK.append(k)
          k //= 2
      ```
  2. check if there is a path from root to K based on path of K-to-root
     
     - pathToK[-1] should be root if root not None
     - so we can iterate pathToK reversely to check if K exists or not

        ```python
        # starts from root (pathToK[-1])
        for i in range(len(pathToK), -1, -1):
          if not root: return False # tree's last index < K
          if i == 0: return True # found K

          if pathToK[i-1] == 2 * pathToK[i]: # goes from root from current to left node
            root = root.left
          else: # goes from current to right node
            root = root.right
        ```

then we can use our guess function to do binary search.

search space should start from `left-most index at level of max height` to `right-most index at level of max height`

since max height of complete tree can easily be found by:
```python
h = 0
curr = root
while curr:
    h += 1
    curr = curr.left
```

so our search space should be `[2**(h-1), 2**h-1]`
and we can start our binary search

## Recursion, Divide & Conquer

for complete binary tree, we can keep finding if left subtree is a complete tree or not

- if right subtree's height == left subtree's height, left subtree must be a complete tree

therefore,
hLeft = left subtree's max height
hRight = right subtree's maxheight
- if `hLeft == hRight`, left subtree is complete and keep finding right subtree
  - `count += 2**hLeft - 1`
- if `hLeft != hRight`, right subtree is complete and keep finding left subtree
  - `count += 2**hRight - 1`

```
 1
2 3

hLeft = 1
hRight = 1
count = 1(root) + 1 + dfs(root.right) = 1 + 1 + 1
```

```
  1
 2 
hLeft = 1
hRight = 0
count = 1(root) + 2**0-1 + dfs(root.left)
      = 1 + 0 + (1 + 0 + 0)
      = 2
```

### More Elegant Recursion Solution

[來源](https://labuladong.github.io/algo/2/21/48/)

首先要明確一下兩個關於二叉樹的名詞「完全二叉樹」和「滿二叉樹」。

我們說的完全二叉樹如下圖，每一層都是緊湊靠左排列的：


我們說的滿二叉樹如下圖，是一種特殊的完全二叉樹，每層都是是滿的，像一個穩定的三角形：

     o
   o   o
  o o o o


說句題外話，關於這兩個定義，中文語境和英文語境似乎有點區別，我們說的完全二叉樹對應英文 Complete Binary Tree，沒有問題。但是我們說的滿二叉樹對應英文 Perfect Binary Tree，而英文中的 Full Binary Tree 是指一棵二叉樹的所有節點要麽沒有子節點，要麽有兩個子節點。

以上定義出自 wikipedia，這里就是順便一提，其實名詞叫什麽都無所謂，重要的是算法操作。本文就按我們中文的語境，記住「滿二叉樹」和「完全二叉樹」的區別，等會會用到。

一、思路分析
現在回歸正題，如何求一棵完全二叉樹的節點個數呢？

// 輸入一棵完全二叉樹，返回節點總數
int countNodes(TreeNode root);
如果是一個普通二叉樹，顯然只要向下面這樣遍歷一邊即可，時間複雜度 O(N)：

```java
public int countNodes(TreeNode root) {
    if (root == null) return 0;
    return 1 + countNodes(root.left) + countNodes(root.right);
}
```

那如果是一棵滿二叉樹，節點總數就和樹的高度呈指數關系：

```java
public int countNodes(TreeNode root) {
    int h = 0;
    // 計算樹的高度
    while (root != null) {
        root = root.left;
        h++;
    }
    // 節點總數就是 2^h - 1
    return (int)Math.pow(2, h) - 1;
}
```

完全二叉樹比普通二叉樹特殊，但又沒有滿二叉樹那麽特殊，計算它的節點總數，可以說是普通二叉樹和完全二叉樹的結合版，先看代碼：

``` java
public int countNodes(TreeNode root) {
    TreeNode l = root, r = root;
    // 沿最左側和最右側分別計算高度
    int hl = 0, hr = 0;
    while (l != null) {
        l = l.left;
        hl++;
    }
    while (r != null) {
        r = r.right;
        hr++;
    }
    // 如果左右側計算的高度相同，則是一棵滿二叉樹
    if (hl == hr) {
        return (int)Math.pow(2, hl) - 1;
    }
    // 如果左右側的高度不同，則按照普通二叉樹的邏輯計算
    return 1 + countNodes(root.left) + countNodes(root.right);
}
```

結合剛才針對滿二叉樹和普通二叉樹的算法，上面這段代碼應該不難理解，就是一個結合版，但是其中降低時間複雜度的技巧是非常微妙的。

二、複雜度分析
開頭說了，這個算法的時間複雜度是 O(logN*logN)，這是怎麽算出來的呢？

直覺感覺好像最壞情況下是 O(N*logN) 吧，因為之前的 while 需要 logN 的時間，最後要 O(N) 的時間向左右子樹遞歸：

return 1 + countNodes(root.left) + countNodes(root.right);
關鍵點在於，這兩個遞歸只有一個會真的遞歸下去，另一個一定會觸發 hl == hr 而立即返回，不會遞歸下去。

為什麽呢？原因如下：

一棵完全二叉樹的兩棵子樹，至少有一棵是滿二叉樹：
(左為完全二叉樹, 右為滿二叉樹)
        o
    o       o
  o   o   o   o
 o o 

 (左為滿二叉樹, 右為完全二叉樹)
        o
    o       o
  o   o   o   o
 o o o o o

看圖就明顯了吧，由於完全二叉樹的性質，其子樹一定有一棵是滿的，所以一定會觸發 hl == hr，只消耗 O(logN) 的複雜度而不會繼續遞歸。

綜上，算法的遞歸深度就是樹的高度 O(logN)，每次遞歸所花費的時間就是 while 循環，需要 O(logN)，所以總體的時間複雜度是 O(logN*logN)。

所以說，「完全二叉樹」這個概念還是有它存在的原因的，不僅適用於數組實現二叉堆，而且連計算節點總數這種看起來簡單的操作都有高效的算法實現。
[230. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

`Medium`

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

```
Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

Constraints:

- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

<details>
<summary>explanaiton</summary>

[尋找第 K 小的元素](https://labuladong.github.io/algo/2/21/42/)

`如果让你实现一个在二叉搜索树中通过排名计算对应元素的方法 select(int k)，你会怎么设计？`

如果按照我们刚才说的方法，利用「BST 中序遍历就是升序排序结果」这个性质，每次寻找第 k 小的元素都要中序遍历一次，最坏的时间复杂度是 O(N)，N 是 BST 的节点个数。

要知道 BST 性质是非常牛逼的，像红黑树这种改良的自平衡 BST，增删查改都是 O(logN) 的复杂度，让你算一个第 k 小元素，时间复杂度竟然要 O(N)，有点低效了。

所以说，计算第 k 小元素，最好的算法肯定也是对数级别的复杂度，不过这个依赖于 BST 节点记录的信息有多少。

我们想一下 BST 的操作为什么这么高效？就拿搜索某一个元素来说，BST 能够在对数时间找到该元素的根本原因还是在 BST 的定义里，左子树小右子树大嘛，所以每个节点都可以通过对比自身的值判断去左子树还是右子树搜索目标值，从而避免了全树遍历，达到对数级复杂度。

那么回到这个问题，想找到第 k 小的元素，或者说找到排名为 k 的元素，如果想达到对数级复杂度，关键也在于每个节点得知道他自己排第几。

比如说你让我查找排名为 k 的元素，当前节点知道自己排名第 m，那么我可以比较 m 和 k 的大小：

1、如果 m == k，显然就是找到了第 k 个元素，返回当前节点就行了。

2、如果 k < m，那说明排名第 k 的元素在左子树，所以可以去左子树搜索第 k 个元素。

3、如果 k > m，那说明排名第 k 的元素在右子树，所以可以去右子树搜索第 k - m - 1 个元素。

这样就可以将时间复杂度降到 O(logN) 了。

那么，如何让每一个节点知道自己的排名呢？

这就是我们之前说的，需要在二叉树节点中维护额外信息。每个节点需要记录，以自己为根的这棵二叉树有多少个节点。

也就是說，我們 TreeNode 中的實作應為如下：

```python
class TreeNode:
  def __init__(self, val, size, left, right):
      self.val = val
      self.size = size # 以該節點為根的節點總數
      self.left = left
      self.right = right
```
</details>
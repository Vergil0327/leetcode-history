[865. Smallest Subtree with all the Deepest Nodes](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/)

`Medium`

Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is a tree consisting of that node, plus the set of all descendants of that node.


```
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation: We return the node with value 2, colored in yellow in the diagram.
The nodes coloured in blue are the deepest nodes of the tree.
Notice that nodes 5, 3 and 2 contain the deepest nodes in the tree but node 2 is the smallest subtree among them, so we return it.

Example 2:
Input: root = [1]
Output: [1]
Explanation: The root is the deepest node in the tree.

Example 3:
Input: root = [0,1,3,null,2]
Output: [2]
Explanation: The deepest node in the tree is 2, the valid subtrees are the subtrees of nodes 2, 1 and 0 but the subtree of node 2 is the smallest.
```

Constraints:

- The number of nodes in the tree will be in the range [1, 500].
- 0 <= Node.val <= 500
- The values of the nodes in the tree are unique.
 

Note: This question is the same as [leetcode 1123](https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/)

<details>
<summary>Solution</summary>

基本思路
前文 [手把手刷二叉树总结篇](https://labuladong.github.io/article/fname.html?fname=%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93) 说过二叉树的递归分为「遍历」和「分解问题」两种思维模式，这道题需要用到「分解问题」的思维，而且涉及处理子树，需要用后序遍历。

说到底，这道题就是让你求那些「最深」的叶子节点的最近公共祖先，可以看下前文 [二叉树最近公共祖先](https://appktavsiei5995.pc.xiaoe-tech.com/detail/i_62987959e4b01a4852072fa5/1)。

你想想，一个节点需要知道哪些信息，才能确定自己是最深叶子节点的最近公共祖先？

它需要知道自己的左右子树的最大深度：如果左右子树一样深，那么当前节点就是最近公共祖先；如果左右子树不一样深，那么最深叶子节点的最近公共祖先肯定在左右子树上。

所以我们新建一个 Result 类，存放左右子树的最大深度及叶子节点的最近公共祖先节点，其余逻辑类似 [104. 二叉树的最大深度](https://leetcode.com/problems/maximum-depth-of-binary-tree)。

```java
class Solution {
    class Result {
        public TreeNode node;
        public int depth;

        public Result(TreeNode node, int depth) {
            // 记录最近公共祖先节点 node
            this.node = node;
            // 记录以 node 为根的二叉树最大深度
            this.depth = depth;
        }
    }

    public TreeNode lcaDeepestLeaves(TreeNode root) {
        Result res = maxDepth(root);
        return res.node;
    }

    // 定义：输入一棵二叉树，返回该二叉树的最大深度以及最深叶子节点的最近公共祖先节点
    Result maxDepth(TreeNode root) {
        if (root == null) {
            return new Result(null, 0);
        }
        Result left = maxDepth(root.left);
        Result right = maxDepth(root.right);
        if (left.depth == right.depth) {
            // 当左右子树的最大深度相同时，这个根节点是新的最近公共祖先
            return new Result(root, left.depth + 1);
        }
        // 左右子树的深度不同，则最近公共祖先在 depth 较大的一边
        Result res = left.depth > right.depth ? left : right;
        // 正确维护二叉树的最大深度
        res.depth++;

        return res;
    }
}
```
</details>

<details>
<summary>Other Solution with Explanation</summary>

[HuifengGuan](https://www.youtube.com/watch?v=DUXvcoEZJqw)
</details>
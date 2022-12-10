[1339. Maximum Product of Splitted Binary Tree](https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/)

`Medium`

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

```
Example 1:
Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:
Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
```

Constraints:

- The number of nodes in the tree is in the range [2, 5 * 10^4].
- 1 <= Node.val <= 10^4

<details>
<summary>Hint</summary>

If we know the sum of a subtree, the answer is max( (total_sum - subtree_sum) * subtree_sum) in each node.
</details>

<details>
<summary>Chinese Explanation</summary>

这里要用到前文 [手把手刷二叉树总结篇](https://labuladong.github.io/article/fname.html?fname=%E4%BA%8C%E5%8F%89%E6%A0%91%E6%80%BB%E7%BB%93) 说过的后序位置的妙用。

题目说的比较繁琐，这道题说的简单些就是：

在二叉树中切出一个小二叉树（子树），计算这个子树节点之和与剩下的节点之和的乘积。

想求最大乘积，那就穷举，把所有可能的切法都穷举一遍，计算乘积。

任何子树的节点之和都可以在后序位置获得，而剩下的其他节点之和就是整棵二叉树的节点之和减去子树节点之和。

所以我们写一个 getSum 函数，先执行一遍计算整棵树的节点之和，然后再调用一次利用它的后序位置计算乘积。

```java
class Solution {
    public int maxProduct(TreeNode root) {
        // 先利用求和函数得到整棵树的节点之和
        treeSum = getSum(root);
        // 再次调用，利用后序位置计算子树之积
        getSum(root);
        return (int) (res % (1e9 + 7));
    }

    long res = 0;
    int treeSum = 0;

    int getSum(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int leftSum = getSum(root.left);
        int rightSum = getSum(root.right);
        int rootSum = leftSum + rightSum + root.val;
        // 后序位置计算乘积
        res = Math.max(res, (long) rootSum * (treeSum - rootSum));
        return rootSum;
    }
}
```
</details>
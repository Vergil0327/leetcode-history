[95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/)

`Medium`

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

```
Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]
```

Constraints:

- 1 <= n <= 8

<details>
<summary>Solution with explanation - 1</summary>

基本思路
类似 96. 不同的二叉搜索树，这题的思路也是类似的，想要构造出所有合法 BST，分以下三步：

1、穷举 root 节点的所有可能。

2、递归构造出左右子树的所有合法 BST。

3、给 root 节点穷举所有左右子树的组合。

```java
class Solution {
    /* 主函数 */
    public List<TreeNode> generateTrees(int n) {
        if (n == 0) return new LinkedList<>();
        // 构造闭区间 [1, n] 组成的 BST
        return build(1, n);
    }

    /* 构造闭区间 [lo, hi] 组成的 BST */
    List<TreeNode> build(int lo, int hi) {
        List<TreeNode> res = new LinkedList<>();
        // base case
        if (lo > hi) {
            res.add(null);
            return res;
        }

        // 1、穷举 root 节点的所有可能。
        for (int i = lo; i <= hi; i++) {
            // 2、递归构造出左右子树的所有合法 BST。
            List<TreeNode> leftTree = build(lo, i - 1);
            List<TreeNode> rightTree = build(i + 1, hi);
            // 3、给 root 节点穷举所有左右子树的组合。
            for (TreeNode left : leftTree) {
                for (TreeNode right : rightTree) {
                    // i 作为根节点 root 的值
                    TreeNode root = new TreeNode(i);
                    root.left = left;
                    root.right = right;
                    res.add(root);
                }
            }
        }
        return res;
    }
}
// 详细解析参见：
// https://labuladong.github.io/article/?qno=95
```
</details>

<details>
<summary>Solution with explanation - 2</summary>

[Huifeng Guan](https://github.com/wisdompeak/LeetCode/tree/master/Tree/095.Unique-Binary-Search-Trees-II)
</details>

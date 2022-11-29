[2096. Step-By-Step Directions From a Binary Tree Node to Another](https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/)

`Medium`

You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. You are also given an integer startValue representing the value of the start node s, and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. Generate step-by-step directions of such path as a string consisting of only the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

```
Example 1:
Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

Example 2:
Input: root = [2,1], startValue = 2, destValue = 1
Output: "L"
Explanation: The shortest path is: 2 → 1.
```

Constraints:

- The number of nodes in the tree is n.
- 2 <= n <= 10^5
- 1 <= Node.val <= n
- All the values in the tree are unique.
- 1 <= startValue, destValue <= n
- startValue != destValue

<details>
<summary>Hint 1</summary>

The shortest path between any two nodes in a tree must pass through their Lowest Common Ancestor (LCA). The path will travel upwards from node s to the LCA and then downwards from the LCA to node t.
</details>

<details>
<summary>Hint 2</summary>

Find the path strings from root → s, and root → t. Can you use these two strings to prepare the final answer?
</details>

<details>
<summary>Hint 3</summary>

Remove the longest common prefix of the two path strings to get the path LCA → s, and LCA → t. Each step in the path of LCA → s should be reversed as 'U'.
</details>

<details>
<summary>Solution 1</summary>

基本思路
这题的思路比较巧妙，主要分三步：

1、分别记录从根节点到 startValue 和 destValue 的路径 startPath 和 destPath。

2、然后去除 startPath 和 destPath 的公共前缀。

3、最后将 startPath 全部变成 U，把 startPath 和 destPath 接在一起，就是题目要求的路径了。

```java
class Solution {
    public String getDirections(TreeNode root, int startValue, int destValue) {
        this.startValue = startValue;
        this.destValue = destValue;
        // 寻找走到 startValue 和 destValue 的方向路径
        traverse(root);
        // 去除两个方向路径的公共前缀
        int p = 0, m = startPath.length(), n = destPath.length();
        while (p < m && p < n
                && startPath.charAt(p) == destPath.charAt(p)) {
            p++;
        }
        startPath = startPath.substring(p);
        destPath = destPath.substring(p);
        // 将走向 startValue 的方向路径全部变成 U
        startPath = "U".repeat(startPath.length());
        // 组合 startPath 和 destPath 就得到了答案
        return startPath + destPath;
    }

    StringBuilder path = new StringBuilder();
    String startPath, destPath;
    int startValue, destValue;

    // 二叉树遍历函数
    void traverse(TreeNode root) {
        if (root == null) {
            return;
        }
        if (root.val == startValue) {
            startPath = path.toString();
        } else if (root.val == destValue) {
            destPath = path.toString();
        }

        // 二叉树遍历框架
        path.append('L');
        traverse(root.left);
        path.deleteCharAt(path.length() - 1);

        path.append('R');
        traverse(root.right);
        path.deleteCharAt(path.length() - 1);
    }
}
```
</details>

<details>
<summary>Solution 2 with Video Explanation</summary>

[HuifengGuan](https://www.youtube.com/watch?v=VvdlzPAQE0s)
</details>
[652. Find Duplicate Subtrees](https://leetcode.com/problems/find-duplicate-subtrees/)

`Medium`

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

```
Example 1:
Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]

Example 2:
Input: root = [2,1,1]
Output: [[1]]

Example 3:
Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
```

Constraints:

- The number of the nodes in the tree will be in the range [1, 5000]
- -200 <= Node.val <= 200

<details>
<summary>Hint</summary>

think [Leetcode 297](../297.%20Serialize%20and%20Deserialize%20Binary%20Tree/)

maybe we can serialize each subtree for us to compare?
</details>

<details>
<summary>Explanation</summary>

[東 哥](https://labuladong.github.io/algo/2/21/40/)
[HuifengGuan 每日一題](https://www.youtube.com/watch?v=YupKiFqtnsA)
</details>
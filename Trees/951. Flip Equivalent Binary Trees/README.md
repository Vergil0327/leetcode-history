[951. Flip Equivalent Binary Trees](https://leetcode.com/problems/flip-equivalent-binary-trees/)

`Medium`

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.

```
Example 1:
Flipped Trees Diagram
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.

Example 2:
Input: root1 = [], root2 = []
Output: true

Example 3:
Input: root1 = [], root2 = [1]
Output: false
```

Constraints:

- The number of nodes in each tree is in the range [0, 100].
- Each tree will have unique node values in the range [0, 99].

<details>
<summary>Canonical Traversal Solution</summary>

Approach 2: Canonical Traversal
Intuition

Flip each node so that the left child is smaller than the right, and call this the canonical representation. All equivalent trees have exactly one canonical representation.

Algorithm

We can use a depth-first search to compare the canonical representation of each tree. If the traversals are the same, the representations are equal.

When traversing, we should be careful to encode both when we enter or leave a node.



```python
class Solution:
    def flipEquiv(self, root1, root2):
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'

        return all(x == y for x, y in itertools.zip_longest(
            dfs(root1), dfs(root2)))
```

```java
class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        List<Integer> vals1 = new ArrayList();
        List<Integer> vals2 = new ArrayList();
        dfs(root1, vals1);
        dfs(root2, vals2);
        return vals1.equals(vals2);
    }

    public void dfs(TreeNode node, List<Integer> vals) {
        if (node != null) {
            vals.add(node.val);
            int L = node.left != null ? node.left.val : -1;
            int R = node.right != null ? node.right.val : -1;

            if (L < R) {
                dfs(node.left, vals);
                dfs(node.right, vals);
            } else {
                dfs(node.right, vals);
                dfs(node.left, vals);
            }

            vals.add(null);
        }
    }
}
```
</details>
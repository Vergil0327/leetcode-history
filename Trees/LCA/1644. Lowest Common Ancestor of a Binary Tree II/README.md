[1644. Lowest Common Ancestor of a Binary Tree II](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/)

`Medium`

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

```
Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.

Example 3:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
```

Constraints:

- The number of nodes in the tree is in the range [1, 10^4].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q

<details>
<summary>Solution</summary>

[Huifeng Guan](https://www.youtube.com/watch?v=337pBcXDE1k)

Other solution
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Node不一定在树里，当root == p or root == q必须后序遍历判断
        dfs() 除了返回当前节点外，还返回是否存在
        
        Time: O(N)
        Space: O(N)
        """
        def dfs(root):
            if not root:
                return None, False
            
            left, l_exist = dfs(root.left)
            right, r_exist = dfs(root.right)
            
            if root == p or root == q:
                return root, left or right
            
            if left and right:
                return root, True
            else:
                if left:
                    return left, l_exist
                else:
                    return right, r_exist
                 
        lca, exist = dfs(root)
        if not exist:
            return None
        return lca
```
</details>
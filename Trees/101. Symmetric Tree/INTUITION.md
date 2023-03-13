# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Compare symmetric position of left subtree and right subtree at each recursion/iteration

As for root node, its symmetric node is itself

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

# Code
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, root)]
        while stack:
            left, right = stack.pop()
            if not left and not right: continue
            if not left:
                if right: return False
            if not right:
                if left: return False
            
            if left.val != right.val: return False
            if left:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
        return True
            
        def dfs(root, other):
            if not root: return not other
            if not other: return not root

            isSymL = dfs(root.left, other.right)
            isSymR = dfs(root.right, other.left)
            
            return isSymL and isSymR and root.val == other.val

        return dfs(root, root)
```
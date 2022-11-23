# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, l, r):
            if not root: return l < r
            return l < root.val < r and dfs(root.left, l, root.val) and dfs(root.right, root.val, r)
        
        return dfs(root, -inf, inf)

# [5,4,6,null,null,3,7]
#     5
#    4 6
# n, n, 3, 7
# ! wrong definition, it doesn't compare left subtree with right subtree
class WrongSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        
        validLeft = root.left.val < root.val if root.left else True
        validRight = root.val < root.right.val if root.right else True
        
        self.isValidBST(root.left)
        self.isValidBST(root.right)
        
        return validLeft and validRight
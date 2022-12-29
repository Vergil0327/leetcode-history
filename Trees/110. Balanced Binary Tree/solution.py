# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root: return 0, True

            left, isLeftBalanced = height(root.left)
            right, isRightBalanced = height(root.right)
            isBalance = abs(left-right) <= 1
            if not isBalance or not isLeftBalanced or not isRightBalanced:
                return max(left, right)+1, False
            else:
                return max(left, right)+1, True
        return height(root)[1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        LEFT, RIGHT = 0, 1
        self.res = 0
        def dfs(root, direct):
            if not root: return 0

            left = dfs(root.left, LEFT)
            right = dfs(root.right, RIGHT)
            self.res = max(self.res, left, right)
            
            if direct == LEFT:
                return 1+right
            elif direct == RIGHT:
                return 1+left
            else:
                return max(left+1, right+1)

        dfs(root, -1)
        return self.res

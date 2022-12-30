# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []
        def dfs(state, root, base):
            if not root: return
            if root and not root.left and not root.right:
                nums.append(state * base + root.val)
                return
            
            nxt = state * base + root.val
            dfs(nxt, root.left, base)
            dfs(nxt, root.right, base)
        dfs(0, root, 10)

        return sum(nums)
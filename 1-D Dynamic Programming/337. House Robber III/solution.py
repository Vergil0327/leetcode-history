# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# explanation: https://www.youtube.com/watch?v=nHR8ytpzz7c&ab_channel=NeetCode
# O(n)
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # returns: [ max with root, max without root]
        def dfs(root):
          if not root: return [0, 0]
          
          left = dfs(root.left)
          right = dfs(root.right)

          return [root.val+left[1]+right[1], max(left)+max(right)]
        return max(dfs(root))

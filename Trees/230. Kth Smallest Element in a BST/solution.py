# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            nonlocal k
            if not root: return -1
            
            v = dfs(root.left)
            if v != -1: return v
            
            if k-1 == 0:
                return root.val
            k -= 1
            
            v = dfs(root.right)
            if v != -1: return v
            return -1

        return dfs(root)

class IterativeSolution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
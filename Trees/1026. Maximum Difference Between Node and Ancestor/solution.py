# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        currMax = currMin = root.val
        diff = 0
        def dfs(root, currMax, currMin):
            nonlocal diff
            if not root: return currMax

            if root.val > currMax:
                currMax = root.val
            if root.val < currMin:
                currMin = root.val
            left = dfs(root.left, currMax, currMin)
            right = dfs(root.right, currMax, currMin)
            
            diff = max(diff, currMax-left, currMax-right)
            diff = max(diff, left-currMin, right-currMin)

            return root.val
        dfs(root, currMax, currMin)
        return diff
    
# Concise
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mx, mn):
            if not node: return 0

            res = 0
            mx, mn = max(mx, node.val), min(mn, node.val)
            if node.left:
                x = abs(mx-node.left.val)
                y = abs(mn-node.left.val)
                z = dfs(node.left, mx, mn)
                res = max(res, x, y, z)
            if node.right:
                x = abs(mx-node.right.val)
                y = abs(mn-node.right.val)
                z = dfs(node.right, mx, mn)
                res = max(res, x, y, z)
            return res
        return dfs(root, root.val, root.val)
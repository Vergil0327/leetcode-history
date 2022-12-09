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
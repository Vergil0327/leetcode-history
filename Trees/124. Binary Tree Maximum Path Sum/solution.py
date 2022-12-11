class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -inf
        def dfs(root):
            nonlocal maxSum
            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)
            maxSum = max(maxSum, root.val + max(0, left) + max(0, right))

            return root.val + max(left, right, 0)

        dfs(root)
        return maxSum
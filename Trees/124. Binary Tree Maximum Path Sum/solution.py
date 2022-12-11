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

# Without Global Variable
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0, -inf

            left, left_max_path_sum = dfs(root.left)
            right, right_max_path_sum = dfs(root.right)
            curr_max_path_sum = root.val + max(0, left) + max(0, right)
            maxSum = max(left_max_path_sum, right_max_path_sum, curr_max_path_sum)

            return root.val + max(left, right, 0), maxSum

        _, maxSum = dfs(root)
        return maxSum
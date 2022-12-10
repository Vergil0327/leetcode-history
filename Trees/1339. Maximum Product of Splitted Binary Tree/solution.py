class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 1000000000+7
        def treesum(root):
            if not root: return 0
            return root.val + treesum(root.left) + treesum(root.right)
        total = treesum(root)

        maxProd = 0
        def dfs(root):
            nonlocal maxProd
            if not root: return 0

            left, right = dfs(root.left), dfs(root.right)
            maxProd = max(maxProd, left * (total-left), right * (total-right))
            return root.val + left + right
        dfs(root)
        return maxProd % MOD
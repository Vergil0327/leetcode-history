# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            if not node: return 0, inf, -inf

            if node.left is None and node.right is None:
                self.res = max(self.res, node.val)

            totL, minL, maxL = dfs(node.left)
            totR, minR, maxR = dfs(node.right)

            if maxL < node.val < minR:
                tot = totL+totR+node.val
                self.res = max(self.res, tot)
                return (tot,
                        min(minL, node.val),
                        max(maxR, node.val))
            else:
                return -inf, inf, -inf

        dfs(root)
        return self.res
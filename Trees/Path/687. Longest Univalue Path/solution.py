# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0
        def dfs(root):
            nonlocal longest
            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)
            candidates = []
            if root.left and root.left.val == root.val:
                candidates.append(left)
            if root.right and root.right.val == root.val:
                candidates.append(right)
            candidates.sort(reverse=True)
            longest = max(longest, sum(candidates[:2]))
            return (candidates[0]+1) if candidates else 1

        dfs(root)
        return longest

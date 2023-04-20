# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # { level: width }

        width = defaultdict(list)
        def dfs(root, idx, level):
            if not root: return

            width[level].append(idx)
            dfs(root.left, 2*idx, level+1)
            dfs(root.right, 2*idx+1, level+1)
        dfs(root, 1, 0)

        res = 0
        for arr in width.values():
            # mx, mn = max(arr), min(arr)
            # res = max(res, mx-mn+1)
            res = max(res, arr[-1]-arr[0]+1)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:        
        res = 0
        # 0: leaf node
        # 1: leaf node's parent => has camera
        # 2: covered by camera
        LEAF, CAMERA, COVERED = 0, 1, 2
        def dfs(node):
            nonlocal res
            if not node: return COVERED

            left = dfs(node.left)
            right = dfs(node.right)

            if left == LEAF or right == LEAF:
                res += 1
                return CAMERA
            
            if left == CAMERA or right == CAMERA:
                return COVERED
            else:
                return LEAF

        state = dfs(root)
        if state == LEAF:
            return res+1
        return res


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root, prevSum):
            if not root: return True
            
            accu = prevSum + root.val
            if not root.left and not root.right: # root-to-left
                return accu < limit

            canDelLeft = dfs(root.left, accu)
            if canDelLeft:
                root.left = None
            
            canDelRight = dfs(root.right, accu)
            if canDelRight:
                root.right = None
            
            return canDelLeft and canDelRight

        canDel = dfs(root, 0)
        if canDel: return None
        return root
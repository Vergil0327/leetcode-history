# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res

        def dfs(target, arr, root):
            if target == 0 and (not root.left and not root.right):
                res.append(arr.copy())
                return
            
            if root.left:
                arr.append(root.left.val)
                dfs(target-root.left.val, arr, root.left)  
                arr.pop()
            if root.right:
                arr.append(root.right.val)
                dfs(target-root.right.val, arr, root.right)
                arr.pop()

        dfs(targetSum-root.val, [root.val], root)
        return res
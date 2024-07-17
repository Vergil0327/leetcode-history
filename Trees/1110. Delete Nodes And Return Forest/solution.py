# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        self.res = []
        def dfs(node):
            if not node: return node
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in to_delete:
                if node.left:
                    self.res.append(node.left)
                if node.right:
                    self.res.append(node.right)
                return None
            return node
        root = dfs(root)
        if root:
            self.res.append(root)
        return self.res
        
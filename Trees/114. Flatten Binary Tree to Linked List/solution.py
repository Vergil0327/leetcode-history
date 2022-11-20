# time: O(n)
# space: O(n)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        
        order = []
        def dfs(root):
            if not root: return

            order.append(root)
            dfs(root.left)
            dfs(root.right)
        curr = root
        dfs(curr)

        dummy = TreeNode()
        for node in order:
            node.left = node.right = None
            dummy.right = node
            dummy = dummy.right

# time: O(n)
# space: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionFollowUp:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        # flatten left subtree & right subtree
        self.flatten(root.left)
        self.flatten(root.right)
        
        # move left subtree to right, set left to None
        l, r = root.left, root.right
        root.right = l
        root.left = None
        
        # append right subtree after left subtree
        curr = root
        while curr and curr.right:
            curr = curr.right
        curr.right = r
        
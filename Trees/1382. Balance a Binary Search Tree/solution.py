# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # collect nodes in order
        nodes = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            nodes.append(node.val)
            dfs(node.right)

        dfs(root)
        
        # create bst
        n = len(nodes)
        def bst(l, r):
            if l > r: return None
            if l == r: return TreeNode(nodes[l])

            i = l + (r-l)//2
            node = TreeNode(nodes[i])
            node.left = bst(l, i-1)
            node.right = bst(i+1, r)
            return node
        return bst(0, n-1)
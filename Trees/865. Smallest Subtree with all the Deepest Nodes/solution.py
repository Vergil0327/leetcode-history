# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root: return [None, 0] # [LCA, depth]
            
            leftNode, leftDepth = dfs(root.left)
            rightNode, rightDepth = dfs(root.right)
            
            # smallest lowest common ancestor is root with equal depth of left subtree and right subtree
            if leftDepth == rightDepth:
                return [root, leftDepth+1]
            
            # Lowest Common Ancestor node exists in the subtree with deeper depth
            # don't forget to  update current root's depth. current depth = max(left depth, right depth) + 1
            if leftDepth > rightDepth:
                return [leftNode, leftDepth+1]
            elif leftDepth < rightDepth:
                return [rightNode, rightDepth+1]
                
        return dfs(root)[0]
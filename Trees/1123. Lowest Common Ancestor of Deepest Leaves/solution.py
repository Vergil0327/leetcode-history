# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        leaves = []
        maxDepth = 0
        def dfs(root, depth):
            nonlocal maxDepth
            if not root: return root
            
            maxDepth = max(maxDepth, depth)
            if len(leaves) == depth:
                leaves.append([])
            leaves[depth].append(root)

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
            
            return root
        dfs(root, 0)
        
        if len(leaves[maxDepth]) == 1:
            return leaves[maxDepth][0]
        
        nodesSet = set(leaves[maxDepth])
        def findLCA(root, targets):
            if not root: return root
            if root in targets: return root
            
            left = findLCA(root.left, targets)
            right = findLCA(root.right, targets)
            if not left:
                return right
            elif not right:
                return left
            else:
                return root
        return findLCA(root, nodesSet)

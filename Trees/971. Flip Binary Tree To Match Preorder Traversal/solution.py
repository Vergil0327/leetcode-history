# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        res = []
        self.i = 0
        def dfs(root):
            if not root: return True
            
            i = self.i
            self.i += 1
            if root.val != voyage[i]: return False

            if root.right and root.right.val == voyage[self.i]:
                if root.left:
                    res.append(root.val)

                left = dfs(root.right)
                right = dfs(root.left)
                
                return left and right
            else:
                left = dfs(root.left)
                right = dfs(root.right)
            
                return left and right

        if dfs(root):
            return res
        else:
            return [-1]

# Concise
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.res = []
        self.i = 0
        def dfs(root):
            if not root: return True
            
            i = self.i
            self.i += 1
            if root.val != voyage[i]: return False

            if root.right and root.right.val == voyage[self.i]:
                if root.left: # flip only if root.left exists. else we don't need to
                    self.res.append(root.val)
                
                return dfs(root.right) and dfs(root.left) # flip
            else:            
                return dfs(root.left) and dfs(root.right)

        return self.res if dfs(root) else [-1]
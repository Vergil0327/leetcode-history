class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, dst: int) -> str:
        def findLCA(root, p, q):
            if not root: return root
            if root.val == p or root.val == q:
                return root
            
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if not left:
                return right
            elif not right:
                path.append("L")
                return left
            else:
                path.append(root.val)
                return root
        lca = findLCA(root, start, dst)
        
        lcaToStart = []
        def dfs1(root, target):
            if not root: return False
            

            if dfs1(root.left, target):
                lcaToStart.append("U")
                return True
            if dfs1(root.right, target):
                lcaToStart.append("U")
                return True
            
            if root.val == target:
                return True
            
            return False
        dfs1(lca, start)
        
        if lca.val == dst: return "".join(lcaToStart)
        
        lcaToDest = []
        def dfs2(root, target):
            if not root: return False

            if dfs2(root.left, target):
                lcaToDest.append("L")
                return True
            if dfs2(root.right, target):
                lcaToDest.append("R")
                return True
            
            if root.val == target:
                return True
            
            return False
        
        dfs2(lca, dst)
        return "".join(lcaToStart) + "".join(reversed(lcaToDest))


class Solution2:
    def getDirections(self, root: Optional[TreeNode], src: int, dst: int) -> str:
        path = []
        path2src = ""
        path2dst = ""
        def dfs(root, src, dst):
            nonlocal path2src, path2dst
            if not root: return
            
            if root.val == src:
                path2src = "".join(path)
            elif root.val == dst:
                path2dst = "".join(path)

            path.append("L")
            dfs(root.left, src, dst)
            path.pop()
            
            path.append("R")
            dfs(root.right, src, dst)
            path.pop()
            
            return
        dfs(root, src, dst)
        
        # remove common ancestor path
        i = 0
        while i < len(path2src) and i < len(path2dst) and path2src[i] == path2dst[i]:
            i += 1
        
        return "U" * len(path2src[i:]) + path2dst[i:]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
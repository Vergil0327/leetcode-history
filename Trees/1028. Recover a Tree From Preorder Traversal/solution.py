# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:        
        nodes = deque()
        while s:
            d = 0
            while d < len(s) and s[d] == "-":
                d += 1
            s = s[d:]

            i = 0
            while i < len(s) and s[i] != "-":
                i += 1
            root = TreeNode(s[:i])
            nodes.append([root, d])
            s = s[i:]
            
        root, depth = nodes.popleft()
        def dfs(root, d):
            if not root: return root
            if not nodes: return None

            if nodes and nodes[0][1] == d+1:
                root.left = nodes.popleft()[0]
            dfs(root.left, d+1)

            if nodes and nodes[0][1] == d+1:
                root.right = nodes.popleft()[0]
            dfs(root.right, d+1)
            return root
            
        dfs(root, depth)
        return root
    
# Concise
class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:        
        nodes = deque()
        while s:
            d = 0
            while d < len(s) and s[d] == "-":
                d += 1
            s = s[d:]

            i = 0
            while i < len(s) and s[i] != "-":
                i += 1
            root = TreeNode(s[:i])
            nodes.append([root, d])
            s = s[i:]
            
        root, depth = nodes.popleft()
        def dfs(root, d):
            if not nodes: return None
            
            if nodes and nodes[0][1] == d+1:
                root.left = nodes.popleft()[0]
                dfs(root.left, d+1)

            if nodes and nodes[0][1] == d+1:
                root.right = nodes.popleft()[0]
                dfs(root.right, d+1)
            
            return root
            
        return dfs(root, depth)
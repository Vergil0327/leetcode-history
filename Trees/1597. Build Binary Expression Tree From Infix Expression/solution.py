class TreeNode:
    def __init__(self, val='', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, expression: str) -> TreeNode:

        def dfs(s):
            n = len(s)
            
            i = n-1
            while i >= 0:
                ch = s[i]
                if ch == '+' or ch == '-':
                    root = TreeNode(ch)
                    root.right = dfs(s[i+1:])
                    root.left = dfs(s[:i])
                    return root
                elif ch == ")":
                    #  (XXXX(XXX)X)
                    # j           i
                    j = i-1
                    cnt = 1
                    while j >= 0 and cnt>0:
                        if s[j] == ")":
                            cnt += 1
                        elif s[j] == "(":
                            cnt -= 1
                        j -= 1
                    i = j+1
                i -= 1
                
            i = n-1
            while i >= 0:
                ch = s[i]
                if ch == '*' or ch == '/':
                    root = TreeNode(ch)
                    root.right = dfs(s[i+1:])
                    root.left = dfs(s[:i])
                    return root
                elif ch == ")":
                    #  (XXXX(XXX)X)
                    # j           i
                    j = i-1
                    cnt = 1
                    while j >= 0 and cnt>0:
                        if s[j] == ")":
                            cnt += 1
                        elif s[j] == "(":
                            cnt -= 1
                        j -= 1
                    i = j+1
                i -= 1
            if s[0] == "(" and s[-1] == ")":
                return dfs(s[1:n-1])
            return TreeNode(s) if s else None
        
        root = dfs(expression)

        self.res = []
        def inorder(root):
            if not root: return

            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)
        inorder(root)
        return "".join(self.res)

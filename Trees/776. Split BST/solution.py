from typing import List, Type

class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = self.right = None

class Solution_:
    def splitBST(self, root: 'TreeNode', v: int) -> List['TreeNode']:
        def dfs(root, v):
            if not root: return [None, None] # [<=v , >v]

            if root.val > v:
                l, r = dfs(root.left, v)
                root.left = r
                return [l, root]
            else:
                l, r = dfs(root.right, v)
                root.right = l
                return [root, r]

        return dfs(root, v)

# 我們可以發現dfs定義跟splitBST一模一樣, 所以我們可以直接寫成
class Solution:
    def splitBST(self, root: 'TreeNode', v: int) -> List['TreeNode']:
        if not root: return [None, None] # [<=v , >v]

        if root.val > v:
            l, r = self.splitBST(root.left, v)
            root.left = r
            return [l, root]
        else:
            l, r = self.splitBST(root.right, v)
            root.right = l
            return [root, r]
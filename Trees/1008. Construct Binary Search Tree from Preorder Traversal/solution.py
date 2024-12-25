class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(l, r):
            if l > r: return None
            if l == r: return TreeNode(preorder[l])

            node = TreeNode(preorder[l])

            for i in range(l+1, r+1):
                if preorder[i] > node.val:
                    node.left = dfs(l+1, i-1)
                    node.right = dfs(i, r)
                    return node
            node.left = dfs(l+1, r)
            return node
        return dfs(0, len(preorder)-1)

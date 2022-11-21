# Accepted, O(n^2), finding index takes O(n)
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        
        root = TreeNode(preorder[0])
        i = postorder.index(root.val) # root node's previous node is right node
        j = preorder.index(postorder[i-1]) # right node's index
        left = preorder[1:j]
        right = preorder[j:]
        root.left = self.constructFromPrePost(left, postorder)
        root.right = self.constructFromPrePost(right, postorder)
        
        return root

# O(n)
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post2idx = {v: i for i, v in enumerate(postorder)}
        
        # preorder [l:r]
        def build(l, r, postL):
            if l > r: return None
            if l == r: return TreeNode(preorder[l])
        
            root = TreeNode(preorder[l])

            leftIdx = l+1 # left node's index
            i = post2idx[preorder[leftIdx]]  # index of left node in postorder array
            leftSize = i-postL+1

            root.left = build(l+1, l+leftSize, postL)
            root.right = build(l+leftSize+1, r, i+1)
            return root
        return build(0, len(preorder)-1, 0)

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N)
class Solution:
    def __init__(self):
        self.preIdx = self.postIdx = 0

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[self.preIdx])
        
        self.preIdx += 1
        if root.val != postorder[self.postIdx]:
            root.left = self.constructFromPrePost(preorder, postorder)
        if root.val != postorder[self.postIdx]:
            root.right = self.constructFromPrePost(preorder, postorder)
        self.postIdx += 1
        
        return root
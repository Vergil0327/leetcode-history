# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder: return None
        if len(postorder) == 1: return TreeNode(postorder[0])
        
        root = TreeNode(postorder[-1])

        i = inorder.index(root.val) # O(n)
        left = inorder[:i]
        right = inorder[i+1:]
        
        root.left = self.buildTree(left, postorder[:len(left)])
        root.right = self.buildTree(right, postorder[len(left):-1])
        
        return root



# with index (efficient)
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        val2Idx = {v: i for i, v in enumerate(inorder)}
        
        def build(l, r):
            if l > r: return None
            if l == r: return TreeNode(postorder.pop())
            
            root = TreeNode(postorder.pop())
            
            j = val2Idx[root.val]
            root.right = build(j+1, r)
            root.left = build(l, j-1)

            return root
        return build(0, len(inorder)-1)
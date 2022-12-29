# since BST in-order traversal is sorted, if we swap two value,
# one must become larger than original and the other must become smaller than original
# if we swap two node which one is neighbor of the other, we'll only catch `swap1`.
# but we can just record swap2 anyway because swap2 will be written if swap2 exists
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        swap1, swap2 = None, None
        def dfs(root):
            nonlocal prev, swap1, swap2
            if not root: return

            dfs(root.left)
            if not prev or root.val > prev.val:
                prev = root
            else:
                if not swap1:
                    swap1 = prev
                    prev = root

                    swap2 = root # it'll be overwritten if we have second invalid node
                else:
                    swap2 = root
                    return
            dfs(root.right)
        dfs(root)

        swap1.val, swap2.val = swap2.val, swap1.val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

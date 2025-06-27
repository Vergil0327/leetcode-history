
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # key == root.val
            # if not root.left and not root.right: return None # redundant
            if not root.left: return root.right
            if not root.right: return root.left
            
            # find smallest node in right-subtree
            minNode = self.findMinNode(root.right)

            # delete smallest node and we'll swap smallest node with current root node afterwards
            root.right = self.deleteNode(root.right, minNode.val)

            # replace current root node with minNode of right subtree
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        return root
            
    def findMinNode(self, node):
        while node.left:
            node = node.left
        return node
    
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # key == root.val
            # if not root.left and not root.right: return None # redundant
            if not root.left: return root.right
            if not root.right: return root.left
            
            # find smallest node in right-subtree
            minNode = self.findMinNode(root.right)
            
            # swap leaf node with current root node and delete leaf node
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)

        return root
            
    def findMinNode(self, node):
        while node.left:
            node = node.left
        return node
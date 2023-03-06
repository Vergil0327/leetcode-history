class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

"""
依據題意從leaf往root走
如果左節點為新父節點, 那麼將父節點移到左節點
如果右節點為新父節點, 那麼將右節點移到左節點, 然後父節點移到左節點
持續遞歸

等到遞歸到原本的root後, 需要特別處理
如果左節點為新的父節點, 那把左節點指向None
"""
class Solution:
    def flipBinaryTree(self, root: "Node", leaf: "Node") -> "Node":
        def reroot(root, prev):
            if not root: return root

            parent = root.parent
            root.parent = prev

            if not parent: # original root node
                if root.left == prev:
                    root.left = None
                elif root.right == prev:
                    root.right = None
            else:
                # cur's original parent becomes cur's left child.
                if root.left == prev:
                    root.left = parent
                elif root.right == prev:
                    # If cur has a left child, then that child becomes cur's right child.
                    root.right = root.left
                    root.left = parent
            return reroot(parent, root)
        return reroot(leaf, None)
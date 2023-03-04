# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:        
        possibleRoots = {}
        leaves = set()
        for tree in trees:
            possibleRoots[tree.val] = tree
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
        roots = []
        for root in possibleRoots.keys():
            if root not in leaves:
                roots.append(possibleRoots[root])
        if len(roots) != 1: return None

        def dfs(root):
            if not root: return root
            
            # leaf node
            if root and not root.left and not root.right:
                if root.val in possibleRoots:
                    merge = possibleRoots[root.val]
                    del possibleRoots[root.val]

                    merge.left = dfs(merge.left)
                    merge.right = dfs(merge.right)
                    return merge
                return root

            root.left = dfs(root.left)
            root.right = dfs(root.right)
            return root

        root = roots[0]
        del possibleRoots[root.val]
        dfs(root)
        if len(possibleRoots) != 0: return None

        def isValidBST(root, l, r):
            if not root: return True

            if l < root.val < r:
                return isValidBST(root.left, l, root.val) and isValidBST(root.right, root.val, r)
            else:
                return False

        if not isValidBST(root, -inf, inf):
            return None
        return root

# Optimized
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        trees.sort(key=lambda t:t.val)
        
        possibleRoots = {}
        leaves = set()
        for tree in trees:
            possibleRoots[tree.val] = tree
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
        roots = []
        for root in possibleRoots.keys():
            if root not in leaves:
                roots.append(possibleRoots[root])
        if len(roots) != 1: return None

        def build(root, l, r):
            if not root: return (root, True)

            val = root.val
            if val <= l or val >= r: return (None, False)

            if root.left or root.right:
                root.left, ok1 = build(root.left, l, root.val)
                root.right, ok2 = build(root.right, root.val, r)
                return (root, True) if ok1 and ok2 else (None, False)
            elif val in possibleRoots: # leaf node
                node = possibleRoots[val]
                del possibleRoots[val]

                node.left, ok1 = build(node.left, l, root.val)
                node.right, ok2 = build(node.right, root.val, r)
                return (node, True) if ok1 and ok2 else (None, False)
            else:
                return root, True

        root = roots[0]
        del possibleRoots[root.val]
        
        root, ok = build(root, -inf, inf)
        if len(possibleRoots) != 0: return None

        return root if ok else None
    
"""
O(n^2)
最初想法是遍歷全部的root node
然後進行DFS, 只要leaf node存在於roots hashmap裡就接枝上去(前提是roots裡的node不可以是當前的根節點, 不然就形成一個環了)
然後最後再檢查是不是合法的BST
"""
class Solution_TLE:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        trees.sort(key=lambda t:t.val)
        
        roots = {}
        for tree in trees:
            roots[tree.val] = tree

        def dfs(root, node):
            if not node: return node
            if node and not node.left and not node.right: # leaf
                if node.val in roots and node != roots[node.val] and roots[node.val] != root:
                    newNode = roots[node.val]
                    del roots[node.val]

                    newNode.left = dfs(root, newNode.left)
                    newNode.right = dfs(root, newNode.right)
                    return newNode

                return node
            
            node.left = dfs(root, node.left)
            node.right = dfs(root, node.right)

            return node

        for tree in trees:
            if tree.val in roots:
                dfs(tree, tree)
                
        rootNodes = list(roots.values())
        if len(rootNodes) != 1: return None
            
        root = rootNodes[0]
        def isValidBST(root, l, r):
            if not root: return True

            if l < root.val < r:
                return isValidBST(root.left, l, root.val) and isValidBST(root.right, root.val, r)
            else:
                return False

        if not isValidBST(root, -inf, inf):
            return None
        return root
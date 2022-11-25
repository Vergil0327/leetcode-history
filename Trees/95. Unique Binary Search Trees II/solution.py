# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # [l, r]
        def generateDFS(l, r):
            res = []
            if l > r:
                res.append(None)
                return res

            # choose i as root
            for i in range(l, r+1):
                leftTree = generateDFS(l, i-1)
                rightTree = generateDFS(i+1, r)

                for leftNode in leftTree:
                    for rightNode in rightTree:
                        root = TreeNode(i)
                        root.left = leftNode
                        root.right = rightNode
                        res.append(root)
            return res
                
        return generateDFS(1, n)
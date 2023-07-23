# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n%2==0: return []

        @lru_cache(None)
        def backtracking(n):
            if n == 0: return []
            if n == 1: return [TreeNode()]

            res = []
            for numLeft in range(n):
                numRight = n-numLeft-1 # 1 for root node
                
                leftSubtree = backtracking(numLeft)
                rightSubtree = backtracking(numRight)
                for leftRoot in leftSubtree:
                    for rightRoot in rightSubtree:
                        res.append(TreeNode(0, leftRoot, rightRoot))
            return res
        return backtracking(n)

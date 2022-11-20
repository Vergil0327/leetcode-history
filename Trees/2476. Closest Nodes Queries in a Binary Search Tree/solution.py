# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        values = []
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            values.append(root.val)
            dfs(root.right)
        dfs(root)

        n = len(values)
        res = []
        for q in queries:
            tmp = []
            l, r = 0 , n-1
            while l < r:
                mid = r - (r-l)//2
                if values[mid] > q:
                    r = mid-1
                else:
                    l = mid
            tmp.append(values[l] if values[l] <= q else -1)
            
            l, r = 0 , n-1
            while l < r:
                mid = l + (r-l)//2
                if values[mid] < q:
                    l = mid+1
                else:
                    r = mid
            tmp.append(values[l] if values[l] >= q else -1)
            res.append(tmp)
        return res

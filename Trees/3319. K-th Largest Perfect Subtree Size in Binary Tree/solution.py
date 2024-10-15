# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        def dfs(node):
            if not node: return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if l < inf and r < inf and l == r:
                heapq.heappush(pq, l+r+1)
                if len(pq) > k:
                    heapq.heappop(pq)
                return l + r + 1
            else:
                return inf
        dfs(root)

        return pq[0] if len(pq) == k else -1
    

class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        pq = []
        def dfs(node):
            if not node: return 0

            l = dfs(node.left)
            r = dfs(node.right)

            if l == r and (size := l+r+1) > 0:
                heapq.heappush(pq, size)
                if len(pq) > k:
                    heapq.heappop(pq)
                return size
            else:
                return -inf
        dfs(root)

        return pq[0] if len(pq) == k else -1
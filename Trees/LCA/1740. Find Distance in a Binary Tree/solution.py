class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


"""
resource: https://www.cnblogs.com/Dylan-Java-NYC/p/16579983.html

We could it in one pass.

DFS returns current root distance to either p or q.

When root.val == p || q. One case is it is the first time we see p or q and didn't see the other, we return 0.

The other case is it is the second time we see p or q, which means we have seen both p and q. We find the LCA, it is either p or q. Return Math.max(l, r) + 1.

If both l >=0 && r >= 0, it means we find the LCA, its subtrees contains p and q. Return l + r + 2.

Time Complexity: O(n). n is the size of tree.

Space: O(logn).
"""

class Solution:
    def findDistance(self, root: TreeNode, p: int, q:int):
        if p == q: return 0

        res = 0
        def dfs(root, p, q):
            nonlocal res
            if not root: return -1

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if root.val == p or root.val == q:
                if left < 0 and right < 0:
                    return 0

                # found LCA and LCA is either p or q
                res = max(left, right) + 1
                return -1

            if left >= 0 and right >= 0:
                # found LCA
                res = left+right+2
                return -1

            if left >= 0: return left +1
            if right >= 0: return right+1

            return -1
        
        dfs(root, p, q)
        return res

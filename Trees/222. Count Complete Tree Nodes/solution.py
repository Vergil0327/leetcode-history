# https://www.youtube.com/watch?v=JSq15O0Bs-E&ab_channel=HuifengGuan

# Binary Search: O(logn * logn)
class Solution:
    def existsK(self, root: Optional[TreeNode], k: int) -> bool:
        # left-child is 2*root.val
        # right-child is 2*root.val+1
        pathToK = []
        while k > 0:
            pathToK.append(k)
            k //= 2

        for i in range(len(pathToK)-1, -1, -1):
            if not root: return False # height is not enough
            if i == 0: return True # found K exists in completed tree

            if pathToK[i-1] == 2*pathToK[i]:
                root = root.left
            else:
                root = root.right
        
        return False # empty path to K

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        h = 0
        curr = root
        while curr:
            h += 1
            curr = curr.left

        # ! edge case: if h = 0, l == -1 -> l becomes 0.5
        l, r = int(2**(h-1)), 2**h-1
        while l < r:
            mid = r - (r-l)//2
            if self.existsK(root, mid):
                l = mid
            else:
                r = mid-1
        return l

# Recursion: O(logn * logn)
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def findMaxHeight(root):
            if not root: return 0
            return 1+findMaxHeight(root.left)

        def dfs(root):
            if not root: return 0
            
            cnt = 1 # root node

            h1 = findMaxHeight(root.left)
            h2 = findMaxHeight(root.right)

            if h1 == h2:
                return cnt + 2**h1-1 + dfs(root.right)
            else:
                return cnt + 2**h2-1 + dfs(root.left)
        
        return dfs(root)
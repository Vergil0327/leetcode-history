# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time: O(2N)
# space: O(N)
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        nodes = []

        # in-order DFS traversal can get value in order
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        dfs(root)
        
        # suffix sum
        nodes = nodes + [TreeNode(0)]
        for i in range(len(nodes)-2, -1, -1):
            nodes[i].val += nodes[i+1].val
            
        return root

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 0,1,2,3,4,5,6,7,8
        nums = []
        
        def dfs(root):
            if not root: return
            
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        dfs(root)
        
        # suffix sum
        nums.append(0)
        for i in range(len(nums)-2, -1, -1):
            nums[i] += nums[i+1]
        
        j = 0
        def dfs2(root):
            nonlocal j
            if not root: return
            
            dfs2(root.left)
            root.val = nums[j]
            j += 1
            dfs2(root.right)
        dfs2(root)
        return root

# Optimized Solution
# time: O(n)
# space: O(1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        total = 0
        def dfs(root):
            nonlocal total
            if not root: return
            
            dfs(root.right)
            total += root.val
            root.val = total
            dfs(root.left)
        dfs(root)

        return root
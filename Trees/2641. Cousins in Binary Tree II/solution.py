# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = defaultdict(int)
        queue = deque([[root, 0]])
        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()
                total[level] += node.val
                if node.left:
                    queue.append([node.left, level+1])
                if node.right:
                    queue.append([node.right, level+1])

        queue = deque([[root, 0]])
        while queue:
            for _ in range(len(queue)):
                node, level = queue.popleft()
                
                SUM = 0
                if node.left:
                    SUM += node.left.val
                    queue.append([node.left, level+1])
                if node.right:
                    SUM += node.right.val
                    queue.append([node.right, level+1])
                
                if level <= 1:
                    node.val = 0
                
                if node.left:
                    node.left.val = total[level+1] - SUM
                if node.right:
                    node.right.val = total[level+1] - SUM
        return root

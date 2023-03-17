# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Slow
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    if queue and queue[0] is not None: return False
                    continue
                
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                
                
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
        return True

# Fast
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])


        showNone = False
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    showNone = True
                    continue

                if showNone: return False
                
                queue.append(node.left)
                queue.append(node.right)
        return True
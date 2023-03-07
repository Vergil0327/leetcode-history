
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:
    def correctBinaryTree(self, root: 'TreeNode') -> 'TreeNode':
        queue = deque([root])

        visited = set([root.val])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    if node.left.right and node.left.right.val in visited: # found invalid
                        node.left = None
                        return root
                    visited.add(node.left.val)
                    queue.append(node.left)
                if node.right:
                    if node.right.right and node.right.right.val in visited: # found invalid
                        node.right = None
                        return root
                    visited.add(node.right.val)
                    queue.qppend(node.right)

        return root

            


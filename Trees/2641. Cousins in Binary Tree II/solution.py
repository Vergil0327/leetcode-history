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

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levelSum = Counter()

        def dfs1(node, level):
            if not node: return
            levelSum[level] += node.val

            dfs1(node.left, level+1)
            dfs1(node.right, level+1)
        dfs1(root, 1)

        def dfs2(node, level, siblingSum):
            if not node: return

            node.val = levelSum[level] - siblingSum

            nxtSiblingSum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
            dfs2(node.left, level+1, nxtSiblingSum)
            dfs2(node.right, level+1, nxtSiblingSum)
        
        dfs2(root, 1, root.val)
        return root
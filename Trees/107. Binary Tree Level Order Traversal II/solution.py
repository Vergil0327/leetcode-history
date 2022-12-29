# BFS
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        order = []
        queue = deque([root])
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            order.append(tmp)
        return list(reversed(order))

# DFS
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root

        order = []
        def dfs(root, level):
            if not root: return root
            
            if level == len(order):
                order.append([])
            if root:
                order[level].append(root.val)

            left = dfs(root.left, level+1)
            right = dfs(root.right, level+1)
            return root
        dfs(root, 0)
        
        return list(reversed(order))
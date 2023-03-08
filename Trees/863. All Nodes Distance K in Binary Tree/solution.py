# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.parent = defaultdict(int)
        def dfs(root):
            if not root: return root
            left = dfs(root.left)
            right = dfs(root.right)

            self.parent[left] = root
            self.parent[right] = root
            return root
        dfs(root)

        queue = deque([target])
        visited = set()
        step = 0
        while queue:
            if step == k:
                return [node.val for node in queue]
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val in visited: continue
                visited.add(node.val)

                if node.left and node.left.val not in visited:
                    queue.append(node.left)
                if node.right and node.right.val not in visited:
                    queue.append(node.right)
                if self.parent[node] and self.parent[node].val not in visited:
                    queue.append(self.parent[node])

            step += 1
        return []
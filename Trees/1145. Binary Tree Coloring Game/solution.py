# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # construct graph
        graph = defaultdict(list)
        def dfs(node):
            if not node: return

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)

        # find subtree size
        queue = deque() # [current node, start node]
        size = Counter() # tree size
        for node in graph[x]:
            queue.append([node, node])
            size[node] = 1
        visited = set([x])

        while queue:
            node, _id = queue.popleft()
            if node in visited: continue
            visited.add(node)

            for nxt in graph[node]:
                if nxt in visited: continue
                size[_id] += 1
                queue.append([nxt, _id])

        # check if any one of subtree size is greater than sum of other's
        tree_size = sorted(size.values())
        return tree_size[-1] > sum(tree_size[:-1]) + 1

# pure dfs:
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        leftX = rightX = 0
        def dfs(node):
            nonlocal leftX, rightX

            if not node: return 0

            l = dfs(node.left)
            r = dfs(node.right)
            if node.val == x:
                leftX, rightX = l, r

            return l + r + 1

        total = dfs(root)

        upperX = (total-leftX-rightX-1)
        res = max(leftX, rightX, upperX)
        return  res > total-res

# Optimzed
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        # time: O(n), space: O(n)
        def dfs(node):
            if not node:
                return 0, 0, 0
            if node.val == x:
                l, _, _ = dfs(node.left)
                r, _, _ = dfs(node.right)
                return 0, l, r
            c1, l1, r1 = dfs(node.left)
            c2, l2, r2 = dfs(node.right)
            return 1 + c1 + c2, l1 + l2, r1 + r2    
        res = max(dfs(root))
        return res > n - res
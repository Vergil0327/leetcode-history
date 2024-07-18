# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.leaf = set()

        self.graph = defaultdict(set)
        _id = {}
        start_id = 0
        def dfs(node, parent):
            nonlocal start_id
            if not node: return
            _id[node] = start_id
            start_id += 1

            if not node.left and not node.right:
                self.leaf.add(node)
            if node.left:
                self.graph[node].add(node.left)
                self.graph[node.left].add(node)
                dfs(node.left, node)
            if node.right:
                self.graph[node].add(node.right)
                self.graph[node.right].add(node)
                dfs(node.right, node)
        dfs(root, None)
        
        queue = deque()
        for node in self.leaf:
            queue.append([node, _id[node]])

        pair = set()
        seen = set()
        while distance >= 0 and queue:
            for _ in range(len(queue)):
                node, start_id = queue.popleft()
                if (_id[node], start_id) in seen or (start_id, _id[node]) in seen: continue
                seen.add((_id[node], start_id))

                if node in self.leaf and _id[node] != start_id:
                    pair.add((min(_id[node], start_id), max(_id[node], start_id)))

                for nxt in self.graph[node]:
                    if nxt in _id and _id[nxt] == start_id: continue
                    queue.append([nxt, start_id])

            distance -= 1

        return len(pair)


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        res = 0
        def dfs(node) -> list[int]:
            if not node: return []
            if node.left is node.right: # it means node is leaf node since leaf.left == leaf.right == None
                return [1]

            right = dfs(node.right)
            left = dfs(node.left)
            nonlocal res
            for r in right:
                for l in left:
                    if l + r <= distance:
                        res += 1
            leaves = []
            for x in right + left:
                x += 1
                if x < distance:
                    leaves.append(x)
            return leaves

        dfs(root)
        return res
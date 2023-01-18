# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.level = [TreeNode()]
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                self.level.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
    def insert(self, val: int) -> int:
        idx = len(self.level)
        parent = idx//2

        node = TreeNode(val)
        if idx == parent * 2: # left child:
            self.level[parent].left = node
        else: # right child
            self.level[parent].right = node
        self.level.append(node)
        return self.level[parent].val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
# [NULL, 1,2,3,4,5,6,7,8,9,10]

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
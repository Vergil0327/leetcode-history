# Iterative way
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.curr = -1
        
        self.stack = []
        stack = self.stack
        while root:
            while root:
                stack.append(root)
                root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        curr = node.right
        while curr:
            self.stack.append(curr)
            curr = curr.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        
        

# Brute Force - Store them all
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorder = deque()
        def dfs(root):
            if not root: return

            dfs(root.left)
            self.inorder.append(root.val)
            dfs(root.right)
        dfs(root)

    def next(self) -> int:
        return self.inorder.popleft()

    def hasNext(self) -> bool:
        return len(self.inorder)>0


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
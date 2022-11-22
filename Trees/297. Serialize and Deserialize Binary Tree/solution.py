# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://labuladong.github.io/algo/2/21/39/
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        values = []
        def dfs(root):
            if not root:
                values.append("#")
                return
            
            values.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(values)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = deque(data.split(","))
        
        def dfs(data):
            if not data: return None
            if data[0] == "#":
                data.popleft()
                return None
            root = TreeNode(int(data.popleft()))
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        return dfs(values)

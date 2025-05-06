class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        self.res = []
        def dfs(node):
            if not node:
                self.res.append("N")
                return

            self.res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ",".join(self.res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        nodes = data.split(",")
        
        self.i = 0
        def dfs(nodes):
            if self.i >= len(nodes): return None
            
            node = TreeNode(nodes[self.i]) if nodes[self.i] != "N" else None
            self.i += 1
            if node is None: return node
            
            left = dfs(nodes)
            right = dfs(nodes)
            node.left = left
            node.right = right
            return node

        root = dfs(nodes)
        return root
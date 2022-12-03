from typing import List


class TreeNode:
  def __init__(self, val: int):
     self.val = val
     self.left = None
     self.right = None

# time: O(n)
# space: O(n)
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]):
        requires = set(nodes)

        def dfs(root):
            if not root: return root
            if root in requires: return root

            left = dfs(root.left)
            right = dfs(root.right)

            if not left:
                return right
            elif not right:
                return left
            else:
                return root
        
        return dfs(root)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, nodes: List[TreeNode]):
        nodeSet = set(nodes)
        res = None

        def dfs(root):
            if not root: return 0

            left = dfs(root.left)
            right = dfs(root.right)

            cnt = 1 if root in nodeSet else 0
            if cnt + left + right == len(nodeSet) and not res:
                res = root

            return left + right + cnt
        dfs(root)
        return res

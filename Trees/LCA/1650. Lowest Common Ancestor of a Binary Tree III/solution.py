from collections import deque
from typing import Optional


class TreeNode:
  def __init__(self, val:int, left: Optional[int]=None, right:Optional[int]=None, parent:Optional[int]=None):
    self.val = val
    self.left = left
    self.right = right
    self.parent = parent

class Solution:
    def lowestCommonAncestor(self, p: 'TreeNode', q: 'TreeNode'):
        pToRoot = []
        curr = p
        while curr.parent:
            pToRoot.append(curr)
            curr = curr.parent

        qToRoot = []
        curr = q
        while curr.parent:
            qToRoot.append(curr)
            curr = curr.parent

        lca = None
        while pToRoot and qToRoot and pToRoot[-1] == qToRoot[-1]:
            lca = pToRoot.pop()
            qToRoot.pop()
        return lca

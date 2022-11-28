# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root: return [root, 0]
            left = dfs(root.left)
            right = dfs(root.right)

            if root.val == p.val: return [root, left[1] + right[1] + 1]
            if root.val == q.val: return [root, left[1] + right[1] + 1]

            if not left[0]: return right
            if not right[0]: return left

            return [root, left[1]+right[1]]
        
        lca, cnt = dfs(root)
        if cnt == 2:
            return lca
        else:
            return None


def build(nums: List[int]):
    nodes = deque(nums)
    root = TreeNode(nodes.popleft())
    deq = deque([root])
    while deq and nodes:
        curr = deq.popleft()
        left = nodes.popleft()
        right = nodes.popleft()
        
        if left is not None:
            curr.left = TreeNode(left)
            deq.append(curr.left)
        if right is not None:
            curr.right = TreeNode(right)
            deq.append(curr.right)

    return root

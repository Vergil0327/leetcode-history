from typing import List
import sortedcontainers

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = self.right = None

# nlogn
class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        root = TreeNode(order[0])

        self.depth = 1
        def insertNode(root, val, d):
            self.depth = max(self.depth, d+1)
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    insertNode(root.left, val, d+1)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    insertNode(root.right, val, d+1)
            
        for i in range(1, len(order)):
            insertNode(root, order[i], 1)
        return self.depth

    def maxDepthBST_2(self, order):
        """
        :type order: List[int]
        :rtype: int
        """
        depths = sortedcontainers.SortedDict({float("-inf"):0, float("inf"):0})

        result = 0
        for x in order:
            i = depths.bisect_right(x)
            values_view = depths.values()
            depths[x] = max(values_view[i-1:i+1])+1
            result = max(result, depths[x])
        return result
    
        # [2,1,4,3]
        # {-inf: 0, inf: 0}
        # {-inf: 0, 2: 1, inf: 0}
        # {-inf: 0, 1: 2, 2: 1, inf: 0}
        # {-inf: 0, 1: 2, 2: 1, 4: 2 inf: 0}
        # {-inf: 0, 1: 2, 2: 1, 3: 3 4: 2 inf: 0}
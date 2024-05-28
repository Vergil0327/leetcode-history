class Node:
    def __init__(self, l, r) -> None:
        self.l, self.r = l, r
        self.left = self.right = None
        self.info = [0,0,0,0] # [dp00, dp01, dp10, dp11]

class SegmentTree:
    def __init__(self, l: int, r: int, nums: int): # init range [l,r] with nums
        def init_tree(l, r, nums):
            node = Node(l, r)
            if l == r:
                node.info = [0, -inf, -inf, nums[l]]
                return node
            
            mid = (l+r)//2
            if node.left == None:
                node.left = init_tree(l, mid, nums)
                node.right = init_tree(mid+1, r, nums)

                node.info[0] = max(
                    node.left.info[0] + node.right.info[0], # 00 = 00+00
                    node.left.info[1] + node.right.info[0], # 00 = 01+00
                    node.left.info[0] + node.right.info[2], # 00 = 00+10
                )
                
                # dp01
                node.info[1] = max(
                    node.left.info[0] + node.right.info[1], # 01 = 00+01
                    node.left.info[1] + node.right.info[1], # 01 = 01+01
                    node.left.info[0] + node.right.info[3], # 01 = 00+11
                )

                # dp10
                node.info[2] = max(
                    node.left.info[2] + node.right.info[0], # 10 = 10+00
                    node.left.info[2] + node.right.info[2], # 10 = 10+10
                    node.left.info[3] + node.right.info[0], # 10 = 11+00
                )

                # dp11
                node.info[3] = max(
                    node.left.info[2] + node.right.info[1], # 11 = 10+01
                    node.left.info[2] + node.right.info[3], # 11 = 10+11
                    node.left.info[3] + node.right.info[1], # 11 = 11+01
                )
            return node
        self.root = init_tree(l, r, nums)

    def update(self, idx: int, val: int) -> None:
        def _update(node, idx, val):
            if idx < node.l or idx  > node.r: return # not covered by [l,r]

            if idx <= node.l and node.r <= idx:
                node.info[3] = val
                node.info[0]
                return
            
            if node.left:
                _update(node.left, idx, val)
                _update(node.right, idx, val)
                
                node.info[0] = max(
                    node.left.info[0] + node.right.info[0], # 00 = 00+00
                    node.left.info[1] + node.right.info[0], # 00 = 01+00
                    node.left.info[0] + node.right.info[2], # 00 = 00+10
                )
                
                # dp01
                node.info[1] = max(
                    node.left.info[0] + node.right.info[1], # 01 = 00+01
                    node.left.info[1] + node.right.info[1], # 01 = 01+01
                    node.left.info[0] + node.right.info[3], # 01 = 00+11
                )

                # dp10
                node.info[2] = max(
                    node.left.info[2] + node.right.info[0], # 10 = 10+00
                    node.left.info[2] + node.right.info[2], # 10 = 10+10
                    node.left.info[3] + node.right.info[0], # 10 = 11+00
                )

                # dp11
                node.info[3] = max(
                    node.left.info[2] + node.right.info[1], # 11 = 10+01
                    node.left.info[2] + node.right.info[3], # 11 = 10+11
                    node.left.info[3] + node.right.info[1], # 11 = 11+01
                )

        return _update(self.root, idx, val)

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        
        seg = SegmentTree(0, len(nums)-1, nums)
        
        res = 0
        for i, x in queries:
            seg.update(i, x)
            
            res += max(seg.root.info)
            res %= mod
        return res

class Node:
    def __init__(self, l, r) -> None:
        self.l, self.r = l, r
        self.left = self.right = None
        self.info = self.lazy_tag = self.lazy_delta = 0 

class LazySegmentTreeSumIncreaseDelta:
    """
    updateRangeBy will increase delta in range [l, r]
    """
    def __init__(self, l: int, r: int, val: int): # init range [l,r] with val
        def init_tree(l, r, val):
            node = Node(l, r)
            if l == r:
                node.info = val
                return node
            
            mid = (l+r)//2
            if node.left == None:
                node.left = init_tree(l, mid, val)
                node.right = init_tree(mid+1, r, val)
                node.info = node.left.info + node.right.info
            return node
        self.root = init_tree(l, r, val)

    # propagation lazy tag and value from parent to child nodes
    def pushDown(self, node):
        if node.lazy_tag == 1 and node.left:
            node.left.info += node.lazy_delta * (node.left.r - node.left.l + 1)
            node.right.info += node.lazy_delta * (node.right.r - node.right.l + 1)

            node.left.lazy_tag = 1
            node.left.lazy_delta += node.lazy_delta
            
            node.right.lazy_tag = 1
            node.right.lazy_delta += node.lazy_delta
            node.lazy_tag = node.lazy_delta = 0

    def updateRangeBy(self, l: int, r: int, delta: int) -> None:
        def update(node, l, r, val):
            if r < node.l or l  > node.r: return # not covered by [l,r]

            if l <= node.l and node.r <= r:
                node.info += val * (node.r-node.l+1)
                node.lazy_tag = 1
                node.lazy_delta += val
                return
            
            if node.left:
                self.pushDown(node)
                update(node.left, l, r, val)
                update(node.right, l, r, val)
                node.info = sum([node.left.info, node.right.info])

        return update(self.root, l, r, delta)

    def queryRange(self, l: int, r: int) -> int:
        def query(node, l, r):
            if r < node.l or l > node.r: return 0

            if l <= node.l and node.r <= r:
                return node.info
            
            if node.left:
                self.pushDown(node)
                res = sum([query(node.left, l, r), query(node.right, l, r)])
                node.info = sum([node.left.info, node.right.info])
                return res
            
            return node.info # should not reach here
        return query(self.root, l, r)

# example:
# class Solution:
#     def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:        
#         n = len(s)

#         right = [-1]*n # valid right boundary of i, s[i:right[i]+1] is valid substring
#         count0 = count1 = j = 0
#         for i in range(n):
#             while j < n and (count0+int(s[j]== "0") <= k or count1+int(s[j]=="1") <= k):
#                 count0 += int(s[j]== "0")
#                 count1 += int(s[j]== "1")
#                 j += 1
#             right[i] = j-1

#             count0 -= int(s[i] == "0")
#             count1 -= int(s[i] == "1")

        
#         for i in range(len(queries)):
#             queries[i].append(i)
#         queries.sort(reverse=True)

#         root = LazySegmentTreeSumIncreaseDelta(0, n-1, 0)
#         res = [0] * len(queries)
#         i = n-1
#         for l, r, idx in queries:
#             while i >= l:
#                 root.updateRangeBy(i, right[i], 1)
#                 i -= 1
#             res[idx] = root.queryRange(l, r)
#         return res
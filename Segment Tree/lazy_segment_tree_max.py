class Node:
    def __init__(self, l, r) -> None:
        self.l, self.r = l, r
        self.left = self.right = None
        self.info = self.lazy_tag = self.lazy_val = 0 

class LazySegmentTreeMax:
    def __init__(self, l: int, r: int, nums: int): # init range [l,r] with nums
        def init_tree(l, r, nums):
            node = Node(l, r)
            if l == r:
                node.info = nums[l]
                return node
            
            mid = (l+r)//2
            if node.left == None:
                node.left = init_tree(l, mid, nums)
                node.right = init_tree(mid+1, r, nums)
                node.info = node.left.info + node.right.info
            return node
        self.root = init_tree(l, r, nums)

    # propagation lazy tag and value from parent to child nodes
    def pushDown(self, node):
        if node.lazy_tag == 1 and node.left:
            node.left.info = node.info
            node.right.info = node.info

            node.left.lazy_tag = 1
            node.right.lazy_tag = 1
            
            node.lazy_tag = 0

    def updateRange(self, l: int, r: int, val: int) -> None:
        def update(node, l, r, val):
            if r < node.l or l  > node.r: return # not covered by [l,r]

            if l <= node.l and node.r <= r:
                node.info = val
                node.lazy_tag = 1
                return
            
            if node.left:
                self.pushDown(node)
                update(node.left, l, r, val)
                update(node.right, l, r, val)
                node.info = max(node.left.info, node.right.info)

        return update(self.root, l, r, val)

    def queryRange(self, l: int, r: int) -> int:
        def query(node, l, r):
            if r < node.l or l > node.r: return 0

            if l <= node.l and node.r <= r:
                return node.info
            
            if node.left:
                self.pushDown(node)
                res = max(query(node.left, l, r), query(node.right, l, r))
                node.info = max(node.left.info, node.right.info)
                return res
            
            return node.info # should not reach here
        return query(self.root, l, r)

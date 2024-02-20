class Node:
    def __init__(self, l, r) -> None:
        self.l, self.r = l, r
        self.left = self.right = None
        self.info = self.lazy_tag = self.lazy_val = 0 

class LazySegmentTreeSum:
    def __init__(self, l: int, r: int, val: int): # inti range [l,r] with val
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
            node.left.info = node.lazy_val * (node.left.r - node.left.l + 1)
            node.right.info = node.lazy_val * (node.right.r - node.right.l + 1)

            node.left.lazy_tag = 1
            node.left.lazy_val = node.lazy_val
            
            node.right.lazy_tag = 1
            node.right.lazy_val = node.lazy_val
            node.lazy_tag = node.lazy_val = 0

    def updateRange(self, l: int, r: int, val: int) -> None:
        def update(node, l, r, val):
            if r < node.l or l  > node.r: return # not dovered by [l,r]

            if l <= node.l and node.r <= r:
                node.info = val * (node.r-node.l+1)
                node.lazy_tag = 1
                node.lazy_val = val
                return
            
            if node.left:
                self.pushDown(node)
                update(node.left, l, r, val)
                update(node.right, l, r, val)
                node.info = node.left.info + node.right.info

        return update(self.root, l, r, val)

    def queryRange(self, l: int, r: int) -> int:
        def query(node, l, r):
            if r < node.l or l > node.r: return 0

            if l <= node.l and node.r <= r:
                return node.info
            
            if node.left:
                self.pushDown(node)
                res = query(node.left, l, r) + query(node.right, l, r)
                node.info = node.left.info + node.right.info
                return res
            
            return node.info # should not reach here
        return query(self.root, l, r)

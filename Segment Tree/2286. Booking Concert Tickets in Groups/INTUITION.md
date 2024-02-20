# Intuition

n x m matrix

- gather: 返回(row, col) where row <= maxRow and [col, col+k-1] are all valid
- scatter: 判斷在所有`row <= maxRow`情況下, 存不存在著k個座位, 有的話返回True並從最小(row, col)開始坐滿k個

我們需要的是能快速在[0, maxRow]範圍內查找
1. k個連續座位
2. k個不連續座位

range query => segment tree, 但該如何實現?

一開始把題目想複雜了, 覺得每個row的座位有可能會變成多個區間, 有些區間有坐人、有些沒有
但實際上並不會, 由於都是從smallest seat開始, 所以不管是`gather`或`scatter`, 永遠都從smallest seat開始坐人
所以每一row永遠都是consecutive seats, 因此我們能用一個seats[row]以及segment tree來維護每row還有多少consecutive seats

seats[row]: the number of available seats, 由於從smallest開始, 那這樣不管scatter 或 gather
最終都會讓smallest row優先被坐滿, 那這樣我們就能另外維護一個單調遞增的smallest row index `startRow`有利於我們搜索

再來我們分別來看

`scatter`:

x = segment.query_sum(0, maxRow)
我們需要**k**個座位, 所以只要 x >= k 即可, 然後從最小seat number開始連續標記k個座位已被訂位 => how?

再來由於這題要從smallest row and seats開始考察
我們可以用個單調遞增的index `startRow`以及一個array seats[row]來紀錄每個row現在有多少available seats

那這樣再配合前面的x = segment_tree.query_sum(0, maxRow), 只要 x >= k, 那就能更新seats[startRow]


`gather`:
smallest_seat = segment_tree.query_max_consecutive(0, maxRow)
那找到後一樣記得更新seats[smallest_seat]

所以我們需要能query_sum以及query_max的segment tree
可以寫在一起, 也能分開維護兩個不同用途的segment tree

## Iterative/Recursive Segment Tree

```py
class SegmentTree:
    def __init__(self, arr, op):
        self.n = n = len(arr)
        self.op = op
        self.st = st = [0]*n + arr
        for i in range(n-1, 0, -1):
            st[i] = op([st[i<<1], st[i<<1|1]])
        
    def __getitem__(self, i):
        return self.st[i+self.n]
    def __setitem__(self, i, val):
        st, op, n = self.st, self.op, self.n
        i += n
        st[i] = val

        while i:
            st[i>>1] = op([st[i], st[i^1]])
            i >>= 1

    def query(self, l, r): # query range [l,r]
        st, op, n = self.st, self.op, self.n
        l, r = l+n, r+n

        res = 0
        while l <= r:
            if l == r:
                res = op([res, st[l]])
                break
            if l&1 == 1:
                res = op([res, st[l]])
                l += 1
            if r&1 == 0:
                res = op([res, st[r]])
                r -= 1
            l, r = l>>1, r>>1
        return res
```

## Recursion Segment Tree

credit to [@stilleholz](https://leetcode.com/problems/booking-concert-tickets-in-groups/solutions/2085084/python-segment-tree-range-sum-max-with-explanation/)

```py
class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None
        self.total = 0 # for range sum query
        self.mx = 0 # for range max query
        
class SegTree:
    def __init__(self, start, end, val):
        
        def build(l, r):
            if l > r:
                return None
            if l == r:
                node = Node(l, r)
                node.total = val
                node.mx = val
                return node
            node = Node(l, r)
            m = (l + r) // 2
            node.left = build(l, m)
            node.right = build(m+1, r)
            node.mx = max(node.left.mx, node.right.mx)
            node.total = sum([node.left.total, node.right.total])
            return node
        
        self.root = build(start, end)
    
	# update the total remain seats and the max remain seats for each node (range) in the segment tree
    def update(self, index, val):
        
        def updateHelper(node):
            if node.s == node.e == index:
                node.total -= val
                node.mx -= val
                return

            m = (node.s + node.e) // 2
            if index <= m:
                updateHelper(node.left)
            elif index > m:
                updateHelper(node.right)
            node.mx = max(node.left.mx, node.right.mx)
            node.total = sum([node.left.total, node.right.total])
            return
            
        updateHelper(self.root)
        
    def maxQuery(self, k, maxRow, seats):
        
        def queryHelper(node):
            if node.s == node.e:
				# check if the row number is less than maxRow and the number of remains seats is greater or equal than k
                if node.e > maxRow or node.total < k:
                    return []
                if node.e <= maxRow and node.total >= k:
                    return [node.e, seats - node.total]
			# we want to greedily search the left subtree to get the smallest row which has enough remain seats
            if node.left.mx >= k:
                return queryHelper(node.left)
            return queryHelper(node.right)
        
        return queryHelper(self.root)
                
    def sumQuery(self, endRow):
        
        def queryHelper(node, left, right):
            if left <= node.s and node.e <= right:
                return node.total
            m = (node.s + node.e) // 2
            if right <= m:
                return queryHelper(node.left, left, right)
            elif left > m:
                return queryHelper(node.right, left, right)
            return queryHelper(node.left, left, m) + queryHelper(node.right, m+1, right)
        
        return queryHelper(self.root, 0, endRow)
```
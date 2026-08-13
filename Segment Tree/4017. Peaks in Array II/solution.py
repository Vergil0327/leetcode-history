# ===================================================================
#              Peaks in Array II - Segment Tree Approach
# ===================================================================

# 【1. Why Segment Tree Works (The Mathematical Magic)】

# For a query range [L, R], let the peaks strictly inside [L, R] be:
#     p_1 < p_2 < ... < p_t  (where L < p_k < R)

# The total number of valid peak subarrays in [L, R] is:
#   Total = (p_1 - L)(R - p_1) + ∑_{k=2}^t (p_k - p_{k-1})(R - p_k)

# Expanding and simplifying the algebra:
#   Total = R * p_t - L * R + L * p_1 - [ p_1^2 + ∑_{k=2}^t p_k * (p_k - p_{k-1}) ]
#         = R * (p_t - L) + L * p_1 - sum_val

# Where:
#   - p_1     = first peak in range
#   - p_t     = last peak in range
#   - sum_val = p_1^2 + ∑_{k=2}^t p_k * (p_k - p_{k-1})

# Notice that the outside predecessor q = prev(p_1) CANCELS OUT ENTIRELY!
# We do NOT need to look up any peaks outside [L, R]!


# 【2. Segment Tree Node Structure & O(1) Merge】

# Each node in the Segment Tree covers an index range [l, r] of peak candidates:

#   Node Attributes:
#     - cnt     : Total number of peaks in this node's range.
#     - first   : Index of the first peak (or -1 if cnt == 0).
#     - last    : Index of the last peak (or -1 if cnt == 0).
#     - sum_val : p_1^2 + ∑_{k=2}^t p_k * (p_k - p_{k-1})

#   Merging Left Child (A) and Right Child (B):
#     - If A.cnt == 0: return B
#     - If B.cnt == 0: return A
#     - Otherwise:
#         merged.cnt     = A.cnt + B.cnt
#         merged.first   = A.first
#         merged.last    = B.last
#         merged.sum_val = A.sum_val + B.sum_val - B.first * A.last

#   Why does `merged.sum_val` work like that?
#   In B, B.first was treated as the first peak, contributing B.first^2.
#   When merged with A, B.first's predecessor becomes A.last.
#   The new term is B.first * (B.first - A.last) = B.first^2 - B.first * A.last.
#   So we simply subtract B.first * A.last from A.sum_val + B.sum_val!


class Node:
    __slots__ = ('cnt', 'first', 'last', 'sum_val')
    def __init__(self, cnt=0, first=-1, last=-1, sum_val=0):
        self.cnt = cnt
        self.first = first
        self.last = last
        self.sum_val = sum_val

def merge(a: Node, b: Node) -> Node:
    if a.cnt == 0:
        return b
    if b.cnt == 0:
        return a
    res = Node()
    res.cnt = a.cnt + b.cnt
    res.first = a.first
    res.last = b.last  # Fixed: Must be b.last (from the right child)
    res.sum_val = a.sum_val + b.sum_val - b.first * a.last
    return res

class SegmentTree:
    def __init__(self, n: int, is_peak_fn):
        self.n = n
        self.tree = [Node() for _ in range(4 * n)]
        self._build(1, 0, n - 1, is_peak_fn)

    def _build(self, node: int, l: int, r: int, is_peak_fn):
        if l == r:
            if is_peak_fn(l):
                self.tree[node] = Node(1, l, l, l * l)
            return
        mid = (l + r) // 2
        self._build(2 * node, l, mid, is_peak_fn)
        self._build(2 * node + 1, mid + 1, r, is_peak_fn)
        self.tree[node] = merge(self.tree[2 * node], self.tree[2 * node + 1])

    def update(self, node: int, l: int, r: int, idx: int, is_peak: bool):
        if l == r:
            if is_peak:
                self.tree[node] = Node(1, idx, idx, idx * idx)
            else:
                self.tree[node] = Node(0, -1, -1, 0)
            return
        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, is_peak)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, is_peak)
        self.tree[node] = merge(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, node: int, l: int, r: int, ql: int, qr: int) -> Node:
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * node, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 1, mid + 1, r, ql, qr)
        left_node = self.query(2 * node, l, mid, ql, qr)
        right_node = self.query(2 * node + 1, mid + 1, r, ql, qr)
        return merge(left_node, right_node)


class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        def is_peak(i: int) -> bool:
            return 1 <= i <= n - 2 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1]

        seg_tree = SegmentTree(n, is_peak)
        ans = []

        for q in queries:
            if q[0] == 1:
                L, R = q[1], q[2]
                if L + 1 > R - 1:
                    ans.append(0)
                    continue

                res = seg_tree.query(1, 0, n - 1, L + 1, R - 1)
                if res.cnt == 0:
                    ans.append(0)
                else:
                    p1 = res.first
                    pt = res.last
                    total = R * (pt - L) + L * p1 - res.sum_val
                    ans.append(total)

            else:  # Type 2 Update: [2, index, val]
                idx, val = q[1], q[2]
                nums[idx] = val

                for i in (idx - 1, idx, idx + 1):
                    if 0 <= i < n:
                        seg_tree.update(1, 0, n - 1, i, is_peak(i))

        return ans
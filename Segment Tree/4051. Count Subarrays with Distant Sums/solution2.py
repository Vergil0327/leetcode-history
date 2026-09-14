"""
Algorithm Approach (Coordinate Compression + Segment Tree):
1. Compute prefix sums P where P[0] = 0.
2. Coordinate compress all unique values of P[x], P[x] - goal - k, and P[x] - goal + k.
3. Build a Segment Tree over the rank domain [1 .. MAX_RANK].
4. Iterate j from 0 to N:
   - For j > 0, query the Segment Tree for counts in ranges:
     a) Left range: [1, rank(P[j] - goal - k)]
     b) Right range: [rank(P[j] - goal + k), MAX_RANK]
     Add both query results to the answer.
   - Insert P[j] into the Segment Tree by calling point_update(rank(P[j]), +1).
"""
class SegmentTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, node: int, start: int, end: int, idx: int, val: int):
        if start == end:
            self.tree[node] += val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self.update(2 * node, start, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query(self, node: int, start: int, end: int, l: int, r: int) -> int:
        if l > end or r < start or l > r:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        left_sum = self.query(2 * node, start, mid, l, r)
        right_sum = self.query(2 * node + 1, mid + 1, end, l, r)
        return left_sum + right_sum


class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        n = len(nums)
        if k == 0:
            return n * (n + 1) // 2

        # 1. Compute Prefix Sums
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]

        # 2. Collect all values for Coordinate Compression
        vals = set()
        for x in P:
            vals.add(x)
            vals.add(x - goal - k)
            vals.add(x - goal + k)

        sorted_vals = sorted(vals)
        rank = {val: i + 1 for i, val in enumerate(sorted_vals)}
        num_ranks = len(sorted_vals)

        # 3. Process with Segment Tree
        seg_tree = SegmentTree(num_ranks)
        ans = 0

        for j in range(n + 1):
            if j > 0:
                current_p = P[j]
                val_A = current_p - goal - k
                val_B = current_p - goal + k

                idx_A = rank[val_A]
                idx_B = rank[val_B]

                # Count previous P[i] <= val_A  -> Range [1, idx_A]
                count_left = seg_tree.query(1, 1, num_ranks, 1, idx_A)
                # Count previous P[i] >= val_B  -> Range [idx_B, num_ranks]
                count_right = seg_tree.query(1, 1, num_ranks, idx_B, num_ranks)

                ans += count_left + count_right

            # Insert P[j] into Segment Tree
            seg_tree.update(1, 1, num_ranks, rank[P[j]], 1)

        return ans
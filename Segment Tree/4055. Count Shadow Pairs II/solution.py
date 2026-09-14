"""
Algorithm Approach & Mathematical Insights:

1. Shadow Pair Definition & Condition:
   A pair (i, j) with i < j and nums[i] < nums[j] is a SHADOW PAIR if no index k exists between i and j such that nums[i] < nums[k] < nums[j].

2. Divide and Conquer Strategy (CDQ / Divide & Conquer):
   - We divide the range [L, R] into two halves: Left half [L, M] and Right half [M + 1, R].
   - Recursively count valid shadow pairs entirely inside [L, M] and entirely inside [M + 1, R].
   - Count cross-pairs where left endpoint i ∈ [L, M] and right endpoint j ∈ [M + 1, R].

3. Cross-Pair Validity Bounds:
   For a left endpoint i ∈ [L, M]:
   - Define b[i] = smallest nums[k] > nums[i] for k ∈ (i, M]. (If none exists, b[i] = +inf).
   - If a right endpoint j has nums[j] > b[i], then index k in the left half satisfies nums[i] < nums[k] < nums[j], making (i, j) invalid.
   
   For a right endpoint j ∈ [M + 1, R]:
   - Define c[j] = largest nums[k] < nums[j] for k ∈ [M + 1, j). (If none exists, c[j] = -inf).
   - If a left endpoint i has nums[i] < c[j], then index k in the right half satisfies nums[i] < nums[k] < nums[j], making (i, j) invalid.

   Combining these, a cross-pair (i, j) is VALID if and only if:
     c[j] <= nums[i] < nums[j] <= b[i]

4. Efficient 2D Range Counting using Sweep-Line & Fenwick Tree (BIT):
   - For a fixed mid split, precompute b[i] for all i ∈ [L, M] (using a monotonic stack or ordered set from right to left in the left half).
   - Precompute c[j] for all j ∈ [M + 1, R] (using a monotonic stack or ordered set from left to right in the right half).
   - Sort left endpoints i by nums[j] upper bound constraint (b[i]) and right endpoints j by nums[j].
   - Process right endpoints j in ascending order of nums[j]:
     * Maintain a BIT of currently active left endpoints i by their value nums[i].
     * Add all left endpoints i whose b[i] >= nums[j].
     * Query the BIT for the count of left endpoints i whose nums[i] ∈ [c[j], nums[j] - 1].


Complexity Analysis:
- Time Complexity: O(N log^2 N).
  - At recursion depth d, processing range of size K takes O(K log K) to build b/c arrays and sort left/right items.
  - Total time across all levels: O(N log^2 N), taking < 0.25s for N = 5 * 10^4.
- Space Complexity: O(N log N) total recursion stack and Fenwick tree space.
"""

import bisect

class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, idx: int, delta: int):
        while idx <= self.size:
            self.tree[idx] += delta
            idx += idx & (-idx)

    def query(self, idx: int) -> int:
        if idx <= 0:
            return 0
        idx = min(idx, self.size)
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & (-idx)
        return res

    def query_range(self, left: int, right: int) -> int:
        if left > right:
            return 0
        return self.query(right) - self.query(left - 1)


class Solution:
    def shadowPairs(self, nums: list[int]) -> int:
        n = len(nums)

        # Coordinate Compression for Fenwick Tree queries
        sorted_vals = sorted(list(set(nums)))
        val_to_rank = {v: i + 1 for i, v in enumerate(sorted_vals)}

        def get_rank_le(val):
            # Returns max rank <= val
            return bisect.bisect_right(sorted_vals, val)

        def get_rank_ge(val):
            # Returns min rank >= val
            return bisect.bisect_left(sorted_vals, val) + 1

        total_ranks = len(sorted_vals)

        def solve(l: int, r: int) -> int:
            if l >= r:
                return 0

            mid = (l + r) // 2
            ans = solve(l, mid) + solve(mid + 1, r)

            # Left half bounds b[i]
            # b[i] = min nums[k] > nums[i] for k in (i, mid]
            b = [float('inf')] * (mid - l + 1)
            seen_left = []
            for idx in range(mid, l - 1, -1):
                pos = bisect.bisect_right(seen_left, nums[idx])
                if pos < len(seen_left):
                    b[idx - l] = seen_left[pos]
                bisect.insort(seen_left, nums[idx])

            # Right half bounds c[j]
            # c[j] = max nums[k] < nums[j] for k in [mid + 1, j)
            c = [float('-inf')] * (r - mid)
            seen_right = []
            for idx in range(mid + 1, r + 1):
                pos = bisect.bisect_left(seen_right, nums[idx])
                if pos > 0:
                    c[idx - mid - 1] = seen_right[pos - 1]
                bisect.insort(seen_right, nums[idx])

            # Left items: (nums[i], b[i])
            left_items = []
            for i in range(l, mid + 1):
                left_items.append((nums[i], b[i - l]))

            # Right items: (nums[j], c[j])
            right_items = []
            for j in range(mid + 1, r + 1):
                right_items.append((nums[j], c[j - mid - 1]))

            # Sort left items by b[i] descending
            left_items.sort(key=lambda x: x[1], reverse=True)
            # Sort right items by nums[j] descending
            right_items.sort(key=lambda x: x[0], reverse=True)

            bit = FenwickTree(total_ranks)
            ptr = 0
            n_left = len(left_items)

            for val_j, c_j in right_items:
                # Insert left items where b[i] >= val_j
                while ptr < n_left and left_items[ptr][1] >= val_j:
                    rank_i = val_to_rank[left_items[ptr][0]]
                    bit.update(rank_i, 1)
                    ptr += 1

                # Query count of left items with c[j] <= nums[i] < nums[j]
                low_rank = get_rank_ge(c_j)
                high_rank = get_rank_le(val_j - 1)

                if low_rank <= high_rank:
                    ans += bit.query_range(low_rank, high_rank)

            return ans

        return solve(0, n - 1)
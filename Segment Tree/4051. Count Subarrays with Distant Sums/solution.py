"""
Mathematical Reformulation & Key Insight:
A subarray nums[i..j] (0 <= i <= j < N) has sum S(i, j) = P[j + 1] - P[i], where P is the prefix sum array of size N + 1 with P[0] = 0.
The condition for a subarray to be distant is:
  |S(i, j) - goal| >= k

Expanding the absolute value inequality:
  P[j + 1] - P[i] <= goal - k  OR  P[j + 1] - P[i] >= goal + k

Rearranging for the earlier prefix sum P[i] (where i < j + 1):
  P[i] <= P[j + 1] - goal - k   OR   P[i] >= P[j + 1] - goal + k

Corner Case:
If k == 0, the absolute difference |S(i, j) - goal| >= 0 is always true for every valid subarray.
Thus, when k == 0, the answer is simply the total number of subarrays: N * (N + 1) // 2.

Algorithm Approach (Coordinate Compression + Fenwick Tree / BIT):
1. Compute the prefix sum array P of length N + 1 where P[0] = 0.

2. Collect all target query values for Coordinate Compression:
   For every prefix sum P[x]:
     - Add P[x]
     - Add P[x] - goal - k  (upper bound for left range)
     - Add P[x] - goal + k  (lower bound for right range)
   Sort and deduplicate these values to assign each a unique 1-based rank index.

3. Process prefix sums from left to right (j from 0 to N):
   - For j > 0, query the Fenwick Tree (BIT) for:
     a) Count of previous prefix sums P[i] <= P[j] - goal - k
     b) Count of previous prefix sums P[i] >= P[j] - goal + k
     Add (count_a + count_b) to the total answer.
   - Insert the rank of current prefix sum P[j] into the Fenwick Tree.

Complexity Analysis:
- Time Complexity: O(N log N) for sorting coordinate compression values and performing O(log N) BIT operations across N + 1 prefix sums.
- Space Complexity: O(N) auxiliary space to store prefix sums, rank maps, and the BIT array.
"""
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

        # 3. Process with BIT
        bit = FenwickTree(len(sorted_vals))
        ans = 0

        for j in range(n + 1):
            if j > 0:
                current_p = P[j]
                val_A = current_p - goal - k
                val_B = current_p - goal + k

                idx_A = rank[val_A]
                idx_B = rank[val_B]

                # Count previous P[i] <= val_A
                count_left = bit.query(idx_A)
                # Count previous P[i] >= val_B
                count_right = bit.query_range(idx_B, len(sorted_vals))

                ans += count_left + count_right

            # Insert P[j] into BIT
            bit.update(rank[P[j]], 1)

        return ans
"""
Two Cases for Subarrays Ending at Index i:
Assume you're at index i looking at all subarrays that end at i. Those subarrays are:

nums[0..i], nums[1..i], nums[2..i], ..., nums[i..i]

Now suppose nums[i] was last seen at index p.

We divide all subarrays ending at i into two types:

1. Subarrays that start after the last occurrence of nums[i]
These are subarrays [k..i] where k > p (or k >= p + 1).

In these subarrays, nums[i] is not seen before, so it becomes a new distinct element.

So distinct count increases by 1 in these.

This is the part that i - last_idx + 1 is accounting for.

2. Subarrays that start before or at the last occurrence of nums[i]
These are subarrays [k..i] where k <= p.

In these subarrays, nums[i] has already appeared, so it's not a new distinct value.

But we still need to square the new distinct count.

Here’s the trick: if we previously computed distinct count d for these subarrays [k..i-1], now they are extended by nums[i] at index i. Since nums[i] already appeared in them, the number of distinct elements stays the same (d), so the squared value doesn’t change because of the distinct count increasing.

But we are computing the square of distinct counts of subarrays ending at i, and we need to update the total result accordingly.

Now how do we compute:

(d)^2 → already included in curr_res

Now we are including [k..i] — a new subarray, same distinct count d, so we add d^2 again.

But this doubling of contribution is done efficiently using the segment tree.

That's what the segment tree is helping with: quickly getting the sum of distinct counts of subarrays starting between last_idx and i, which can be reused (and squared via the formula).

Final Clarification of the Formula:

curr_res += (i - last_idx + 1)       # New subarrays where nums[i] is a new distinct element
             + 2 * segment_tree.query(last_idx, i + 1)
             # Add the 2*d term from (d + 1)^2 = d^2 + 2d + 1

So the "increment distinct count" phrasing was confusing — a better explanation is:

We're using the query to account for the 2*d term in the identity (d+1)^2 = d^2 + 2d + 1, for the subarrays that are extended by including nums[i], and nums[i] acts as a new distinct element in some, and a duplicate in others — but in either case, the total square changes, and we must update accordingly.


Let p = last_idx_dict[num] (last index where nums[i] appeared).

So nums[i] was last seen at p. We are at i now.

Subarrays ending at i are [k..i] where k ∈ [0, i].

We split them into:

Type A: k ∈ [0, p] → nums[i] is already in the subarray → distinct count stays d

Type B: k ∈ [p+1, i] → nums[i] is new in the subarray → distinct count becomes d+1

We want to compute the sum of squares of the distinct counts of all [k..i] subarrays.

Let’s go deeper:
Let:

S_A be the sum of squares of distinct counts for Type A subarrays.

S_B be the sum of squares of distinct counts for Type B subarrays.

We want to compute:

curr_res += S_A_new + S_B_new

For Type A ([k..i] with k ≤ p):
Distinct count is same as [k..i−1], say d.

So for [k..i], we are repeating this subarray with same distinct count → we add d^2 again.

But we already stored d (not d^2) in the segment tree.

So to efficiently compute 2*d for later squaring (as per the identity), we use this clever trick:

Instead of storing and summing d^2 directly, we maintain an expression that leads to the correct square when accumulated.

In particular:

The change in square is:
(d+1)^2 - d^2 = 2d + 1

This leads us to a formula that accumulates the difference:

delta = (i - p)        # count of Type B subarrays
      + 2 * segment_tree.query(p+1, i+1)  # sum of distinct counts (d) of Type B subarrays

But in the code, the segment tree stores the value in index range [p+1, i+1).
So the code actually does:

segment_tree.query(last_idx, i+1)
Because last_idx = p + 1.

So combining everything:

Final Expression Justified

curr_res += (i - last_idx + 1) + 2 * segment_tree.query(last_idx, i + 1)
Where:

(i - last_idx + 1) is the number of new subarrays ([p+1..i]) where nums[i] becomes a new distinct element. These subarrays add +1 to their square.

segment_tree.query(...) returns the sum of distinct counts for these subarrays, giving us the 2d part.

This expression is computing:

sum((d+1)^2 - d^2) = sum(2d + 1) = 2 * sum(d) + count
over the Type B subarrays. Which is exactly what this line of code is doing.

TL;DR
You can think of:

curr_res += (i - last_idx + 1) + 2 * segment_tree.query(last_idx, i + 1)
as computing the total change in sum-of-squares due to nums[i] appearing again, with:

+1 added to each Type B subarray's square

2d added due to the increased distinct count

This gives us the efficient way to maintain the sum of squares incrementally, without recomputing all subarrays.
"""
MOD = 1_000_000_007  # Modulo as the result can be large

class SegmentTreeNode:
    def __init__(self, lo, hi) -> None:
        self.lo = lo  # start index of the range this node represents
        self.hi = hi  # end index of the range this node represents (exclusive)
        self.val = 0  # stores sum of values in the range
        self.lazy = 0  # used for lazy propagation (postponed updates)

        # Recursively build the left and right children if the segment size is greater than 1
        if lo + 1 < hi:
            mid = (lo + hi) // 2
            self.left = SegmentTreeNode(lo, mid)
            self.right = SegmentTreeNode(mid, hi)
    def update(self, val):
        """
        Apply lazy update to the current node: add `val` to the entire range this node covers.
        """
        self.lazy += val
        self.val += val * (self.hi - self.lo)  # apply value to range length
    def query(self, lo, hi):
        """
        Query the sum in the range [lo, hi), and apply a lazy update (+1) to that same range.
        """
        # If the current node's range is fully inside the query range
        if self.lo >= lo and self.hi <= hi:
            res = self.val  # save current value
            self.update(1)  # apply +1 update to current node (lazy)
            return res

        # Propagate any pending lazy updates to children before proceeding
        mid = (self.lo + self.hi) // 2
        res = 0
        self.left.update(self.lazy)
        self.right.update(self.lazy)
        self.lazy = 0  # Clear lazy after propagating

        # Recurse into left and/or right children based on the query range
        if lo < mid:
            res += self.left.query(lo, hi)
        if hi > mid:
            res += self.right.query(lo, hi)

        # Update current node value after child queries
        self.val = self.left.val + self.right.val
        return res

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        last_idx_dict = {}  # To track last seen index of each number
        segment_tree = SegmentTreeNode(0, len(nums))  # Build segment tree over indices
        res = 0            # Final result: sum of squares of distinct counts
        curr_res = 0       # Current running total of squares

        for i, num in enumerate(nums):
            # Get the index just after the last occurrence of `num`
            # If it's the first time seeing `num`, use 0 as the start
            last_idx = last_idx_dict.get(num, -1) + 1

            # Calculate the contribution of subarrays ending at index i
            # Explanation:
            # - (i - last_idx + 1): number of new subarrays where `num` is added as a new distinct value
            # - segment_tree.query(last_idx, i + 1): sum of distinct counts in previous subarrays
            #   that get one more distinct number by adding current `num`
            # - We double the value from segment tree because:
            #   (a + 1)^2 = a^2 + 2a + 1 => the +2a part comes from the new value added
            curr_res = (
                curr_res + i - last_idx + 1 + 2 * segment_tree.query(last_idx, i + 1)
            ) % MOD

            res = (res + curr_res) % MOD  # Add to final result
            last_idx_dict[num] = i  # Update last index of current number

        return res % MOD

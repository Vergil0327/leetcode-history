# Intuition

嘗試用了sliding window, greedy都解不了
後來發現這題可以用binary search去猜測minimum possible stability factor

如果當前測試`mid`長度, 能符合數量少於等於`maxC`時, 代表我們就能透過`maxC`次來將這些合法的subarray給破壞掉

We need to find the smallest possible longest stable subarray length after at most maxC modifications. Equivalently, for any candidate length L, we can reframe this problem by askisng: “If every subarray of length L whose GCD ≥2 must be ‘broken’ by changing at least one element, how many such disjoint subarrays do we encounter?” If that count is ≤ maxC, then it’s feasible to force the maximum stable‐subarray length down to L. This feasibility check is monotonic in L, so we can binary‐search on L.

[solution](https://leetcode.com/problems/minimum-stability-factor-of-array/solutions/6924818/binary-search-on-stability-factor)
1. Binary search on length L in [0..n].

2. For each L, run `count(L)`:

    - Slide a window start i from 0 to n−L.
    - Compute the GCD of nums[i..i+L−1].
    - If the GCD >1, increment count and advance i += L (we “break” that entire block with one modification).
    - Otherwise advance i += 1.
3. If getCount(L) ≤ maxC, we can succeed with length L or smaller; otherwise we must increase L.

Return the largest L for which the check fails, i.e. the minimum achievable stability factor.

但由於GCD計算耗費O(n^2), 所以這邊需要用到另個技巧來加速GCD Query: Sparse Table

- Sparse Table gives you O(1) GCD range queries after O(n log n) preprocessing.

- Perfect for static arrays, no updates.

"""
### Problem Breakdown & Mathematical Logic

For each starting index $k \in [0, m - n]$, let $W = \text{target}[k \dots k + n - 1]$ be the window of length $n$.
We want to count the number of suffix-start indices $i \in [0, n - 1]$ such that sorting $\text{nums}[i \dots n - 1]$ in non-increasing order produces $W$.

An index $i$ is valid for window $W$ if and only if three conditions hold:

1. **Total Multiset Equality:**
   Sorting elements only rearranges them. Thus, $W$ and $\text{nums}$ must have the exact same multiset of elements. If their multisets differ, 0 indices can produce $W$.

2. **Prefix Invariance (Upper Bound on $i$):**
   The prefix $\text{nums}[0 \dots i - 1]$ is untouched by the suffix sort, so it must strictly match $W[0 \dots i - 1]$.
   Let $l = \text{LCP}(\text{nums}, W)$ be the length of the longest common prefix:
   - If $l < n$, then $\text{nums}[l] \ne W[l]$, meaning the prefix can extend at most up to index $l - 1$. Hence, $i \le l$.
   - If $l = n$ ($\text{nums} == W$), then $i$ can be any index up to $n - 1$.
   Therefore:
   $$\text{first\_diff} = \min(l, n - 1)$$
   The condition $\text{nums}[0 \dots i - 1] == W[0 \dots i - 1]$ is satisfied if and only if:
   $$i \le \text{first\_diff}$$

3. **Suffix Monotonicity (Lower Bound on $i$):**
   Because the suffix is sorted in non-increasing order, the resulting suffix $W[i \dots n - 1]$ must already be non-increasing ($W[j] \ge W[j + 1]$ for all $j \ge i$).
   Let $\text{min\_non\_inc}$ be the smallest index such that $W[\text{min\_non\_inc} \dots n - 1]$ is non-increasing.
   The suffix is non-increasing if and only if:
   $$i \ge \text{min\_non\_inc}$$

Combining these conditions:
For any window $W$ whose multiset matches $\text{nums}$, the valid indices $i$ are precisely those in the interval:
$$[\text{min\_non\_inc}, \text{first\_diff}]$$
The count of valid indices is:
$$\max(0, \text{first\_diff} - \text{min\_non\_inc} + 1)$$

---

### $O(n + m)$ Global Precomputation Strategy

Instead of recalculating for each window $W$ from scratch:

1. **Multiset Matching in $O(1)$ per Window:**
   Maintain a frequency difference array `diff` of size $\max(nums, target) + 1 \le 100,005$ and a counter `mismatched` tracking how many values have non-zero differences. As $k$ advances, we slide the window by adding the incoming element and removing the outgoing element in $O(1)$ time.

2. **LCP in $O(1)$ via the Z-Algorithm:**
   Construct $S = \text{nums} + [-1] + \text{target}$. 
   Run the standard Z-algorithm on $S$. For window $k$, the LCP between $\text{nums}$ and $\text{target}[k \dots]$ is given directly by:
   $$l = \min(n, Z[n + 1 + k])$$

3. **$\text{min\_non\_inc}$ in $O(1)$ via Last Inversion Index:**
   A violation in $W$ occurs where $W[p] < W[p + 1] \iff \text{target}[k + p] < \text{target}[k + p + 1]$.
   Precompute `last_inc[idx]`: the largest index $q \le idx$ such that $\text{target}[q] < \text{target}[q + 1]$.
   For window $k$, the last violation in range $[k, k + n - 2]$ is at:
   $$q = \text{last\_inc}[k + n - 2]$$
   - If $q \ge k$, the last violation is inside $W$, so $\text{min\_non\_inc} = q - k + 1$.
   - If $q < k$, there are no violations in $W$, so $\text{min\_non\_inc} = 0$.
"""
class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> list[int]:
        n = len(nums)
        m = len(target)
        
        # 1. Z-algorithm to compute LCP between nums and target[k...]
        # Delimiter -1 never appears in nums or target (values >= 1)
        S = nums + [-1] + target
        L_S = len(S)
        Z = [0] * L_S
        l, r = 0, 0
        for i in range(1, L_S):
            if i <= r:
                Z[i] = min(r - i + 1, Z[i - l])
            while i + Z[i] < L_S and S[Z[i]] == S[i + Z[i]]:
                Z[i] += 1
            if i + Z[i] - 1 > r:
                l = i
                r = i + Z[i] - 1
                
        # 2. Precompute last_inc: largest index q <= idx such that target[q] < target[q + 1]
        last_inc = [-1] * m
        cur_last = -1
        for i in range(m - 1):
            if target[i] < target[i + 1]:
                cur_last = i
            last_inc[i] = cur_last
        last_inc[m - 1] = cur_last
        
        # 3. Sliding window frequency tracking for multiset matching
        max_val = max(max(nums), max(target))
        diff = [0] * (max_val + 1)
        for v in nums:
            diff[v] -= 1
            
        mismatched = 0
        for v in range(max_val + 1):
            if diff[v] != 0:
                mismatched += 1
                
        # Initialize window of length n
        for i in range(n):
            v = target[i]
            if diff[v] == 0:
                mismatched += 1
            diff[v] += 1
            if diff[v] == 0:
                mismatched -= 1
                
        ans = [0] * (m - n + 1)
        
        # 4. Process all windows k in [0, m - n]
        for k in range(m - n + 1):
            if k > 0:
                # Remove target[k - 1]
                out_v = target[k - 1]
                if diff[out_v] == 0:
                    mismatched += 1
                diff[out_v] -= 1
                if diff[out_v] == 0:
                    mismatched -= 1
                    
                # Add target[k + n - 1]
                in_v = target[k + n - 1]
                if diff[in_v] == 0:
                    mismatched += 1
                diff[in_v] += 1
                if diff[in_v] == 0:
                    mismatched -= 1
            
            # If the window has the identical multiset of elements
            if mismatched == 0:
                lcp = min(n, Z[n + 1 + k])
                first_diff = min(lcp, n - 1)
                
                if n == 1:
                    min_non_inc = 0
                else:
                    q = last_inc[k + n - 2]
                    min_non_inc = (q - k + 1) if q >= k else 0
                
                if first_diff >= min_non_inc:
                    ans[k] = first_diff - min_non_inc + 1
                    
        return ans

    
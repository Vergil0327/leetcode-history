"""
Mo’s Algorithm (or Query Square Root Decomposition) is an offline algorithm used in competitive programming to answer multiple range queries on a static array in $O((N + Q) \sqrt{N})$ time.It applies to problems where:
The array is static (no updates/modifications).
The queries are known in advance (offline processing is allowed).
Transitioning from a range $[L, R]$ to $[L \pm 1, R]$, $[L, R \pm 1]$ can be done efficiently in $O(1)$ time.

Core Idea
If you process $Q$ queries sequentially by moving two pointers ($l$ and $r$) from one query's range $[L_1, R_1]$ to the next $[L_2, R_2]$, the pointers might jump back and forth across the array, taking $O(N)$ time per query ($O(N \cdot Q)$ total).
Mo’s Algorithm optimizes this by reordering the queries to minimize the total distance traveled by the $l$ and $r$ pointers.
Divide the array of size $N$ into blocks of size $B = \lceil\sqrt{N}\rceil$.
Sort the queries based on:
    Primary Key: The block index of $L$ ($\lfloor L / B \rfloor$).
    Secondary Key: $R$ in ascending order (or descending if using Hilbert curve/zig-zag optimization).
Maintain two pointers, $l$ and $r$, and expand/shrink the window element-by-element to answer each sorted query.
Why the Time Complexity is $O((N + Q) \sqrt{N})$$R$ Pointer Movement:For a fixed $L$-block, $R$ increases monotonically from $0$ to $N$.Across all $\sqrt{N}$ blocks, $R$ moves at most $O(N)$ times per block.Total $R$ moves: $O(N \sqrt{N})$.$L$ Pointer Movement:Within the same $L$-block, $L$ can jump at most $B = \sqrt{N}$ positions per query.Across $Q$ queries, total $L$ moves: $O(Q \sqrt{N})$.

Algorithm Approach:
As suggested by the hints, since queries can be processed offline and moving range endpoints L and R by 1 takes O(1) time, we can use Mo's Algorithm.

1. State Tracking:
   - 'freq[x]': Frequency of element x in the current range [cur_l, cur_r].
   - 'distinct_count': Number of elements x with freq[x] > 0.
   - 'odd_count': Number of elements x with freq[x] % 2 != 0.

2. Range Modifications (O(1)):
   - add(x):
     - If freq[x] == 0, increment distinct_count.
     - Increment freq[x].
     - Update odd_count: if freq[x] becomes odd, increment odd_count; if it becomes even, decrement odd_count.
   - remove(x):
     - Decrement freq[x].
     - If freq[x] == 0, decrement distinct_count.
     - Update odd_count: if freq[x] becomes odd, increment odd_count; if it becomes even, decrement odd_count.

3. Query Validity:
   A range is valid if and only if:
   - distinct_count == k
   - odd_count == 0

4. Sorting Queries:
   Block size = N / sqrt(Q). Sort queries by (L // block_size, R) with zig-zag parity optimization.

Complexity Analysis:
- Time Complexity: O((N + Q) * sqrt(N)), where N <= 10^5 and Q <= 10^5.
  - Sorting queries takes O(Q log Q).
  - Mo's pointer movements take O((N + Q) * sqrt(N)).
- Space Complexity: O(N + Q) to store query structures and frequency array.
"""
import math

class Solution:
    def validSubarrays(self, nums: list[int], k: int, queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        q = len(queries)
        
        block_size = max(1, int(n / math.sqrt(q)))
        
        # Prepare queries with indices
        sorted_queries = []
        for i, (l, r) in enumerate(queries):
            sorted_queries.append((l // block_size, l, r, i))
            
        # Sort queries using Mo's Ordering
        sorted_queries.sort(key=lambda x: (x[0], x[2] if x[0] % 2 == 0 else -x[2]))
        
        max_val = max(nums) if nums else 0
        freq = [0] * (max_val + 1)
        
        distinct_count = 0
        odd_count = 0
        
        def add(x):
            nonlocal distinct_count, odd_count
            if freq[x] == 0:
                distinct_count += 1
            freq[x] += 1
            if freq[x] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
                
        def remove(x):
            nonlocal distinct_count, odd_count
            if freq[x] % 2 == 1:
                odd_count -= 1
            else:
                odd_count += 1
            freq[x] -= 1
            if freq[x] == 0:
                distinct_count -= 1

        ans = [False] * q
        cur_l = 0
        cur_r = -1
        
        for block, l, r, original_idx in sorted_queries:
            while cur_l > l:
                cur_l -= 1
                add(nums[cur_l])
            while cur_r < r:
                cur_r += 1
                add(nums[cur_r])
            while cur_l < l:
                remove(nums[cur_l])
                cur_l += 1
            while cur_r > r:
                remove(nums[cur_r])
                cur_r -= 1
                
            ans[original_idx] = (distinct_count == k and odd_count == 0)
            
        return ans
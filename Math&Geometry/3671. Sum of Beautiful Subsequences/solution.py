# solution from [Alex Wice](https://leetcode.com/problems/sum-of-beautiful-subsequences/solutions/7140297/python-sieve)

class Fenwick:
    def __init__(self, n):
        self.a = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.a[i]
            i -= i & -i
        return s

    def add(self, i, delta):
        while i < len(self.a):
            self.a[i] += delta
            i += i & -i

class Solution:
    """
    1. Position-Based Processing
    Instead of working with values directly, we work with positions. This naturally handles the "strictly increasing subsequence" constraint - if position i < position j, then we have a valid subsequence structure.
    
    2. Decreasing Value Order
    The crucial optimization is processing values in decreasing order:

    When we process value v, all larger values have already been processed
    This ensures that when we add ways for positions with value v, we're correctly extending subsequences that end with larger values
    The Fenwick tree accumulates ways from positions with larger values

    3. Reverse Position Order Within Same Value
    For positions with the same value, we process in reverse order to avoid double-counting the same position in our Fenwick tree updates.

    4. Time Complexity Optimization

    Previous TLE approach: O(max_val x n log n) - checked every possible GCD
    New approach: O(max_val x n log n) but with much better constants since we process each position exactly once per divisor

    The key insight is that by processing values in decreasing order and using position-based ranking, we can efficiently count strictly increasing subsequences while maintaining the GCD constraint.
    The inclusion-exclusion principle then gives us the exact count for each GCD value.
    """
    def totalBeauty(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        M = max(nums) + 1
        locs = defaultdict(list)
        for i, x in enumerate(nums):
            locs[x].append(i)

        F = [0] * M
        for d in range(1, M):
            indices = sorted(i for v in range(d, M, d) for i in locs[v])
            if len(indices) <= 1:
                F[d] = len(indices)
                continue

            rank = {pos: r for r, pos in enumerate(indices, 1)}
            fen = Fenwick(len(indices))
            for v in range(d, M, d):
                for pos in reversed(locs[v]):
                    r = rank[pos]
                    addend = 1 + fen.sum(r - 1)
                    F[d] += addend
                    fen.add(r, addend)

        for d in range(M - 1, 0, -1):
            for e in range(2 * d, M, d):
                F[d] -= F[e]
            F[d] %= MOD

        return sum(d * F[d] for d in range(1, M)) % MOD

# solution from @Cartographer24
from typing import List
import math

MOD = 10**9 + 7

class Fenwick:
    # 1-indexed BIT for sums mod MOD
    def __init__(self, size: int):
        self.n = size
        self.bit = [0] * (size + 1)

    def add(self, idx: int, delta: int) -> None:
        while idx <= self.n:
            self.bit[idx] = (self.bit[idx] + delta) % MOD
            idx += idx & -idx

    def sum(self, idx: int) -> int:
        s = 0
        while idx > 0:
            s += self.bit[idx]
            if s >= MOD:
                s -= MOD
            idx -= idx & -idx
        return s


class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        if not nums:
            return 0

        maxA = max(nums)

        # Cache divisors for values we actually see (trial division is fine at this scale)
        div_cache = {}

        def divisors(x: int) -> List[int]:
            if x in div_cache:
                return div_cache[x]
            ds = []
            r = int(math.isqrt(x))
            for d in range(1, r + 1):
                if x % d == 0:
                    ds.append(d)
                    if d * d != x:
                        ds.append(x // d)
            ds.sort()
            div_cache[x] = ds
            return ds

        # Fenwick per g, created on demand. Size for g-world is floor(maxA / g).
        bits = {}  # g -> Fenwick
        # F[g] = number of strictly increasing subsequences whose elements are multiples of g
        F = [0] * (maxA + 1)

        # Process nums left-to-right
        for val in nums:
            for g in divisors(val):
                w = val // g
                # build BIT for g on first use
                if g not in bits:
                    bits[g] = Fenwick(maxA // g)
                ft = bits[g]
                # ways to end an increasing subsequence here in g-world
                smaller = ft.sum(w - 1)  # subsequences ending with values < w
                ways = (1 + smaller) % MOD  # +1 for the singleton [val] in this g-world
                F[g] = (F[g] + ways) % MOD
                ft.add(w, ways)

        # Convert F (gcd multiple of g) -> exact counts per gcd via inclusion–exclusion
        exact = [0] * (maxA + 1)
        for g in range(maxA, 0, -1):
            if F[g] == 0:
                continue
            s = F[g]
            for m in range(g * 2, maxA + 1, g):
                if exact[m]:
                    s -= exact[m]
            exact[g] = s % MOD

        # Sum beauty = Σ g * exact[g]
        ans = 0
        for g in range(1, maxA + 1):
            if exact[g]:
                ans = (ans + g * exact[g]) % MOD
        return ans

##########################################
# TLE Solution - but you can see the idea
##########################################

class FenwickTree:
    def __init__(self, n, mod):
        self.MOD = mod
        self.n = n
        self.tree = [0] * (n + 1)
    
    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] = (self.tree[i] + delta) % self.MOD
            i += i & (-i)
    
    def query(self, i):
        res = 0
        while i > 0:
            res = (res + self.tree[i]) % self.MOD
            i -= i & (-i)
        return res

class Solution:
    def totalBeauty(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # Count strictly increasing subsequences
        def count_increasing_subsequences(arr):
            if not arr: return 0
            
            # Coordinate compression
            sorted_vals = sorted(set(arr))
            rank = {val: i + 1 for i, val in enumerate(sorted_vals)}
            
            ft = FenwickTree(len(sorted_vals), MOD)
            total = 0
            
            for num in arr:
                r = rank[num]
                # Ways to extend existing subsequences + this element as singleton
                ways = (ft.query(r - 1) + 1) % MOD
                ft.update(r, ways)
                total = (total + ways) % MOD
            
            return total
        
        # Step 1: For each g, count subsequences with GCD being a multiple of g
        cnt = {}
        for g in range(1, max_val + 1):
            # Filter elements divisible by g and scale down
            filtered = []
            for num in nums:
                if num % g == 0:
                    filtered.append(num // g)
            
            cnt[g] = count_increasing_subsequences(filtered)
        
        # Step 2: Use inclusion-exclusion to get exactly g
        F = {}
        for g in range(max_val, 0, -1):  # Process from max down to 1
            F[g] = cnt[g]
            # Subtract overcounted multiples
            for k in range(2 * g, max_val + 1, g):
                F[g] = (F[g] - F[k]) % MOD
        
        # Step 3: Calculate final answer
        result = 0
        for g in range(1, max_val + 1):
            result = (result + g * F[g]) % MOD
        
        return result

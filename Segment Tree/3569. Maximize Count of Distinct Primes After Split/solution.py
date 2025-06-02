# Precompute primes using Sieve of Eratosthenes
def generatePrimeUntil(n: int):
    isPrime = [0, 0] + [1] * (n-2)

    for i in range(2, int(sqrt(n))+1):
        if not isPrime[i]: continue
        # all the factors before i*i have been considered at i-1, i-2, ..., 3, 2
        for j in range(i*i, n, i):
            isPrime[j] = 0
    return isPrime
        
N = 100000
is_prime = generatePrimeUntil(N+1)

"""
solution by @Abhishek Choudhary
https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/solutions/6801912/lazy-segment-tree-to-maintain-count-dynamically
"""
class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        self._default = default
        self._func = func # `func` can be max, min, or sum depending on use-case
        self._len = len(data)
        self._size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * self._size)
        self.data = [default] * (2 * self._size)
        self.data[self._size:self._size + self._len] = data
        for i in range(self._size - 1, 0, -1):
            self.data[i] = func(self.data[2 * i], self.data[2 * i + 1])

    def _push(self, idx):
        # Push lazy updates down the tree
        q = self._lazy[idx]
        if q:
            self._lazy[2 * idx] += q
            self._lazy[2 * idx + 1] += q
            self.data[2 * idx] += q
            self.data[2 * idx + 1] += q
            self._lazy[idx] = 0

    def _update(self, idx):
        # Apply pending lazy updates from ancestors
        for h in range(idx.bit_length() - 1, 0, -1):
            self._push(idx >> h)

    def _build(self, idx):
        # Rebuild data going upward
        while idx > 1:
            idx >>= 1
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]

    def add(self, l, r, v):
        # Add `v` to the range [l, r)
        l0, r0 = l + self._size, r + self._size
        l1, r1 = l0, r0
        while l0 < r0:
            if l0 & 1:
                self._lazy[l0] += v
                self.data[l0] += v
                l0 += 1
            if r0 & 1:
                r0 -= 1
                self._lazy[r0] += v
                self.data[r0] += v
            l0 >>= 1
            r0 >>= 1
        self._build(l1)
        self._build(r1 - 1)

    def query(self, l, r):
        # Query for maximum in range [l, r)
        l += self._size
        r += self._size
        self._update(l)
        self._update(r - 1)
        res = self._default
        while l < r:
            if l & 1:
                res = self._func(res, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                res = self._func(res, self.data[r])
            l >>= 1
            r >>= 1
        return res

class Solution:
    def maximumCount(self, nums, queries):
        n = len(nums)
        self.nums = [0] * n

        # Track indices for each prime value using SortedList
        self.pos = defaultdict(lambda: SortedList([-1, n]))
        
        # Segment tree to maintain active prime count at each split
        self.st = LazySegmentTree([0] * (n + 1))

        def update(idx, val):
            old = self.nums[idx]
            
            # Remove old value if it's prime
            if is_prime[old]:
                lst = self.pos[old]
                i = lst.bisect_left(idx)
                prv = lst[i-1]
                nxt = lst[i+1]

                # Remove its contribution to segment tree
                # These are needed because we track each prime as an active range from its first to last occurrence.
                if prv == -1:
                    # If idx was the first occurrence of `old`, remove [idx+1, nxt+1)
                    self.st.add(idx+1, nxt+1, -1)
                if nxt == n:
                    # If idx was the last occurrence, remove [prv+1, idx+1)
                    self.st.add(prv+1, idx+1, -1)
                lst.remove(idx)

            # Set new value and add new value if it's prime
            self.nums[idx] = val
            if is_prime[val]:
                lst = self.pos[val] # All positions where this prime occurs
                lst.add(idx) # Find index of `idx` in the list
                i = lst.bisect_left(idx)
                prv = lst[i-1] # previous occurrence
                nxt = lst[i+1] # next occurrence
                
                # Add its contribution
                if prv == -1:
                    self.st.add(idx+1, nxt+1, 1)
                if nxt == n:
                    self.st.add(prv+1, idx+1, 1)
        for i, v in enumerate(nums):
            update(i, v)
        res = []
        for idx, val in queries:
            update(idx, val)
            res.append(self.st.query(1, n)) # Valid split is from 1 to n-1
        return res
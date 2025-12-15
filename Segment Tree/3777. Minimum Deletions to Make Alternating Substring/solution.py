"""
# Intuition

The solution uses a Segment Tree to efficiently count "violations",
which are adjacent identical characters ('AA' or 'BB').
The total number of violations is the minimum number of deletions needed.

Explanation

Transform s to a 0-1 array. If A[i] == A[i - 1], then it needs one operation to remove A[i]

We use a Segment Tree.

- It stores the count of violations at each position.
- This allows for fast updates and queries.

### Query [2, l, r] Range Sum

- This is a range sum query.
- We calculate segment_tree.query(l+1, r) to find the number of violations within the substring s[l+1..r]

### Query [1, i] Flip

- Flipping the character at s[i] only affects its neighbors.
- We update the Segment tree at positions i and i+1 accordingly:
    - add 1 if a new violation is created,
    - or -1 if one is removed.
"""

class SegmentTree():
    def __init__(self, A, op=sum):
        n = len(A)
        self.st = st = ([0]*n+A)
        for i in range(n-1, 0, -1):
            st[i] = op([st[i<<1], st[i<<1|1]])
        self.op = op
        self.n = n

    def __getitem__(self, i):
        return self.st[i+self.n]

    def __setitem__(self, i, v):
        st, op, n = self.st, self.op, self.n
        i += n
        st[i] = v
        while i:
            st[i>>1] = op([st[i], st[i^1]])
            i >>= 1

    def query(self, l, r):
        st, op , n = self.st, self.op, self.n
        l, r = l+n, r+n
        res = 0
        while l <= r:
            if l == r:
                res = op([res, st[l]])
                break
            if l&1 == 1:
                res = op([res, st[l]])
                l += 1
            if r&1 == 0:
                res = op([res, st[r]])
                r -= 1
            l, r = l >> 1, r >> 1
        return res

class Solution:
    def minDeletions(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        arr = [ord(c) - ord('A') for c in s]
        
        st = SegmentTree([0] * n)
        
        # Initialize: mark positions where arr[i] == arr[i-1]
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                st[i] = 1
        
        res = []
        for query in queries:
            if query[0] == 1:
                i = query[1]
                arr[i] = 1 - arr[i]
                
                # Update position i (comparison with left neighbor)
                if i > 0:
                    st[i] = 1 if arr[i] == arr[i - 1] else 0
                
                # Update position i+1 (comparison with current position)
                if i < n - 1:
                    st[i + 1] = 1 if arr[i] == arr[i + 1] else 0  # ✅ Fixed!
            else:
                l, r = query[1], query[2]
                # Query [l+1, r] because we store "equal to previous" at each position
                if l + 1 <= r:
                    res.append(st.query(l + 1, r))
                else:
                    res.append(0)
        
        return res
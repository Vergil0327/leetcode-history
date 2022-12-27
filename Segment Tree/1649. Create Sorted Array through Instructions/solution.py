from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9+7
        nums = SortedList()
        cost = 0
        for num in instructions:
            i = nums.bisect_left(num)
            j = nums.bisect_right(num)
            n = len(nums)
            nums.add(num)
        
            cost += min(i, n-j)
            cost %= MOD
        return cost

# Brute Force
class Solution_TLE:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9+7
        nums = []
        cost = 0
        for num in instructions:
            i = bisect.bisect_left(nums, num)
            j = bisect.bisect_right(nums, num)
            n = len(nums)
            bisect.insort_left(nums, num)
        
            cost += min(i, n-j)
            cost %= MOD
        return cost

class SegmentTree:
    def __init__(self, nums, op=sum):
        self.n = len(nums)
        self.st = [0] * self.n + nums
        self.op = op
    
    def __getitem__(self, i):
        return self.st[i+self.n]
    
    def __setitem__(self, i, v):
        st, n, op = self.st, self.n, self.op
        i += n
        st[i] = v

        while i:
            st[i>>1] = op([st[i], st[i^1]])
            i >>= 1

    def query(self, l, r):
        st, n, op = self.st, self.n, self.op
        l, r = l+n, r+n

        res = 0
        while l <= r:
            if l== r:
                res = op([res, st[l]])
                break
            if l&1 == 1:
                res = op([res, st[l]])
                l += 1
            if r&1 == 0:
                res = op([res, st[r]])
                r -= 1
            l, r = l>>1, r>>1
        return res
            

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:        
        MOD = 10**9+7

        # find index of sorted distinct number
        # store each distinct number's index in num2idx hashmap
        nums = sorted(set(instructions))
        num2idx = defaultdict(int)
        for i, num in enumerate(nums):
            num2idx[num] = i
        
        n = len(instructions)
        seg = SegmentTree([0] * n)

        cost = 0
        for num in instructions:
            idx = num2idx[num]
            countLess = seg.query(0, idx-1)
            countGreater = seg.query(idx+1, n-1)

            cost += min(countLess, countGreater)
            cost %= MOD

            seg[idx] += 1

        return cost

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        # Segment Tree
        # use a segment tree to trace the count of each possible value in instructions
        # Time: O(nlogm)
        # Space: O(m)
        
        m = max(instructions)
        tree = [0] * (2 * m)
        
        def update(n):
			# convert the number to tree index
            i = m + n - 1

            while i > 0:
                tree[i] += 1
                i >>= 1
        
        def query(n):
			# query the total count of the numbers in range [1, n], or [1, n + 1)
			# convert left and right boundary to tree index by + m - 1
            left = m
            right = n + m
			
            res = 0
            
            # note that the interval is [left, right)
            while left < right:
                if left & 1:
                    res += tree[left]
                    left += 1
                if right & 1:
                    right -= 1
                    res += tree[right]
                
                left >>= 1
                right >>= 1
                
            return res
        
        cost = 0
        for i, v in enumerate(instructions):
            cost += min(query(v-1), i - query(v))
            update(v)
            
        return cost % (10 ** 9 + 7)

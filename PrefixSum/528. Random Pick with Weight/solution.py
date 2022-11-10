"""Intuition:

in the beginning, I tried brute force but got TLE.
then I thought maybe I didn't need to unpack all the index based on its weight, I can use prefix sum to represent one single index
the random value should be within [1, sum(w)] (both inclusive)
for a sorted array (our prefix sum), we can use binary search
"""
class BruteForceSolutionTLE:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.val = []
        for i, wei in enumerate(w):
            while wei > 0:
                self.val.append(i)
                wei -= 1

    def pickIndex(self) -> int:
        j = randint(0, len(self.val)-1)
        return self.val[j]

# Prefix Sum + Binary Search
class Solution:
	# O(n)
    def __init__(self, w: List[int]):
        self.val = [0] * (len(w)+1)
        for i in range(1, len(w)+1):
            self.val[i] = self.val[i-1]+w[i-1]
        # [1,2,1]
        # [0,1,3,4]
        # 01234
	# O(logn)
    def pickIndex(self) -> int:
        target = randint(1, self.val[-1])
        # return bisect.bisect_left(self.val, target)-1

        l, r = 0, len(self.val)
        while l < r:
            mid = l + (r-l)//2
            if self.val[mid] < target:
                l = mid+1
            else:
                r = mid
        return l-1
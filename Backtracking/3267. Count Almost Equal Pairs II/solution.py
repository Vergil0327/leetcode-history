# TLE
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        n = len(nums)

        return sum(int(self.almostEqual(nums[i], nums[j])) for i in range(n) for j in range(i+1, n))

    def almostEqual(self, a, b):
        arr1, arr2 = [], []
        while a > 0 or b > 0:
            if (a%10 != b%10):
                arr1.append(a%10)
                arr2.append(b%10)
            a //= 10
            b //= 10

            if len(arr1) >= 4: break

        if len(arr1) <= 1: return len(arr1) == 0
        if len(arr1) == 2 or len(arr1) == 3:
            arr1.sort()
            arr2.sort()
            return a == b and arr1 == arr2 # remaining part equals and swap digits equal

        for i in range(3):
            for j in range(i+1, 4):
                if arr1[i] == arr2[j] and arr1[j] == arr2[i]:
                    arr1.sort()
                    arr2.sort()
                    return a == b and arr1 == arr2
        return False

from itertools import combinations_with_replacement
from collections import Counter

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        # backtracking
        def findAlmost(x):
            s = list(str(x))
            n = len(s)
            res = set()
            for i, j in combinations_with_replacement(range(n), 2):
                s[i], s[j] = s[j], s[i] # swap
                for k, l in combinations_with_replacement(range(n), 2):
                    s[k], s[l] = s[l], s[k] # swap
                    res.add(int("".join(s)))
                    s[k], s[l] = s[l], s[k]
                s[i], s[j] = s[j], s[i]
            return res

        nums.sort(reverse=True)
        res = 0
        count = Counter()
        for num in nums:
            res += count[num]
            for x in findAlmost(num):
                count[x] += 1
        return res
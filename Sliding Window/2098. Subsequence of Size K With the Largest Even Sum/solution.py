from typing import List

class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        odds = []
        evens = []
        for num in nums:
            if num%2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        
        evens.sort(key=lambda x: -x)
        odds.sort(key=lambda x:-x)

        i = j = 0
        n, m = len(evens), len(odds)

        presumOdd = [0] * (m+1)
        for i in range(1, m+1):
            presumOdd[i] = presumOdd[i-1] + odds[i-1]

        res = -1
        presumEven = 0
        for i in range(min(k, n)):
            presumEven += evens[i]
            j = k-(i+1)
            
            # 需要有j個odd value並且sum為even
            if j <= m and j%2 == 0:
                res = max(res, presumEven + presumOdd[j])
        return res

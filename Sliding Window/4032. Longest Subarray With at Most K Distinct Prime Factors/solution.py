from collections import Counter
from math import isqrt
class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prime = Counter()
        l = r = res = 0
        while r < n:
            num = nums[r]
            r += 1

            for i in range(2, isqrt(num)+1):
                if num%i == 0:
                    while num%i == 0:
                        prime[i] += 1
                        num //= i
            if num > 1:
                prime[num] += 1

            while l < r and len(prime) > k:
                num = nums[l]
                for i in range(2, isqrt(num)+1):
                    if num%i == 0:
                        while num%i == 0:
                            prime[i] -= 1
                            num //= i
                        if prime[i] == 0:
                            del prime[i]
                if num > 1:
                    prime[num] -= 1
                    if prime[num] == 0:
                        del prime[num]
                l += 1

            res = max(res, r-l)
        return res
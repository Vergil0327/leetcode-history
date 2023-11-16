from typing import List
from math import gcd, sqrt
import bisect
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)

        Kfactors = set()
        for i in range(1, int(sqrt(k))+1):
            if k%i != 0: continue
            Kfactors.add(i)
            Kfactors.add(k//i)
        
        # groups: {common divisor with k: indices}
        groups = defaultdict(list)
        for i in range(n):
            for f in Kfactors:
                if nums[i]%f == 0:
                    groups[f].append(i)

        res = 0
        for i in range(n):
            GCD = gcd(nums[i], k)
            numj = k//GCD

            # 所有小於i的index都可以跟nums[i]配對
            res += bisect.bisect_left(groups[numj], i)      
            
        return res

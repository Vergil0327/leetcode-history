class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        
        res = 0
        for k in range(1, n + 1):
            if n % k != 0: continue
            
            is_valid = True
            for i in range(0, n, k):
                sub = nums[i : i + k]
                t_sub = target[i : i + k]
                
                # 1. Check if the elements are the same
                if sorted(sub) != t_sub:
                    is_valid = False
                    break
                
                # 2. Check if sub is a cyclic shift of t_sub
                # A cyclic shift of a sorted array has at most one "pivot" 
                # where the next element is smaller than the current.
                inflections = 0
                for j in range(k):
                    if sub[j] > sub[(j + 1) % k]:
                        inflections += 1
                
                # A sorted array rotated can have at most 1 inflection point.
                # Special case: if all elements are same, inflections = 0.
                if inflections > 1:
                    is_valid = False
                    break
            
            if is_valid:
                res += k
                
        return res
from itertools import accumulate


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        tmp = [0] * len(nums)
        # 1. presum = [0] + list(accumulate(nums)) => TLE
        # 2. 
        # presum = [0]
        # for n in nums:
        #     presum.append(presum[-1]+n)
        presum = [0] * (len(nums)+1)
        for i in range(len(nums)):
            presum[i+1] = presum[i] + nums[i]

        count = 0
        
        # [l, r] both inclusive
        def merge(l, mid, r):
            nonlocal count
            
            # [-2, 5,-1]
            # [0],[-2]  [3],[2]
            # [-2, 0]   [2,3]
            # lower <= presum[j] - presum[i-1] <= upper
            # presum[j] >= presum[i-1] + lower -> count of larger number after self
            # persum[j] <= presum[i-1] + upper -> count of smaller number after self
            # padding 0 at 0-th position
            # =>
            # presum[j] >= presum[i] + lower -> count of larger number after self
            # persum[j] <= presum[i] + upper -> count of smaller number after self
            # presum[i] + lower <= persum[j] <= presum[i] + upper, where i <= j
            start, end = mid+1, mid+1
            for i in range(l, mid+1):
                while start < r+1 and presum[start] < presum[i] + lower:
                    start += 1
                while end < r+1 and presum[end] <= presum[i] + upper:
                    end += 1
                count += end-start
                # TLE
                # start = bisect.bisect_left(presum[mid+1:r+1], presum[i] + lower)
                # end = bisect.bisect_right(presum[mid+1:r+1], presum[i] + upper)
                # count += end-start # (end-start) == numbers of valid presum[j]
                        
            tmp[l:r+1] = presum[l:r+1][:]
            i, j = l, mid+1
            for k in range(l, r+1):
                if i == mid+1:
                    presum[k] = tmp[j]
                    j += 1
                elif j == r+1:
                    presum[k] = tmp[i]
                    i += 1
                elif tmp[i] > tmp[j]:
                    presum[k] = tmp[j]
                    j += 1
                else:
                    presum[k] = tmp[i]
                    i += 1    
            # presum[l:r+1] = sorted(presum[l:r+1])
        
        def mergesort(l, r):
            nonlocal count

            if l == r: return
            
            mid = l + (r-l)//2
            mergesort(l, mid)
            mergesort(mid+1, r)
            merge(l, mid, r)
        
        mergesort(0, len(presum)-1)
        return count
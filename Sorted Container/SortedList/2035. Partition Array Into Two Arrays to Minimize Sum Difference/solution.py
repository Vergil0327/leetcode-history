from sortedcontainers import SortedList

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        def find_subset(arr):
            n = len(arr)
            subset = defaultdict(SortedList)
            max_state = 1<<n
            for state in range(1, max_state):
                tot = size = 0
                for i in range(n):
                    if (state>>i)&1:
                        size += 1
                        tot += arr[i]
                subset[size].add(tot)
            return subset

        n = len(nums)//2
        arr1, arr2 = nums[:n], nums[n:]
        subset1 = find_subset(arr1)
        subset2 = find_subset(arr2)
        
        res = abs(sum(arr1)-sum(arr2))
        SUM = sum(nums)
        target = SUM/2

        for k in range(1, n):
            for s1 in subset1[k]:
                r = subset2[n-k].bisect_right(target-s1)
                l = r-1
                for i in [l, r]:
                    # half1 = s1+s2
                    # half2 = SUM-half1
                    # diff = abs(half2-half1) = SUM - 2*half1
                    if 0 <= i < len(subset2[n-k]):
                        s2 = subset2[n-k][i]
                        res = min(res, abs(SUM-(s1+s2)*2))
                
                if res == 0: return res
        return res
    

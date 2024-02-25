class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n, m = len(nums), len(changeIndices)

        def check(sec):
            mark = [0] * (n+1)
            need = 0
            for i in range(sec-1, -1, -1):
                idx = changeIndices[i]-1
                if not mark[idx]:
                    mark[idx] = 1
                    need += nums[idx]
                else:
                    if need > 0:
                        need -= 1
            return sum(mark) == n and need == 0

        l, r = 0, m
        while l < r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid
            else:
                l = mid+1
        
        if not check(l): return -1
        return l

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)

        def checkAtMost(numMedian):
            l = r = res = 0
            count = Counter()
            while r < n:
                count[nums[r]] += 1
                r += 1

                while l < r and len(count) > numMedian:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                res += r-l
            return res

        l, r = 1, n
        N = n*(n+1)//2
        while l < r:
            mid = l + (r-l)//2
            if checkAtMost(mid) >= (N+1)//2:
                r = mid
            else:
                l = mid+1
        return l

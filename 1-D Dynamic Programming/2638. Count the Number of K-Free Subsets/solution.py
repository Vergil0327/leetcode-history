class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        arr = [[] for _ in range(k)]
        for num in nums:
            arr[num%k].append(num)

        # house robber
        def count(values):
            values.sort()

            # the number of ways to get k-free subsets when take/skp current values[i] considering values[:i]
            take, skip = 0, 1 # for empty subsets, there is 0 way to take and there is 1 way for us to skip
            
            n = len(values)
            for i in range(n):
                prevTake, prevSkip = take, skip
                if i >= 1 and nums[i] == nums[i-1]+k:
                    take = prevSkip
                    skip = prevTake + prevSkip
                else:
                    take = prevTake + prevSkip
                    skip = prevTake + prevSkip
            return take+skip

        res = 1
        for i in range(k):
            res *= count(arr[i])
        return res
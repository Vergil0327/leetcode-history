class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        x, y = nums[:len(nums)//2], nums[len(nums)//2:]
        
        def get_subset(arr):
            n = len(arr)
            # SET = set()
            # for state in range(1<<n):
            #     SET.add(sum(arr[i] for i in range(n) if (state>>i)&1))
            SET = set([0])
            for num in arr:
                SET |= {num + x for x in SET}
            return SET
        subset1 = get_subset(x)
        subset2 = sorted(list(get_subset(y)))

        res = abs(sum(nums)-goal)
        for sum1 in subset1:
            target = goal-sum1
            j = bisect_right(subset2, target)
            l, r = j-1, j
            if l >= 0:
                res = min(res, abs(sum1+subset2[l]-goal))
            if r < len(subset2):
                res = min(res, abs(sum1+subset2[r]-goal))
        return res

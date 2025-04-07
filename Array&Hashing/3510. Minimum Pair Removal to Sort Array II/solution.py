from sortedcontainers import SortedList
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        inverse = sum(int(nums[i] > nums[i+1]) for i in range(n-1))
        sl = SortedList([nums[i] + nums[i + 1], i] for i in range(n-1))

        L = list(range(-1, n-1))
        R = list(range(1, n+1))

        def add(i):
            nonlocal inverse

            j = R[i]
            if 0 <= i < j < n:
                sl.add([nums[i]+nums[j], i])
                inverse += int(nums[i] > nums[j])

        def remove(i):
            nonlocal inverse

            j = R[i]
            if 0 <= i < j < n:
                sl.discard([nums[i]+nums[j], i])
                inverse -= int(nums[i] > nums[j])

        res = 0
        while inverse > 0:
            res += 1

            # [..., l, i, j, r, ...]
            # find index of minimum pair sum
            _, i = sl.pop(0)
            j = R[i]
            l, r = L[i], R[j]

            # remove linked list nodes first
            remove(l)
            remove(i)
            remove(j)

            # merge (i,j), update `L`, `R`, `nums[i]`
            nums[i] += nums[j]
            R[i] = r
            if r < n:
                L[r] = i

            # add new merged node back to linked list
            add(l)
            add(i)
        return res
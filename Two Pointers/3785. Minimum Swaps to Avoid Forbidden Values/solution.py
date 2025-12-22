class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)

        count = Counter()
        for num in nums:
            count[num] += 1
        for num in forbidden:
            count[num] += 1

        # no enough position for current num
        if any(freq > n for freq in count.values()): return -1

        needSwap = Counter()
        for i in range(n):
            if nums[i] == forbidden[i]:
                needSwap[nums[i]] += 1

        swaps = list(needSwap.values())
        swaps.sort()

        res = 0
        l, r = 0, len(swaps)-1
        while l <= r:
            swap = min(swaps[l], swaps[r])
            res += swap
            swaps[l] -= swap
            swaps[r] -= swap
            if swaps[l] == 0 and swaps[r] == 0:
                l, r = l+1, r-1
            elif swaps[l] == 0:
                l += 1
            else:
                r-= 1
        return res
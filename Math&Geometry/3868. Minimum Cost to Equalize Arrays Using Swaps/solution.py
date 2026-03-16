class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        nums = set(count1.keys()) | set(count2.keys())
        diff = 0
        for num in nums:
            if (count1[num] + count2[num])%2: return -1
            diff += abs(count1[num] - count2[num])

        return diff // 4
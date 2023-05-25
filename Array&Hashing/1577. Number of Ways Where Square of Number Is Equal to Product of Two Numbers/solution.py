class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for num in nums1:
            curr = num*num
            counter = defaultdict(int)
            for val in nums2:
                if curr%val == 0:
                    res += counter[curr//val]
                counter[val] += 1

        for num in nums2:
            curr = num*num
            counter = defaultdict(int)
            for val in nums1:
                if curr%val == 0:
                    res += counter[curr//val]
                counter[val] += 1

        return res

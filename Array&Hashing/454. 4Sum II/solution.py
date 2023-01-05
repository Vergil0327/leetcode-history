class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        
        sum12 = defaultdict(int)
        for i in range(n):
            for j in range(n):
                curr = nums1[i] + nums2[j]
                sum12[curr] += 1

        cnt = 0
        for j in range(n):
            for k in range(n):
                curr = nums3[j] + nums4[k]
                cnt += sum12[-curr]
        return cnt

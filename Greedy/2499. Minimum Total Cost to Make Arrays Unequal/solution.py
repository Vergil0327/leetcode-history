class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:        
        n = len(nums1)
        
        toSwap = set()
        freq = defaultdict(int)
        maxFreq = 0
        maxFreqVal = -1
        for i in range(n):
            if nums1[i] == nums2[i]:
                toSwap.add(i)
                freq[nums1[i]] += 1
                if freq[nums1[i]] > maxFreq:
                    maxFreq = freq[nums1[i]]
                    maxFreqVal = nums1[i]
                
        if not toSwap: return 0
        res = sum(toSwap)

        for i in range(n):
            if 2*maxFreq > len(toSwap): # we need to find another index to swap
                if nums1[i] != nums2[i] and nums1[i] != maxFreqVal and nums2[i] != maxFreqVal:
                    res += i

                    # update swap times, if we find proper num1[i] to swap
                    # we need to make sure # we swap is greater than 2*maxFreq
                    toSwap.add(i)

        if 2*maxFreq > len(toSwap): return -1 # greater than half, we can't distribute value with maxFreq to right position
        return res

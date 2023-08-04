class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        n = len(nums1)
        counter = defaultdict(int)
        mxHeap = [] # store [-diff=nums1[i]-nums2[i], count]
        k = k1+k2
        for i in range(n):
            counter[abs(nums1[i]-nums2[i])] += 1
            
        for diff, cnt in counter.items():
            heapq.heappush(mxHeap, [-diff, cnt])

        while k:
            diff, cnt = mxHeap[0][0], mxHeap[0][1]
            if diff == 0: break
            
            # merge same diff pair with current
            heapq.heappop(mxHeap)
            while mxHeap and mxHeap[0][0] == diff:
                _, cnt2 = heapq.heappop(mxHeap)
                cnt += cnt2

            if k >= cnt:
                heapq.heappush(mxHeap, [diff+1, cnt])
                k -= cnt
            else:
                heapq.heappush(mxHeap, [diff, cnt-k])
                heapq.heappush(mxHeap, [diff+1, k])
                k = 0

        return sum(pow(diff, 2)*cnt for diff, cnt in mxHeap)

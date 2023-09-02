class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        counter = Counter(s)
        maxHeap = []
        for ch, cnt in counter.items():
            heapq.heappush(maxHeap, [-cnt, ch])
            
        topKGroups = [[0, 0] for _ in range(k)]
        i = 0
        while maxHeap and i < k:
            curMax = maxHeap[0][0]
            topKGroups[i][0] = -maxHeap[0][0]
            while maxHeap and maxHeap[0][0] == curMax:
                topKGroups[i][1] += 1
                heapq.heappop(maxHeap)
            i += 1
            
        @cache
        def C(n,m):
            if m == n:
                return 1
            elif m == 1:
                return n
            else:
                return C(n-1, m-1) + C(n-1, m)
        
        mod = 10**9 + 7

        res = 1
        for i in range(k):
            if not topKGroups[i]: break
            if topKGroups[i][1] <= k:
                k -= topKGroups[i][1]
                res *= pow(topKGroups[i][0], topKGroups[i][1], mod)
                res %= mod
            else:
                res *= C(topKGroups[i][1], k) * pow(topKGroups[i][0], k, mod)
                res %= mod
                k = 0
            if k == 0:
                return res
        return 0

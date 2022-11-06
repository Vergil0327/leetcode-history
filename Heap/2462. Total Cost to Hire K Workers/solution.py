# [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        minheap = []
        for i, cost in enumerate(costs):
            if i < candidates or i >= len(costs)-candidates:
                heapq.heappush(minheap, [cost, i])
        
        # keep tracking if any left worker still not push into the min heap
        l, r = candidates-1, len(costs)-candidates

        res = 0
        while k > 0:
            cost, idx = heapq.heappop(minheap)
            if l+1 < r and idx <= l:
                l+=1
                heapq.heappush(minheap, [costs[l], l])
            if l < r-1 and idx >= r:
                r-=1
                heapq.heappush(minheap, [costs[r], r])

            res += cost
            k -= 1
            
        return res
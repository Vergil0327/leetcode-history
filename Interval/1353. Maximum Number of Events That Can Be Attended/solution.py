class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x:(x[0], x[1]))
        lastDay = -1
        for _, end in events:
            lastDay = max(lastDay, end)

        n = len(events)
        availableEvt = [] # min heap
        res = j = 0
        for day in range(1, lastDay+1):
            while j < n and events[j][0] == day:
                heapq.heappush(availableEvt, [events[j][1], events[j][0]])
                j += 1

            while availableEvt and availableEvt[0][0] < day:
                heapq.heappop(availableEvt)
            
            if availableEvt:
                res += 1
                end, start = heapq.heappop(availableEvt)
        return res

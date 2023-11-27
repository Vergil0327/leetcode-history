from sortedcontainers import SortedList
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = [] # min heap, [time, server_id]
        idle = SortedList(range(k))

        res = [0]*k
        for i, t in enumerate(arrival):
            while busy and busy[0][0] <= t:
                _, svr = heapq.heappop(busy)
                idle.add(svr)

            idx = idle.bisect_left(i%k)
            if not idle: continue
            if idx == len(idle):
                idx = 0
            
            assignSvr = idle.pop(idx)
            res[assignSvr] += 1
            heapq.heappush(busy, [t+load[i], assignSvr])
        
        mx = max(res)
        return [svr for svr, cnt in enumerate(res) if cnt == mx]

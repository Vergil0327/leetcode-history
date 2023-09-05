from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n, k = len(rooms), len(queries)
        
        q = sorted([[queries[i][1], queries[i][0], i] for i in range(k)], reverse=True)
        rooms.sort(key=lambda x:x[1], reverse=True)
        res = [-1] * k
        candidates = SortedList()
        i = 0
        for minSize, preferred, idx in q:
            while i < n and rooms[i][1] >= minSize:
                candidates.add(rooms[i][0])
                i += 1

            r = candidates.bisect_right(preferred) # 最靠近preferred右側的roomId
            l = r-1 # 最靠近preferred左側的roomId

            diffR = diffL = inf
            if r < len(candidates):
                diffR = abs(candidates[r]-preferred)

            if l >= 0:
                diffL = abs(candidates[l]-preferred)

            if diffL > diffR:
                res[idx] = candidates[r]
            elif diffL < diffR:
                res[idx] = candidates[l]
            elif diffL != inf: # if there is a tie, choose smallest id
                res[idx] = candidates[l]
        return res

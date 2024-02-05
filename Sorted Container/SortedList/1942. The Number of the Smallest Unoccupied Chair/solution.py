from sortedcontainers import SortedList
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        
        available = SortedList([i for i in range(n)])
        occupied = SortedList()
        target = times[targetFriend][0]
        times.sort()
        for arrival, leave in times:
            while occupied and occupied[0][0] <= arrival:
                available.add(occupied.pop(0)[1])

            chair_id = available.pop(0)
            if arrival == target: return chair_id
            occupied.add((leave, chair_id))
        return -1

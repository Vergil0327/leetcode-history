class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted([[capital[i], profits[i]] for i in range(len(profits))])

        currCapital = w
        maxHeap = []
        i = 0
        while k > 0:
            while i < len(projects) and projects[i][0] <= currCapital:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            if not maxHeap: break
            
            p = heapq.heappop(maxHeap)
            currCapital += -p
            k -= 1
            
        return currCapital

class Solution_Slow:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        maxHeap = [[-profits[i], capital[i]] for i in range(n)]
        heapq.heapify(maxHeap)

        queue = []
        earned = w
        while k > 0 and maxHeap:
            p, cap = heapq.heappop(maxHeap)
            if cap > earned:
                queue.append([p, cap])
                continue
            
            earned += -p
            k -= 1
            while k > 0 and queue:
                heapq.heappush(maxHeap, queue.pop())
        return earned
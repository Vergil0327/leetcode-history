class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        queue = deque(sorted([[task[0], task[1], i] for i, task in enumerate(tasks)]))

        pq = []
        currTime = queue[0][0]
        order = []
        while pq or queue:
            while (queue and queue[0][0] <= currTime) or not pq:
                enq, pt, i = queue.popleft()
                heapq.heappush(pq, [pt, i, enq])
            
            pt, i, enq = heapq.heappop(pq)
            order.append(i)
            currTime = max(currTime+pt, enq+pt)
        return order

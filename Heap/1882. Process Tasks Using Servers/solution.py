class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        idleServers = [[servers[i], i] for i in range(len(servers))] # [servers[i], i]
        heapq.heapify(idleServers)
    
        taskQueue = deque()
        processed = [] # [finished_t, [servers[i], i]]
        n = len(tasks)
        res = [-1] * n
        for j in range(n):
            taskQueue.append(j)
            while processed and processed[0][0] <= j:
                finished_t, server = heapq.heappop(processed)
                heapq.heappush(idleServers, server)

            while taskQueue and idleServers:
                task = taskQueue.popleft()
                server = heapq.heappop(idleServers)
                res[task] = server[1]

                heapq.heappush(processed, [j+tasks[task], server])
            
        # 這時全部server應為忙碌中
        while taskQueue:
            task = taskQueue.popleft()
            finished_t, server = heapq.heappop(processed)
            res[task] = server[1]
            heapq.heappush(processed, [finished_t + tasks[task], server])
        return res

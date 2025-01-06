class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.users = defaultdict(lambda: defaultdict(int))
        self.task2user = {}
        self.tasks = []
        
        for userId, taskId, priority in tasks:
            heapq.heappush(self.tasks, [-priority, -taskId])
            self.task2user[taskId] = userId
            self.users[userId][taskId] = priority

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.users[userId][taskId] = priority
        self.task2user[taskId] = userId
        heapq.heappush(self.tasks, [-priority, -taskId])

    def edit(self, taskId: int, newPriority: int) -> None:
        userId = self.task2user[taskId]
        self.users[userId][taskId] = newPriority
        heapq.heappush(self.tasks, [-newPriority, -taskId])

    def rmv(self, taskId: int) -> None:
        userId = self.task2user[taskId]
        del self.users[userId][taskId]
        del self.task2user[taskId]

    def execTop(self) -> int:
        while self.tasks:
            priority, taskId = -self.tasks[0][0], -self.tasks[0][1]
            if taskId not in self.task2user:
                heapq.heappop(self.tasks)
                continue
            userId = self.task2user[taskId]
            if userId not in self.users:
                heapq.heappop(self.tasks)
                continue
            
            if priority != self.users[userId][taskId]:
                heapq.heappop(self.tasks)
                continue
            
            break
        if not self.tasks: return -1

        taskId = -self.tasks[0][1]
        heapq.heappop(self.tasks)
        userId = self.task2user[taskId]
        
        del self.task2user[taskId]
        del self.users[userId][taskId]

        return userId

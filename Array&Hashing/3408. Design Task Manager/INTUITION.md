# Intuition

首先先試著用hashmap記錄我們要的訊息, 並且由於execTop要看的是highest priority, 其次是highest taskId, 所以我們可以用priority queue儲存這類訊息(-priority, -taskId)

那麼`add`, `edit`, `rmv`其實就很直覺, 就維護hashmap跟priority queue即可

至於最後的`execTop`, 只要透過priority queue跟hashmap相比較, 汰除掉不合法的task之後
剩下的首位極為所求


```py
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

```
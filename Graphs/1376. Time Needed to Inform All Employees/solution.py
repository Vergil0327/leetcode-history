from collections import defaultdict, deque

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nxt = defaultdict(list)
        for node, head in enumerate(manager):
            nxt[head].append(node)

        time = 0
        queue = deque([(headID, informTime[headID])])
        while queue:
            cur, t = queue.popleft()
            time = max(time, t)

            for node in nxt[cur]:
                queue.append([node, t+informTime[node]])

        return time
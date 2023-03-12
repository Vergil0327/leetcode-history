class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        n = len(tasks)
        tasks.sort(key=lambda x:x[1])

        timeline = [0] * 2002
        for start, end, dur in tasks:
            for i in range(end, start-1, -1):
                if timeline[i] > 0:
                    dur -= 1
                if dur == 0: break

            if dur > 0:
                for i in range(end, start-1, -1):
                    if timeline[i] == 0:
                        timeline[i] = 1
                        dur -= 1
                    if dur == 0: break
        return sum(timeline)
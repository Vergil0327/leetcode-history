class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        days = [0]*(len(tasks)+5) # day for task i to complete
        prevTaskIdx = {}
        for i, tsk in enumerate(tasks, start=1):
            days[i] += days[i-1]
            if tsk in prevTaskIdx:
                prev = prevTaskIdx[tsk]
                breaks = max(0, space - (days[i] - days[prev]))
                days[i] += breaks

            days[i] += 1
            prevTaskIdx[tsk] = i

        return days[len(tasks)]
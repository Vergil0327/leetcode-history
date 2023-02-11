from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()

        def canComplete(numTask, pills):
            if numTask > len(workers): return False
            sl = SortedList(workers)

            for i in range(numTask-1, -1, -1):
                if sl[-1] >= tasks[i]:
                    sl.pop()
                elif pills > 0:
                    pills -= 1
                    i = sl.bisect_left(tasks[i]-strength)
                    if i == len(sl): return False
                    sl.pop(i)
                else:
                    return False
            return True

        l, r = 0, len(tasks)
        while l < r:
            mid = r - (r-l)//2
            if canComplete(mid, pills):
                l = mid
            else:
                r = mid-1
        return l


# tasks可以優先選小的來盡可能分配，看最多能選幾件tasks
# 但要分配給哪個worker或是worker+pill並沒有優劣
# example
# tasks = [5,9,8,5,9]
# workers = [1,6,4,2,6], pills = 1, strength = 5
# ans = 3

# 所以至少可以先對tasks排序，然後來看我們最多可以選幾件


# 一開始的想法，排序後盡可能去分配
# 但是，是錯的
# example:
# tasks = [5,9,8,5,9]
# workers = [1,6,4,2,6], pills = 1, strength = 5
# ans = 3

# class Solution:
#     def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
#         tasks.sort()
#         workers.sort()

#         taskIdx = 0
#         complete = 0
#         for workerStr in workers:
#             if workerStr >= tasks[taskIdx]:
#                 complete += 1
#                 taskIdx += 1
#             elif pills > 0 and workerStr+strength >= tasks[taskIdx]:
#                 complete += 1
#                 pills -= 1
#                 taskIdx += 1
#             if taskIdx == len(tasks): break
#         return complete

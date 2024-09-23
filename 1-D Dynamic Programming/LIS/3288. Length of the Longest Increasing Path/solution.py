class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        x, y = coordinates[k]

        coordinates.sort(key=lambda x:(x[0], -x[1]))
        before, after = [], []
        for xx, yy in coordinates:
            if xx < x and yy < y: # 前半段LIS
                i = bisect_left(before, yy)
                if i == len(before):
                    before.append(yy)
                else:
                    before[i] = min(before[i], yy)

            elif xx > x and yy > y: # 後半段LIS
                i = bisect_left(after, yy)
                if i == len(after):
                    after.append(yy)
                else:
                    after[i] = min(after[i], yy)
        return len(before) + 1 + len(after)
    

from sortedcontainers import SortedList
class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
        n = len(coordinates)
        x, y = coordinates[k]

        coordinates.sort(key=lambda x:(x[0], -x[1]))
        before, after = SortedList(), SortedList()
        for xx, yy in coordinates:
            if xx < x and yy < y: # 前半段LIS
                i = before.bisect_left(yy)
                if i == len(before):
                    before.add(yy)
                else:
                    num = before.pop(i)
                    before.add(min(num, yy))
            elif xx > x and yy > y: # 後半段LIS
                i = after.bisect_left(yy)
                if i == len(after):
                    after.add(yy)
                else:
                    num = after.pop(i)
                    after.add(min(num, yy))

        return len(before) + 1 + len(after)
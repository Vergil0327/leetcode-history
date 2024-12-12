from sortedcontainers import SortedList

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)

        sl = SortedList()
        for i in range(n-1, -1, -1):
            j = sl.bisect_left([arr[i], -inf])-1
            if j >= 0:
                targetIdx = -sl[j][1]
                arr[i], arr[targetIdx] = arr[targetIdx], arr[i]
                return arr

            sl.add([arr[i], -i])
        return arr
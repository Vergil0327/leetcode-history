from sortedcontainers import SortedDict
class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        m = len(queries)
        
        # sort in decreasing order of x
        nums = sorted(zip(nums1, nums2), reverse=True)
        query = sorted([(x, y, i) for i, (x,y) in enumerate(queries)], reverse=True)

        res = [0] * m
        j = 0
        sd = SortedDict()
        for x, y, idx in query:

            # put all the nums[j] where nums[j][0] >= x into a group. here we use SortedDict
            while j < n and nums[j][0] >= x:
                num1, num2 = nums[j]

                # update monotonic hashmap: {num2: num1 + num2}
                self.updateMap(sd, num2, num1 + num2)
                j += 1

            # find all the maximum value where num2 >= y
            # since sd is a monotonic decreasing hashmap, first key-value pair which key >= y is maximum value
            k = sd.bisect_left(y)
            res[idx] = sd.peekitem(k)[1] if k != len(sd) else -1
        return res

    def updateMap(self, sMap, key, value):
        i = sMap.bisect_left(key)
        if i != len(sMap) and sMap.peekitem(i)[1] >= value:
            return

        # maintain a monotonic decreasing hashmap where map[k] = v1 and map[k+1] = v2 where v1 > v2
        if i > 0:
            i -= 1
            while i >= 0 and sMap.peekitem(i)[1] <= value:
                sMap.popitem(i)
                i -= 1
        sMap[key] = value

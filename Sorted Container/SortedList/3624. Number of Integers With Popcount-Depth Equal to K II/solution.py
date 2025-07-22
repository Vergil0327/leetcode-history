from math import log2, ceil
from collections import defaultdict
from sortedcontainers import SortedList
class Solution:    
    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        m = ceil(log2(10**15))+1
        depth = [0] * m
        for i in range(2, m):
            depth[i] = depth[i.bit_count()]+1

        position = defaultdict(SortedList)# position[depth] = [index1, index2, ...]
        for i, num in enumerate(nums):
            if num == 1:
                position[-1].add(i)
            else:
                position[depth[num.bit_count()]].add(i)
        
        res = []
        for query in queries:

            if query[0] == 1:
                l, r, k = query[1], query[2], query[3]

                i = position[k-1].bisect_left(l)
                j = position[k-1].bisect_right(r)
                res.append(j-i)
            else:
                idx, val = query[1], query[2]

                if nums[idx] == 1:
                    position[-1].remove(idx)
                else:
                    position[depth[nums[idx].bit_count()]].remove(idx)
                nums[idx] = val

                if nums[idx] == 1:
                    position[-1].add(idx)
                else:
                    position[depth[nums[idx].bit_count()]].add(idx)
        return res
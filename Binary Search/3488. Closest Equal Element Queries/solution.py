class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        indice = defaultdict(list)
        for i, num in enumerate(nums):
            indice[num].append(i)


        res = []
        for i in queries:
            if (m := len(indice[nums[i]])) > 1:
                r = bisect_right(indice[nums[i]], i)%m # right closest, take modular to find circular item if not exist
                l = (bisect_left(indice[nums[i]], i)-1+m)%m # left closest, take modular to find circular item if not exist
                idxR = indice[nums[i]][r]
                idxL = indice[nums[i]][l]
                dist1 = abs(i-idxR) # n-dist1 = ther other circular distance
                dist2 = abs(i-idxL) # n-dist2 = ther other circular distance
                res.append(min(min(dist1, n-dist1), min(dist2, n-dist2)))
            else:
                res.append(-1)
        return res
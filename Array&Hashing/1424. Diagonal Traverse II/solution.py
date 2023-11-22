class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        diagonals = defaultdict(list)
        for i in range(m):
            for j, num in enumerate(nums[i]):
                key = i+j
                diagonals[key].append([i, j])

        res = []
        for key in sorted(diagonals.keys()):
            for i, j in sorted(diagonals[key], key=lambda x:(-x[0], x[1])):
                res.append(nums[i][j])
        return res
        

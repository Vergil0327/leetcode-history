# Intuition

diagonal: i+j is the same, [[0,0]], [[0,1],[1,0]], [[0,2],[1,1],[2,0]]
take i+j as key and iteration

see example2, be careful of incompleted row

brute force - TLE
```py
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        n = len(nums[0])
        for i in range(m):
            n = max(n, len(nums[i]))

        res = []
        for key in range(m+n):
            for i in range(min(m-1, key), -1, -1):
                cols = len(nums[i])
                j = key-i
                
                if j < len(nums[i]):
                    res.append(nums[i][j])
  
        return res
```

since iteration like above may iterate m*n times, but there might be many incomplete rows.
thus, we can use i+j as key the sort each diagonal, then restore their order
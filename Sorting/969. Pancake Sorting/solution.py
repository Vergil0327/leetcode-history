# Straight-forward
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        v2i = {v:i for i, v in enumerate(arr)}
        res = []
        def rev(n):
            arr[:n] = reversed(arr[:n])
            for i in range(n):
                v2i[arr[i]] = i
            res.append(n)

        n = len(arr)
        for i in range(n-1, -1, -1):
            while arr[i] != i+1:
                if v2i[i+1] != 0:
                    rev(v2i[i+1]+1)
                else:
                    rev(i+1)
        
        return res

# Space-Optimized
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        def rev(n):
            arr[:n] = reversed(arr[:n])
            res.append(n)
        
        n = len(arr)

        for i in range(n-1, -1, -1):
            while arr[i] != i+1:
                j = arr.index(i+1)
                if j != 0:
                    rev(j+1)
                else:
                    rev(i+1)
        
        return res
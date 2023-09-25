class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        res = set()
        dp = set()
        for i in range(n):
            tmp = dp.copy()
            
            dp.clear()
            dp.add(arr[i])
            for prev in tmp:
                dp.add(prev | arr[i])
            
            res.update(dp)
        return len(res)

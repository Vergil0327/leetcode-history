class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        valids = []
        
        n = len(arr)
        total = l = r = 0
        while r < n:
            total += arr[r]
            r += 1

            while l < r and total > target:
                total -= arr[l]
                l += 1

            if total == target:
                valids.append([r-l, l, r-1])
                
        if len(valids) < 2: return -1

        m = len(valids)
        valids.sort(key=lambda x:x[1])
        
        suffixMin = [inf] * (m+1)
        for i in range(m-1, -1, -1):
            suffixMin[i] = min(suffixMin[i+1], valids[i][0])
        
        res = inf
        j = 0
        for i in range(m):
            while j < m and valids[j][1] <= valids[i][2]:
                j += 1

            if j != m:
                res = min(res, valids[i][0] + suffixMin[j])
            
        return res if res != inf else -1

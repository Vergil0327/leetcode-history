class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        flowers.sort(reverse=True)
        
        sufsum = list(reversed(list(accumulate(list(reversed(flowers)), initial=0))))

        res = 0
        j = 0
        for k in range(0, n+1):
            j = max(j, k)
            while j < n and (sufsum[j]+newFlowers) < flowers[j] * (n-j):
                j += 1
            
            max_incomplete = (sufsum[j]+newFlowers) // (n-j) if j<n else 0
            
            beauty = k*full
            if j < n and flowers[j] < target:
                beauty += min(max_incomplete, target-1) * partial

            res = max(res, beauty)

            if k < n and (diff := target-flowers[k]) > 0:
                newFlowers -= diff
            if newFlowers < 0: break
        return res
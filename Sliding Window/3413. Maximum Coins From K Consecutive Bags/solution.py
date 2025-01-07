class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        n = len(coins)

        def sliding(arr):
            arr.sort()
            res = collect = j = 0

            for i, (l, r, c) in enumerate(arr):
                # fully contain
                while j+1 < n and arr[j+1][0] < l+k:
                    ll, rr, cc = arr[j]
                    collect += (rr-ll+1) * cc
                    j += 1
        
                extra = 0
                if j < n and arr[j][0] < l+k:
                    end = min(l+k-1, arr[j][1])
                    extra += (end-arr[j][0]+1) * arr[j][2]
                
                res = max(res, collect+extra)
                collect -= (r-l+1) * c
            return res

        # sliding forwards
        res = sliding(coins)

        # sliding backwards
        coins = [[-r,-l,c] for l, r, c in coins]
        res = max(res, sliding(coins))
        return res

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = int(1e9+7)
        
        def count(threshold):
            cnt = 0
            for num in inventory:
                if num < threshold: continue
                cnt += num-threshold+1
            return cnt

        
        l, r = 1, int(1e9)
        while l < r:
            mid = l + (r-l)//2
            if count(mid) <= orders:
                r = mid
            else:
                l = mid+1
        
        targetPrice = l
        res = 0
        for ball in inventory:
            if ball < targetPrice: continue
            res = (res + (ball+targetPrice)*(ball-targetPrice+1)//2)%MOD
        
        remainOrder = orders - count(targetPrice)
        res += (targetPrice-1)*remainOrder
        
        return res%MOD
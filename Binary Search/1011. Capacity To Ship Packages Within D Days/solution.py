class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = 0, sum(weights)
        while l < r:
            mid = l + (r-l)//2
            if self.canShip(mid, weights, days):
                r = mid
            else:
                l = mid+1
        return l

    def canShip(self, cap, weights, days):
        day = 0
        carry = 0
        for w in weights:
            if w > cap: return False
            if carry+w>cap:
                day+=1
                carry = 0
            carry += w
        return day+1 <= days
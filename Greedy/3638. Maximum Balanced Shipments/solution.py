class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        mx = weight[0]
        i = 0
        res = 0
        while i < n:
            if weight[i] < mx:
                res += 1
                i = i+1
                if i < n:
                    mx = weight[i]
            else:
                mx = max(mx, weight[i]) 
                i += 1
        return res
    

    def maxBalancedShipments(self, weight: List[int]) -> int:
        res = maxi = 0
        for w in weight:
            maxi = max(maxi, w)
            if w < maxi:
                res += 1
                maxi = 0
        return res
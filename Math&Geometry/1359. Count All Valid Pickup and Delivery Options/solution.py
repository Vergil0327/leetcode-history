class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9+7
        res = 1
        totSlots = 2*n
        for i in range(totSlots, 0, -2):
            validChoices = i*(i-1)//2
            res = (res * validChoices)%mod
            
        return res

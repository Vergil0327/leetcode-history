class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0
        for m in range(1, ceil(n/2)+1):
            k = ((2*n/m) - m + 1)/2
            if k.is_integer() and k+m-1 <= n and k > 0:
                res += 1
            elif k <= 0 or k+m-1 > n:
                break
 
        return res

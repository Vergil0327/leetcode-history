# gray code: https://cp-algorithms.com/algebra/gray-code.html
class Solution:
    def grayCode(self, n):
        return n ^ (n >> 1)
    
    def circularPermutation(self, n, start):
        res = list(map(self.grayCode, range(pow(2, n))))
        
        i = res.index(start)
        return res[i:] + res[:i]

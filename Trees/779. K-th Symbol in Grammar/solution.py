
@cache
def rec(n, k):
    if n == 1:
        return 0
    
    if (rightChild := k%2 == 0):
        return rec(n-1, k//2)^1
    else:
        return rec(n-1, (k+1)//2)

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1: return 0
        return rec(n, k)

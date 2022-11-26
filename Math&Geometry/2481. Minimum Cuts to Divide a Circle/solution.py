# if n is even, we can cut half and half in n//2 times
# if n is odd, all we can do is cut n times to split equally

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n ==1: return 0
        if n % 2 == 0: return n//2
        return n

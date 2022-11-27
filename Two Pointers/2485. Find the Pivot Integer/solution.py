# O(n)
class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: return 1

        l, r = 1, n
        totalL, totalR = 0, 0
        while l < r:
            totalR += r
            r -= 1
            
            while l < r and totalR >= totalL:
                totalL += l
                l += 1
        
        if totalL + l == totalR + r:
            return l
        else:
            return -1

# Math Solution
# ref: https://leetcode.com/problems/find-the-pivot-integer/discuss/2851991/SQRT-or-Binary-Search-or-DP
# SQRT
# Why x * x == sum? For n, the sum of [1..n] is sum = n * (n + 1) / 2.

# The sum of [1..x] is x * (x + 1) / 2. The sum of [x..n] is n * (n + 1) / 2 - x * (x + 1) / 2 + x. So:

# x * (x + 1) / 2 == n * (n + 1) / 2 - x * (x + 1) / 2 + x,
# x * (x + 1) / 2 + x * (x + 1) / 2 - x == n * (n + 1) / 2,
# x * (x + 1) - x == sum,
# x * x == sum.

class Solution:
    def pivotInteger(self, n: int) -> int:
      total = n*(n+1)//2
      x = math.sqrt(total)
      if x*x == total:
        return x
      else:
        return -1
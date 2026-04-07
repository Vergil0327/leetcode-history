from math import ceil

class Solution:
        def findGoodIntegers(self, n: int) -> list[int]:

            cubes = [x * x * x for x in range(1, ceil(n**(1/3)))]
            first, ans = set(), set()

            for i, x3 in enumerate(cubes):
                for y3 in cubes[i:]:
                    x = x3 + y3
                    if x > n: break
                    
                    if x not in first:
                        first.add(x)
                    else:
                        ans.add(x)

            return sorted(ans)
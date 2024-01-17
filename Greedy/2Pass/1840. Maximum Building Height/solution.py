class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions = [[1,0]] + restrictions
        restrictions.sort()
        if restrictions[-1][0] < n:
            restrictions.append([n, n-1])

        m = len(restrictions)
        for i in range(m-1):
            a, ha = restrictions[i]
            b, hb = restrictions[i+1]
            
            h = ha + abs(b-a)

            # [a,b]之間夠遠
            if h > hb:
                diff = h-hb
                h = hb + diff//2
            
            restrictions[i+1][1] = min(h, hb)

        res = 0
        restrictions.reverse()
        for i in range(m-1):
            a, ha = restrictions[i]
            b, hb = restrictions[i+1]
            
            h = ha + abs(b-a)

            # [a,b]之間夠遠
            if h > hb:
                diff = h-hb
                h = hb + diff//2

            # find maximum valid height
            res = max(res, h)
            
            restrictions[i+1][1] = min(h, hb)

        return res

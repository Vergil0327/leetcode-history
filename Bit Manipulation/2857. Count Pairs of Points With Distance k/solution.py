class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        res = 0

        # (0, k) == (k, 0), only need to iterate from 0 to k//2
        for i in range(k//2+1):
            a, b = i, k-i
            seen = defaultdict(int)
            for x1, y1 in coordinates:
                # x1^x2 == a
                # y1^y2 == b
                x2 = a^x1
                y2 = b^y1
                res += seen[(x2, y2)] 
                
                # x1^x2 == b
                # y1^y2 == a
                x3 = b^x1
                y3 = a^y1

                # if only 1 possible target, don't calculate twice, see example 2
                if (x2,y2) != (x3,y3):
                    res += seen[(x3, y3)]
                
                seen[(x1,y1)] += 1
        return res
    
# or this
class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        count = Counter()
        res = 0
        for x1, y1 in coordinates:
            for x in range(k + 1):
                res += count[x1 ^ x, y1 ^ (k - x)]
            count[x1, y1] += 1
        return res
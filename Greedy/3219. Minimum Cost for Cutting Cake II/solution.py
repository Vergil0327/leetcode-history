class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        i = j = res = 0
        while i < len(horizontalCut) or j < len(verticalCut):
            costH = horizontalCut[i] if i < len(horizontalCut) else 0
            costV = verticalCut[j] if j < len(verticalCut) else 0
            
            if costH >= costV:
                res += costH * (j+1)
                i += 1
            else:
                res += costV * (i+1)
                j += 1

        return res
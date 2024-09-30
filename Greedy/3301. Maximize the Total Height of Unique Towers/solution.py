class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        
        res = 0
        validHeight = maximumHeight[0]+1
        for h in maximumHeight:
            if h <= validHeight:
                res += h
                validHeight = h-1
            else:
                if validHeight <= 0: return -1
                res += validHeight
                validHeight -= 1
        return res


# 重新整理一下為
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        
        res = 0
        validHeight = maximumHeight[0]+1
        for h in maximumHeight:
            validHeight = min(validHeight-1, h)
            if validHeight <= 0: return -1
            res += validHeight
            
        return res
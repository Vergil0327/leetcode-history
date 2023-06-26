class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        step = 0
        while target > startValue:
            if target%2 == 0:
                target //= 2
                step += 1
            else:
                target = (target+1)//2
                step += 2            
            
        if target < startValue:
            step += startValue-target
        return step

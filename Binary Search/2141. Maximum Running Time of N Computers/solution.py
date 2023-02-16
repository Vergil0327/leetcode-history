class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def canRun(targetMinute):
            computer = accumulatePower = 0
            for battery in batteries:
                if battery >= targetMinute:
                    computer += 1
                    continue

                accumulatePower += battery
                if accumulatePower >= targetMinute:
                    accumulatePower -= targetMinute
                    computer += 1
            return computer >= n
                        
        l, r = 0, sum(batteries)
        while l < r:
            mid = r - (r-l)//2
            if canRun(mid):
                l = mid
            else:
                r = mid-1
        return l
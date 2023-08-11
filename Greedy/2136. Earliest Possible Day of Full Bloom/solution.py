class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        time = 0
        lastGrowTime = 0
        for p, g in sorted(zip(plantTime, growTime), key=lambda x: -x[1]):
            time += p
            lastGrowTime = max(lastGrowTime, time+g)
        return lastGrowTime
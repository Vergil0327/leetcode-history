class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.prob = m*n-1 # probability, 可以想成一個一維array作為我們的random value space
        self.deleteToAlive = {} # mapping deleted num to still-alive num, keep probability continuous
    
    def to2DIndex(self, num):
        n = self.n    
        return [num//n, num%n]

    def flip(self) -> List[int]:
        deleteToAlive = self.deleteToAlive

        pick = randint(0, self.prob)
        actualPick = pick if pick not in deleteToAlive else deleteToAlive[pick]

        # important, lastAliveNum can also be a deleted num
        lastAliveNum = self.prob
        if lastAliveNum in deleteToAlive:
            lastAliveNum = deleteToAlive[lastAliveNum]
        
        deleteToAlive[pick] = lastAliveNum
        self.prob -= 1
        
        return self.to2DIndex(actualPick)

    def reset(self) -> None:
        self.prob = self.m * self.n - 1
        self.deleteToAlive = {}


# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()
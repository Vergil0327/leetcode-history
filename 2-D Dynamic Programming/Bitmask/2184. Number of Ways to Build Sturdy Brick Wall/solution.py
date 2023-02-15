# 1 <= height <= 100
# 1 <= width <= 10
# 1 <= bricks.length <= 10
# 1 <= bricks[i] <= 10
# All the values of bricks are unique.

class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        def getBricks(joinState):
            # 00100010
            # brick width = 1, 4, 2
            usedBricks = set()
            start = 0
            for i in range(width):
                if (1<<i)&joinState == 1:
                    usedBricks.add(i-start)
                    start = i
                if i == width-1:
                    usedBricks.add(i-start)
            return usedBricks

        SET = set(bricks)
        MOD = int(1e9+7)

        maxState = 1<<(width-1) # number of join positions are only width-1
        validStates = []
        for state in range(maxState):
            usedBricks = getBricks(state)
            if len(usedBricks&SET) == len(usedBricks):
                validStates.append(state)

        dp = [0] * len(validStates)
        prevdp = [1] * len(validStates) # base case, for first row, every possible state can be accepted as sturdy wall. intital value is 1

        def checkSturdy(curr, prev):
            # for i in range(width):
            #     pos = 1<<i
            #     if (curr&pos) == 1 and (prev&pos) == 1:
            #         return False
            # return True
            return (curr&prev) == 0
                

        for _ in range(height):
            for j in range(len(validStates)):
                dp[j] = 0
                for k in range(len(validStates)):
                    if checkSturdy(validStates[j], validStates[k]):
                        dp[j] += prevdp[k]
                        dp[j] %= MOD
            dp, prevdp = prevdp, dp
        return sum(prevdp)%MOD

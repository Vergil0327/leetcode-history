# TLE for Python
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        maxState = 3 ** n

        # dp[row][state][introvertsCount][extrovertsCount]
        dp = [[[[-inf]*(extrovertsCount+1) for _ in range(introvertsCount+1)] for _ in range(maxState)] for _ in range(m+1)]

        # base case
        dp[0][0][0][0] = 0

        def countPeopleType(state):
            intro = extro = 0
            for _ in range(n):
                if state%3 == 1:
                    intro += 1
                elif state%3 == 2:
                    extro += 1
                state //= 3
            return intro, extro

        prevBits = [0]*n
        currBits = [0]*n
        def addValue(prevState, state):
            for i in range(n):
                prevBits[i] = prevState%3
                currBits[i] = state%3
                prevState //= 3
                state //= 3

            happy = 0
            for i in range(n):
                if currBits[i] == 1: # current[i] is introvert
                    happy += 120
                    if i-1>=0 and currBits[i-1] > 0: happy -= 30
                    if i+1<n and currBits[i+1] > 0: happy -= 30
                    if prevBits[i] > 0: happy -= 30

                    if prevBits[i] == 1:
                        happy -= 30
                    elif prevBits[i] == 2:
                        happy += 20
                elif currBits[i] == 2: # current[i] is extrovert
                    happy += 40
                    if i-1>=0 and currBits[i-1] > 0: happy += 20
                    if i+1<n and currBits[i+1] > 0: happy += 20
                    if prevBits[i] > 0: happy += 20

                    if prevBits[i] == 1:
                        happy -= 30
                    elif prevBits[i] == 2:
                        happy += 20
            return happy

        res = 0
        for row in range(1, m+1):
            for intr in range(introvertsCount+1):
                for extr in range(extrovertsCount+1):
                    for state in range(maxState):
                        x, y = countPeopleType(state)
                        if x > intr or y > extr: continue
                        currIntr = intr-x
                        currExtr = extr-y
                        for prevState in range(maxState):
                            if dp[row-1][prevState][currIntr][currExtr] == -inf: continue
                            dp[row][state][intr][extr] = max(dp[row][state][intr][extr], dp[row-1][prevState][currIntr][currExtr] + addValue(prevState, state))

                        if row == m:
                            res = max(res, dp[row][state][intr][extr])
        return res

# precompute
# Better but still TLE at 52/67
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        maxState = 3 ** n

        # dp[row][state][introvertsCount][extrovertsCount]
        dp = [[[[-inf]*(extrovertsCount+1) for _ in range(introvertsCount+1)] for _ in range(maxState)] for _ in range(m+1)]

        # base case
        dp[0][0][0][0] = 0

        peopleType = defaultdict(tuple)
        def countPeopleType(state):
            intro = extro = 0
            for _ in range(n):
                if state%3 == 1:
                    intro += 1
                elif state%3 == 2:
                    extro += 1
                state //= 3
            return intro, extro
        for state in range(maxState):
            peopleType[state] = countPeopleType(state)

        prevBits = [0]*n
        currBits = [0]*n
        def addValue(prevState, state):
            for i in range(n):
                prevBits[i] = prevState%3
                currBits[i] = state%3
                prevState //= 3
                state //= 3

            happy = 0
            for i in range(n):
                if currBits[i] == 1: # current[i] is introvert
                    happy += 120
                    if i-1>=0 and currBits[i-1] > 0: happy -= 30
                    if i+1<n and currBits[i+1] > 0: happy -= 30
                    if prevBits[i] > 0: happy -= 30

                    if prevBits[i] == 1:
                        happy -= 30
                    elif prevBits[i] == 2:
                        happy += 20
                elif currBits[i] == 2: # current[i] is extrovert
                    happy += 40
                    if i-1>=0 and currBits[i-1] > 0: happy += 20
                    if i+1<n and currBits[i+1] > 0: happy += 20
                    if prevBits[i] > 0: happy += 20

                    if prevBits[i] == 1:
                        happy -= 30
                    elif prevBits[i] == 2:
                        happy += 20
            return happy
        additionalValue = defaultdict(int)
        for state in range(maxState):
            for prevState in range(maxState):
                additionalValue[(prevState, state)] = addValue(prevState, state)

        res = 0
        for row in range(1, m+1):
            for intr in range(introvertsCount+1):
                for extr in range(extrovertsCount+1):
                    for state in range(maxState):
                        # x, y = countPeopleType(state)
                        x, y = peopleType[state]
                        if x > intr or y > extr: continue
                        currIntr = intr-x
                        currExtr = extr-y
                        for prevState in range(maxState):
                            if dp[row-1][prevState][currIntr][currExtr] == -inf: continue
                            # score = addValue(prevState, state)
                            score = additionalValue[(prevState, state)]
                            dp[row][state][intr][extr] = max(dp[row][state][intr][extr], dp[row-1][prevState][currIntr][currExtr] + score)

                        if row == m:
                            res = max(res, dp[row][state][intr][extr])
        return res


# Sliding Window Bitmask
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, nx: int, wx: int) -> int:
        # 如果 x 和 y 相邻，需要加上的分数
        def calc(x: int, y: int) -> int:
            if x == 0 or y == 0:
                return 0
            # 例如两个内向的人，每个人要 -30，一共 -60，下同
            if x == 1 and y == 1:
                return -60
            if x == 2 and y == 2:
                return 40
            return -10
        
        n3 = 3**n
        # 预处理：每一个 mask 的三进制表示
        mask_span = dict()
        # 预处理：每一个 mask 去除最高位、乘 3、加上新的最低位的结果
        truncate = dict()

        # 预处理
        highest = n3 // 3
        for mask in range(n3):
            mask_tmp = mask
            bits = list()
            for i in range(n):
                bits.append(mask_tmp % 3)
                mask_tmp //= 3
            # 与方法一不同的是，这里需要反过来存储，这样 [0] 对应最高位，[n-1] 对应最低位
            mask_span[mask] = bits[::-1]
            truncate[mask] = [
                mask % highest * 3,
                mask % highest * 3 + 1,
                mask % highest * 3 + 2,
            ]
        
        # dfs(位置，轮廓线上的 mask，剩余的内向人数，剩余的外向人数)
        @lru_cache(None)
        def dfs(pos: int, borderline: int, nx: int, wx: int):
            # 边界条件：如果已经处理完，或者没有人了
            if pos == m * n or nx + wx == 0:
                return 0
            
            x, y = divmod(pos, n)
            
            # 什么都不做
            best = dfs(pos + 1, truncate[borderline][0], nx, wx)
            # 放一个内向的人
            if nx > 0:
                best = max(best, 120 + calc(1, mask_span[borderline][0]) \
                                     + (0 if y == 0 else calc(1, mask_span[borderline][n - 1])) \
                                     + dfs(pos + 1, truncate[borderline][1], nx - 1, wx))
            # 放一个外向的人
            if wx > 0:
                best = max(best, 40 + calc(2, mask_span[borderline][0]) \
                                    + (0 if y == 0 else calc(2, mask_span[borderline][n - 1])) \
                                    + dfs(pos + 1, truncate[borderline][2], nx, wx - 1))

            return best
        
        return dfs(0, 0, nx, wx)
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        tires.sort(key=lambda x:x[1])
        candidateTires = []
        for tire in tires:
            if not candidateTires:
                candidateTires.append(tire)
            elif tire[0] < candidateTires[-1][0]:
                candidateTires.append(tire)

        n = len(candidateTires)

        def totalTime(tire, lap):
            f, r = candidateTires[tire][0], candidateTires[tire][1]
            # f * r^(lap-1)
            # f * r^0 + f*r^1 + f*r^2 + ... + f*r^(lap-1)
            return f * (r**lap-1)//(r-1)

        minTime = [inf] * (numLaps + 1)
        for lap in range(1, numLaps+1):
            for i in range(n):
                minTime[lap] = min(minTime[lap], totalTime(i, lap))

        dp = [inf] * 1001
        dp[0] = 0
        for i in range(1, numLaps+1):
            for j in range(1, i+1):
                if j < i:
                    dp[i] = min(dp[i], dp[i-j] + changeTime + minTime[j])
                elif j == i:
                    dp[i] = min(dp[i], dp[i-j] + minTime[j])

        return dp[numLaps]
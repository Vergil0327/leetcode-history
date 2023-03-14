class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)

        # make largest value be height
        for i in range(n):
            cuboids[i].sort()
        cuboids.sort(key=lambda x:(-x[2], -x[0], -x[1]))

        # the maximum height of the stacked cuboids[:i] with last stack is j
        dp = [0] * n

        for i in range(n):
            w, l, h = cuboids[i][0], cuboids[i][1], cuboids[i][2]
            
            dp[i] = max(dp[i], h)
            for j in range(i):
                if (cuboids[j][0] >= w and cuboids[j][1] >= l) or (cuboids[j][1] >= w and cuboids[j][0] >= l):
                    dp[i] = max(dp[i], dp[j] + h)

        return max(dp)
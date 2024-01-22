distance = lambda n:pow(2,n)-1
op2_cost = 1

class Solution:
    dp = defaultdict(lambda: inf)

    def racecar(self, target: int) -> int:
        dp = self.dp
        if dp[target] < inf: return dp[target]

        n = int(log2(target+1))

        if distance(n) == target:
            return n

        # condition 1: reach target in before position
        for k in range(n):
            dp[target] = min(dp[target], n + op2_cost + k + op2_cost + self.racecar(target - distance(n) + distance(k)))

        # condition 2: reach target in after position 
        dp[target] = min(dp[target], (n+1) + op2_cost + self.racecar(distance(n+1)-target))
        return dp[target]

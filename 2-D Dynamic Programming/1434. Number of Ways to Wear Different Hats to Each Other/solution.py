# choose people has taken hat to update
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        MOD = int(1e9+7)
        
        hat2people = [[]*(1<<n) for _ in range(40)]
        for i, hatCanChoose in enumerate(hats):
            for hat in hatCanChoose:
                hat2people[hat-1].append(i)

        dp = [[0]*(1<<n) for _ in range(41)]
        
        dp[0][0] = 1 # base case
        for hat in range(40):
            for people_state in range(1<<n):
                dp[hat+1][people_state] = dp[hat][people_state]
                for person in hat2people[hat]:
                    if ((people_state>>person)&1) == 0: continue # person has NOT taken hat
                    dp[hat+1][people_state] += dp[hat][people_state^(1<<person)]
                    dp[hat+1][people_state] %= MOD
                
        return dp[40][(1<<n)-1]

# choose people hasn't taken hat to update
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        n = len(hats)
        MOD = int(1e9+7)
        
        hat2people = [[]*(1<<n) for _ in range(40)]
        for i, hatCanChoose in enumerate(hats):
            for hat in hatCanChoose:
                hat2people[hat-1].append(i)

        dp = [[0]*(1<<n) for _ in range(41)]
        
        dp[0][0] = 1 # base case
        for hat in range(40):
            for people_state in range(1<<n):
                dp[hat+1][people_state] = dp[hat][people_state]

            for people_state in range(1<<n):
                for person in hat2people[hat]:
                    if ((people_state>>person)&1) == 1: continue # person has taken hat
                    dp[hat+1][people_state + (1<<person)] += dp[hat][people_state]
                    dp[hat+1][people_state + (1<<person)] %= MOD
                
        return dp[40][(1<<n)-1]

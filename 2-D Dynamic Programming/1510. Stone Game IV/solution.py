# Top-Down DP (Recursion + Memorization)
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @functools.lru_cache(None)
        def play(n):
            # since Alice can't take any stone, she lose
            if n <= 0: return False

            # try every strategies
            # int(math.sqrt(n)) is upperbound of square number
            for r in range(1, int(math.sqrt(n))+1):
                # Alice can force Bob to lose
                if n-r*r == 0: return True

                bobCanWin = play(n-r*r) # bob's optimal play
                if not bobCanWin: return True

            # if Alice can't win in any strategy above, she lose
            return False
        return play(n)


# Bottom-Up
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * 100005
        dp[0] = 0 # always lose if no stone
        dp[1] = 1 # base case, Alice always win if only one stone exists

        for i in range(2, n+1):
            for root in range(1, int(sqrt(i))+1):
                opponent = dp[i-root*root]
                if opponent == 0:
                    dp[i] = 1
                    break
        return dp[n]

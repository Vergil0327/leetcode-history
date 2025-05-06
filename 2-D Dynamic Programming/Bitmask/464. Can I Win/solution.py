class Solution:
    """
    we can see constraint: 1 <= maxChoosableInteger <= 20
    it reminds us that we can use bitmask as choosing state to store which number we already used.

    then we use dfs to discover all possible ways if player can win
    """
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        n = maxChoosableInteger

        # edge case
        if sum(range(1, n+1)) < desiredTotal: return False
        if desiredTotal <= 0: return True

        @lru_cache(None)
        def dfs(amount, state):
            # Ouput: Return True if current player can win.
            #        Otherwise, return False.
            
            if amount >= desiredTotal:
				## Base case:
                # Opponent has reached desiredTotal and won the game on previous round.
                return False
            
            
			## General cases:
            # Current player use all available call number, and try to make a optimal choice
            for num in range(1, n+1):
                if (state>>num)&1: continue # skip already picked num
                
                isOpponentWin = dfs(amount+num, state | (1<<num))
                if not isOpponentWin: return True

            # failed to find any optimal choice to win
            return False
        return dfs(0, 0)
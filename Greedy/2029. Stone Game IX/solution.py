class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        mod3 = Counter(stone%3 for stone in stones)
        
        Alice = 1
        Bob = 0
        def win(mod3, removedSum, player):
            # special case:
            # Bob will win automatically if there are no remaining stones
            if mod3[0] + mod3[1] + mod3[2] == 0:
                if player == Bob: # if current player is Bob
                    return True
                else: # current player is Alice
                    return False

            if mod3[0] > 0:
                mod3[0] -= 1
                return not win(mod3, removedSum, 1-player) # if alice not win, it means bob win
            elif removedSum%3 == 1:
                # only survive by taking mod3[1]
                if mod3[1] > 0:
                    mod3[1] -= 1
                    return not win(mod3, removedSum+1, 1-player)
                else:
                    return False
            else: # removedSum%3 == 2
                if mod3[2] > 0:
                    mod3[2] -= 1
                    return not win(mod3, removedSum+2, 1-player)
                else:
                    return False

        tmp = mod3.copy()
        if tmp[1] > 0: # Alice take first
            tmp[1] -= 1
            if not win(tmp, 1, Bob): # means if Bob not win stone game
                return True
            # else: try other strategy
        
        tmp = mod3.copy()
        if tmp[2] > 0: # Alice take first
            tmp[2] -= 1
            if not win(tmp, 2, Bob): # means if Bob not win stone game
                return True
        
        return False
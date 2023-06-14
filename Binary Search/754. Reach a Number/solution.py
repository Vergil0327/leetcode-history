class Solution:
    def reachNumber(self, target: int) -> int:
        t = abs(target)

        # find >= position
        l, r = 0, t+1
        while l < r:
            numMoves = l + (r-l)//2
            if (moves := (1+numMoves)*numMoves//2) < t:
                l = numMoves + 1
            else:
                if moves == target: return numMoves
                r = numMoves
        distance = t-(1+l)*l//2
        if distance%2 == 0:
            return l
        else:
            nextMove = l+1
            if nextMove%2 == 1:
                return l+1
            else:
                return l+2
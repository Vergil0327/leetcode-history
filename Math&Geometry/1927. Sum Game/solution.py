class Solution:
    def sumGame(self, num: str) -> bool:
        leftCnt = rightCnt = 0
        diff = 0
        n = len(num)
        for i, ch in enumerate(num):
            if i < n//2:
                if ch == "?":
                    leftCnt += 1
                else:
                    diff += int(ch)
            else:
                if ch == "?":
                    rightCnt += 1
                else:
                    diff -= int(ch)

        d = min(leftCnt, rightCnt)
        leftCnt -= d
        rightCnt -= d
        
        if leftCnt == 0 and rightCnt == 0:
            return diff != 0

        if (leftCnt+rightCnt)%2 == 1: # Alice got last move
            return True

        if leftCnt > 0 and diff >= 0: return True
        if rightCnt > 0 and diff <= 0: return True

        remainRounds = max(leftCnt, rightCnt)//2
        return abs(diff) != remainRounds * 9

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n%2 != 0: return False

        leftLowerCount = leftUpperCount = 0
        for i in range(n):
            if locked[i] == "1":
                if s[i] == "(":
                    leftLowerCount += 1
                    leftUpperCount += 1
                else:
                    leftLowerCount -= 1
                    leftUpperCount -= 1
            else:
                leftLowerCount -= 1
                leftUpperCount += 1

            if leftLowerCount < 0:
                leftLowerCount += 2

            if leftUpperCount < 0: return False
        return leftLowerCount == 0

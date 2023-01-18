# Find Repetition Pattern
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        m, n = len(s1), len(s2)
        totalLen = m * n1

        cache = {}
        i, j = 0, 0
        while i < totalLen:
            if s1[i%m] == s2[j%n]:
                if (i%m, j%n) in cache:
                    prevI, prevJ = cache[(i%m, j%n)]
                    cycleI = i - prevI
                    cycleJ = j - prevJ
                    cycleCount = (totalLen-i) // cycleI

                    i += cycleCount * cycleI
                    j += cycleCount * cycleJ
                    if i >= totalLen: break
                else:
                    cache[(i%m, j%n)] = [i, j]
                j += 1
            i += 1
        return (j // n) // n2

# Brute Force
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        m, n = len(s1), len(s2)

        index, repeat = 0, 0
        while n1 > 0:
            for i in range(m):
                if s1[i] == s2[index]:
                    index += 1
                if index == n:
                    index = 0
                    repeat += 1
            n1 -= 1
        return repeat // n2
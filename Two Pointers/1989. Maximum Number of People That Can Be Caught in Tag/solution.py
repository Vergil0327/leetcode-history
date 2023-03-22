from typing import List

class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        n = len(team)

        j = res = 0
        for i in range(n):
            if team[i] == 1:
                j = max(j, i-dist)
                while j <= min(i+dist, n-1):
                    if team[j] == 0:
                        res += 1
                        j += 1
                        break
                    j += 1
        return res
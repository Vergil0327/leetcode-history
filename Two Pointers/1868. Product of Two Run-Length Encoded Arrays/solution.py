from typing import List

class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        i = j = 0

        n, m = len(encoded1), len(encoded2)

        res = []
        while i < n and j < m:
            curr = encoded1[i][0] * encoded2[j][0]
            k = min(encoded1[i][1], encoded2[j][1])
            encoded1[i][1] -= k
            encoded2[j][1] -= k
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1

            if not res or res[-1][0] != curr:
                res.append([curr, k])
            else:
                res[-1][1] += k

        return res

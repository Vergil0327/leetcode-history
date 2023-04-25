class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        ispal = [[False]* n for _ in range(n)]
        for length in range(1, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if s[i] == s[j]:
                    ispal[i][j] = length <= 3 or ispal[i+1][j-1]

        for i in range(n-2):
            for j in range(i+1, n-1):
                if ispal[0][i] and ispal[i+1][j] and ispal[j+1][n-1]:
                    return True
        return False

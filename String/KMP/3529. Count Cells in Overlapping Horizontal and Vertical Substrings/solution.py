
def preprocess(s):
    n = len(s)
    lps = [0]*n

    for i in range(1, n):
        j = lps[i-1]
        while j >= 1 and s[i]!=s[j]:
            j = lps[j-1]
        lps[i] = j + int(s[i] == s[j])
    return lps

# return index of target in s
def kmp(s: str, target: str):
    n = len(s)

    # preprocess
    # longest prefix suffix
    lps = preprocess(target)

    # find target word in s
    res = []
    j = 0
    for i in range(n):
        while j > 0 and s[i] != target[j]:
            j = lps[j-1]
        j = j+int(s[i] == target[j])
        if j == len(target):
            j = lps[j-1]
            res.append(i-len(target)+1)
    return res

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])

        hozizontal = ""
        for i in range(m):
            for j in range(n):
                hozizontal += grid[i][j]

        vertical = ""
        for j in range(n):
            for i in range(m):
                vertical += grid[i][j]

        indice1 = kmp(hozizontal, pattern)
        indice2 = kmp(vertical, pattern)

        res = 0
        for i in range(m):
            for j in range(n):
                pos1 = i*n+j
                idx1 = bisect_right(indice1, pos1)-1
                if idx1 >= 0 and indice1[idx1] <= pos1 < indice1[idx1]+len(pattern):
                    pos2 = i+j*m
                    idx2 = bisect_right(indice2, pos2)-1
                    if idx2 >= 0 and indice2[idx2] <= pos2 < indice2[idx2]+len(pattern):
                        res += 1
        return res
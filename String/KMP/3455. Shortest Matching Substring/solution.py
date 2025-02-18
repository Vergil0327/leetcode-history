from bisect import bisect_left

def compute_lps(pattern):
    lps = [0]*len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps

def kmp(text, pattern):
    if not pattern:
        return list(range(len(text)+1))

    lps = compute_lps(pattern)
    res = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                res.append(i - j)
                j = lps[j-1]
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
    return res

class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        asteriskIdx = [i for i in range(len(p)) if p[i] == "*"]

        part1 = p[0:asteriskIdx[0]]
        part2 = p[asteriskIdx[0]+1:asteriskIdx[1]]
        part3 = p[asteriskIdx[1]+1:]

        parts = list(filter(lambda x: len(x)>0, [part1, part2, part3]))

        validIndice = []
        for part in parts:
            indice = kmp(s, part)
            indice.sort()
            validIndice.append(indice)

        if len(parts) == 0: return 0 # ex. example 3: p = "**"

        inf = float("inf")
        res = inf
        if len(parts) == 1:
            if not validIndice[0]: return -1
            return len(parts[0])

        elif len(parts) == 2:
            if not validIndice[0] or not validIndice[1]: return -1
            for i in validIndice[0]:
                j = bisect_left(validIndice[1], i+len(parts[0]))
                if j >= len(validIndice[1]): continue

                res = min(res, validIndice[1][j]+len(parts[1])-i)
            return res if res < inf else -1
        else:
            if not validIndice[0] or not validIndice[1] or not validIndice[2]: return -1
            for i in validIndice[0]:
                j = bisect_left(validIndice[1], i+len(parts[0]))
                if j >= len(validIndice[1]): continue

                p = bisect_left(validIndice[2], validIndice[1][j]+len(parts[1]))
                if p >= len(validIndice[2]): continue

                res = min(res, validIndice[2][p]+len(parts[2]) - i)
            return res if res < inf else -1
class Solution:
    def lastSubstring(self, s):
        index = defaultdict(list)
        biggestCh = ""
        for i, c in enumerate(s):
            index[c].append(i)
            biggestCh = max(biggestCh, c)

        if len(index[biggestCh]) == 1:
            return s[index[biggestCh][0]:]

        n = len(s)
        i, j = index[biggestCh][0], index[biggestCh][1]
        k = 1
        while i+k < n and j+k < n:
            if s[i+k] == s[j+k]: # if equal, keep moving k and compare next character
                k += 1
                continue
            elif s[i+k] > s[j+k]:
                j = j+k+1
                while j < n and s[j] != biggestCh:
                    j += 1
                k = 0
            else: # s[i+k] < s[j+k]
                i = i+k+1
                while i < n and s[i] != biggestCh:
                    i += 1
                k = 0

                if i == j:
                    j += 1
                    while j < n and s[j] != biggestCh:
                        j += 1
        return s[i:]
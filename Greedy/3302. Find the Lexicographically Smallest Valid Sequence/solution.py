class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        m, n = len(word1), len(word2)

        last = [0] * n
        j = n-1
        for i in range(m-1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
        
        j = 0
        skip = False
        res = []
        for i in range(m):
            if j == n: break # already found answer

            if word1[i] == word2[j]:
                res.append(i)
                j += 1
            elif not skip and (j == n-1 or i < last[j+1]):
                skip = True
                res.append(i)
                j += 1
        
        return res if len(res) == n else []
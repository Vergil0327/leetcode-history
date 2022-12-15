class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        indexMap = defaultdict(list)
        for i, c in enumerate(s):
            indexMap[c].append(i)

        res = 0
        for word in words:
            found = True
            prevIdx = -1
            for c in word:
                if not indexMap[c]:
                    found = False
                    break
                i = bisect.bisect_left(indexMap[c], prevIdx)

                if i == len(indexMap[c]):
                    found = False
                    break
                prevIdx = indexMap[c][i]+1
            if found: # or use prevIdx == len(word)
                res += 1

        return res
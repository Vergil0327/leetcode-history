class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        pool = set()
        
        for word in startWords:
            footprint = [0] * 26
            for ch in word:
                footprint[ord(ch)-ord("a")] += 1
            pool.add(tuple(footprint))

        res = 0
        for word in targetWords:
            footprint = [0] * 26
            for ch in word:
                footprint[ord(ch)-ord("a")] += 1

            for i, cnt in enumerate(footprint):
                if cnt == 1:
                    footprint[i] -= 1
                    if tuple(footprint) in pool:
                        res += 1
                        break
                    footprint[i] += 1
        return res


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        pool = set()
        
        for word in startWords:
            bit = 0
            
            for ch in word:
                bit |= (1<<ord(ch)-ord("a"))
            pool.add(bit)

        res = 0
        for word in targetWords:
            bit = 0
            
            for ch in word:
                bit |= (1<<ord(ch)-ord("a"))
            for i in range(26):
                if (bit>>i)&1:
                    if bit^(1<<i) in pool:
                        res += 1
                        break
        return res
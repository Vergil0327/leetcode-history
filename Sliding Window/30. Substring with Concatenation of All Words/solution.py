# Hashmap: O((n-wordLen * wordsLen) * wordsLen)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        wordLen = len(words[0])
        substrLen = wordLen * len(words)
        
        def check(substring):
            match = 0
            counter = Counter(words)
            for i in range(0, len(substring), wordLen):
                if counter[substring[i:i+wordLen]] > 0:
                    counter[substring[i:i+wordLen]] -= 1
                    match += 1
                else:
                    return False
            return match == len(words)
        
        res = []
        for i in range(0, n-substrLen+1):
            substr = s[i:i+substrLen]
            if check(substr):
                res.append(i)
        return res

# Sliding Window
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        wordLen = len(words[0])
        wordsLen = len(words)
        counter = Counter(words)
        res = []

        for start in range(wordLen):
            found = defaultdict(int)
            i = start
            count = 0
            head = i
            while i < n:
                if i + wordLen > n or s[i:i+wordLen] not in counter: # skip invalid word
                    found.clear()
                    count = 0
                    head = i+wordLen
                    i = head
                elif found[s[i:i+wordLen]] == counter[s[i:i+wordLen]]: # already has enough current word. current word is excess
                    found.clear()
                    count = 0
                    head += wordLen
                    i = head
                else: # found valid word and not a excess of current count
                    found[s[i:i+wordLen]] += 1
                    i += wordLen
                    count += 1

                if count == wordsLen:
                    res.append(head)
                    found.clear()
                    count = 0
                    head += wordLen
                    i = head
        return res

# Sliding Window: TLE
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        wordLen = len(words[0])
        substrSize = wordLen * len(words)
        res = []

        l, r = 0, 0
        while r < n:
            r += 1

            while r-l == wordLen:
                counter = Counter(words)
                match = 0
                offset = 0
                while counter[s[l+offset:r+offset]] > 0:
                    counter[s[l+offset:r+offset]] -= 1
                    match += 1
                    offset += wordLen
                    if match == len(words):
                        res.append(l)
                l += wordLen

        return res

        # Brute Force, find all permutation
        # permutations = set()
        # visited = set()
        # def dfs(state):
        #     if len(state) == len(words):
        #         permutations.add("".join(state))
        #         return
        #     for i in range(len(words)):
        #         if i in visited: continue
        #         visited.add(i)
        #         state.append(words[i])
        #         dfs(state)
        #         state.pop()
        #         visited.remove(i)
        # dfs([])

        # res = []
        # length = len(words) * len(words[0])
        # for i in range(len(s)-length):
        #     if s[i:i+length] in permutations:
        #         res.append(i)
        # return res
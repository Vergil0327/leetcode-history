class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        target = Counter(word2)
        count = Counter()

        n = len(word1)
        l = r = valid = res = 0
        while r < n:
            ch = word1[r]
            count[ch] += 1
            if count[ch] == target[ch]:
                valid += 1
            r += 1

            while l < r and valid == len(target): # exist valid prefix substring in word1
                res += n-r+1

                count[word1[l]] -= 1
                if count[word1[l]] < target[word1[l]]:
                    valid -= 1
                l += 1
        return res
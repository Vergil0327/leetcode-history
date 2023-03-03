class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        
        res = 0

        length = 0
        currVowel = -inf
        numVowel = 0
        # a < e < i < o < u
        for i in range(n):
            if ord(word[i]) > currVowel:
                numVowel += 1
                length += 1
            elif ord(word[i]) == currVowel:
                length += 1
            else:
                length = 1
                numVowel = 1
            currVowel = ord(word[i])

            if numVowel == 5: # once we found all the 5 vowels, we can update res
                res = max(res, length)
        return res
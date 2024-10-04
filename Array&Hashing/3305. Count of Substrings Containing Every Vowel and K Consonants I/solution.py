class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        res = consonant = 0
        
        n = len(word)
        for i in range(n):
            count = Counter()
            consonant = 0
            for j in range(i, n):
                if word[j] in {"a", "e", "i", "o", "u"}:
                    count[word[j]] += 1
                else:
                    consonant += 1
                if len(count) == 5 and consonant == k:
                    res += 1
        return res
                
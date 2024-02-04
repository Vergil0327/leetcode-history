class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        t = 1
        n = len(word)
        while k*t <= n:
            if word[k*t:] == word[:n-k*t]:
                return t
            t += 1
        return t

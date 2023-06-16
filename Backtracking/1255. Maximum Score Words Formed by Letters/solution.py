class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counter = Counter(letters)
        scores = {chr(ord("a")+i): v for i, v in enumerate(score)}

        n = len(words)
        arr = []
        for word in words:
            arr.append(Counter(word))

        def dfs(i, counter):
            if i == n: return 0
            res = dfs(i+1, counter) # skip

            score = 0
            valid = True
            for ch, cnt in arr[i].items():
                score += scores[ch]*cnt
                counter[ch] -= cnt
                if counter[ch] < 0:
                    valid = False
            if valid:
                res = max(res, dfs(i+1, counter) + score) # pick
            for ch, cnt in arr[i].items(): # backtracking
                counter[ch] += cnt

            return res

        return dfs(0, counter)
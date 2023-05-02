class Solution:
    def maxConsecutiveAnswers(self, answers: str, k: int) -> int:
        n = len(answers)
        res = 0
        count = defaultdict(int)
        l = r = 0
        while r < n:
            count[answers[r]] += 1
            r += 1

            while count["T"] > k and count["F"] > k:
                count[answers[l]] -= 1
                l += 1

            res = max(res, r-l)
        return res
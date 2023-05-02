class Solution:
    def maxConsecutiveAnswers(self, answers: str, k: int) -> int:
        n = len(answers)
        T = F = 0

        res = 0
        
        l = r = 0
        replace = 0
        while r < n:
            if answers[r] == "T":
                T += 1
            else:
                T += 1
                replace += 1
            r += 1

            while l < r and replace > k:
                T -= 1
                if answers[l] == "F":
                    replace -= 1
                l += 1
            res = max(res, T)

        l = r = 0
        replace = 0
        while r < n:
            if answers[r] == "F":
                F += 1
            else:
                F += 1
                replace += 1
            r += 1

            while l < r and replace > k:
                F -= 1
                if answers[l] == "T":
                    replace -= 1
                l += 1
            res = max(res, F)
        return res

class Solution:
    def maxConsecutiveAnswers(self, answers: str, k: int) -> int:
        n = len(answers)
        T = F = 0

        res = 0
        
        l = r = 0
        K = k
        while r < n:
            if answers[r] == "T":
                T += 1
            else:
                T += 1
                K -= 1
            r += 1

            while l < r and K < 0:
                T -= 1
                if answers[l] == "F":
                    K += 1
                l += 1
            res = max(res, T)

        l = r = 0
        K = k
        while r < n:
            if answers[r] == "F":
                F += 1
            else:
                F += 1
                K -= 1
            r += 1

            while l < r and K < 0:
                F -= 1
                if answers[l] == "T":
                    K += 1
                l += 1
            res = max(res, F)
        return res

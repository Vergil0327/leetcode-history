# nlog(n)
class Solution:
    def bestClosingTime(self, s: str) -> int:
        n = len(s)
        sumY = [0] * (n+1)
        sumN = [0] * (n+1)
        for i in range(n-1, -1, -1):
            sumY[i] = sumY[i+1] + (1 if s[i] == "Y" else 0)
        for i in range(1, n+1):
            sumN[i] = sumN[i-1] + (1 if s[i-1] == "N" else 0)
        
        penalty = [[sum(pair), i] for i, pair in enumerate(zip(sumY, sumN))]
        return sorted(penalty)[0][1]

# optimzed, O(n)
class Solution:
    def bestClosingTime(self, s: str) -> int:
        n = len(s)
        sumY = [0] * (n+1)
        sumN = [0] * (n+1)
        for i in range(n-1, -1, -1):
            sumY[i] = sumY[i+1] + (1 if s[i] == "Y" else 0)
        for i in range(1, n+1):
            sumN[i] = sumN[i-1] + (1 if s[i-1] == "N" else 0)
        
        minPenalty = inf
        ans = -1
        for i, pair in enumerate(zip(sumY, sumN)):
            penalty = sum(pair)
            if penalty < minPenalty:
                minPenalty = penalty
                ans = i
        return ans
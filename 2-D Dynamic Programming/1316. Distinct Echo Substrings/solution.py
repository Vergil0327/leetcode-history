# use dp[i][j] to check if substring is echo string or not efficiently and count
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        dp = [[0]*n for _ in range(n)]

        res = 0
        SET = set()
        for i in range(n):
            for j in range(i+1, n):
                if text[i] == text[j]:
                    if i-1 >= 0:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = 1
                    
                if dp[i][j] >= j-i: # which means text[i-dp[i][j]+1:i+1] == text[i+1:j+1]
                    if text[i+1:j+1] not in SET:
                        SET.add(text[i+1:j+1])
                        res += 1
        return res


# Brute Force
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        def check(substring):
            half = len(substring) // 2
            return substring[:half] == substring[half:]

        res = 0
        visited = set()
        for length in range(2, n := len(text) + 1, 2):
            for i in range(n - length + 1):
                if check(word := text[i:i+length]) and word not in visited:
                    res += 1
                    visited.add(word)
        return res

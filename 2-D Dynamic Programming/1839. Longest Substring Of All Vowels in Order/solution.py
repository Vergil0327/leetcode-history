class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        

        vowels = ["", "a", "e", "i", "o", "u"]
        m = len(vowels)

        # dp[i][vowel]: then longest length of beautiful substring considering word[:i] and current character is vowels[j]
        dp = [[-inf]*m for _ in range(n+1)]
        
        # base case: once we got vowels[1] ("a"), we can think it can append after ""
        for i in range(n+1):
            dp[i][0] = 0

        word = "#" + word # shift to 1-indexed
        for i in range(1, n+1): # vowel from vowels[1] to vowels[n-1]
            for j in range(1, m):
                # XXXXXXX i/o [o]
                # XXXXXXX  "" [a]
                #         i-1  i
                if word[i] == vowels[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])+1
        
        res = 0
        for i in range(1, n+1):
            res = max(res, dp[i][m-1])
        return res
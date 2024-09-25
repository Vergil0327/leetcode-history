class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)

        def exist(prefix):
            for word in words:
                if word.startswith(prefix):
                    return True
            return False

        dp = [inf] * (n + 1)
        dp[0] = 0

        l = 0
        for r in range(1, n + 1):
            while l < r and not exist(target[l:r]):
                l += 1

            if l == r: return -1

            dp[r] = dp[l] + 1
        
        return dp[n]
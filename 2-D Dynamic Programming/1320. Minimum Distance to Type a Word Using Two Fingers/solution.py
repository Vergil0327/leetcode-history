# first try
class Solution:
    def minimumDistance(self, word: str) -> int:
        grid = dict()
        for i in range(26): # A-Z -> 0-25
            grid[i] = (i//6, i%6)

        def dist(ch1, ch2):
            x1, y1 = grid[ch1]
            x2, y2 = grid[ch2]
            return abs(x1 - x2) + abs(y1 - y2)

        # dp[i][finger1][finger2] = min(dp[i-1][prev_finger1][finger2] + dist(finger1, prev_finger1), dp[i-1][finger1][prev_finger2] + dist(finger2, prev_finger2))

        n = len(word)
        dp = [[[inf] * 26 for _ in range(26)] for _ in range(n)]

        for i in range(n):
            curr = ord(word[i]) - ord("A")
            for prev in range(26):
                for otherFinger in range(26):
                    dp[i][curr][otherFinger] = min(dp[i][curr][otherFinger], (dp[i-1][prev][otherFinger] if i-1 >= 0 else 0)+ dist(prev, curr))
            for prev in range(26):
                for otherFinger in range(26):
                    dp[i][otherFinger][curr] = min(dp[i][otherFinger][curr], (dp[i-1][otherFinger][prev] if i-1 >= 0 else 0) + dist(prev, curr))
            
        return min(map(min, dp[n-1]))

class Solution:
    def minimumDistance(self, word: str) -> int:
        grid = dict()
        for i in range(26): # A-Z -> 0-25
            grid[i] = (i//6, i%6)

        def dist(ch1, ch2):
            x1, y1 = grid[ch1]
            x2, y2 = grid[ch2]
            return abs(x1 - x2) + abs(y1 - y2)

        # dp[i][finger1][finger2] = min(dp[i-1][prev_finger1][finger2] + dist(finger1, prev_finger1), dp[i-1][finger1][prev_finger2] + dist(finger2, prev_finger2))

        n = len(word)
        dp = [[[inf] * 26 for _ in range(26)] for _ in range(n)]

        for i in range(n):
            curr = ord(word[i]) - ord("A")
            for prev in range(26):
                for otherFinger in range(26):
                    dp[i][curr][otherFinger] = min(dp[i][curr][otherFinger], (dp[i-1][prev][otherFinger] if i-1 >= 0 else 0)+ dist(prev, curr))
                    dp[i][otherFinger][curr] = min(dp[i][otherFinger][curr], (dp[i-1][otherFinger][prev] if i-1 >= 0 else 0) + dist(prev, curr))
            
        return min(map(min, dp[n-1]))

# space optimization
class Solution:
    def minimumDistance(self, word: str) -> int:
        def dist(ch1, ch2):
            x1, y1 = (ch1//6, ch1%6)
            x2, y2 = (ch2//6, ch2%6)
            return abs(x1 - x2) + abs(y1 - y2)

        distance = [[0] * 26 for _ in range(26)]
        for finger1 in range(26):
            for finger2 in range(26):
                distance[finger1][finger2] = dist(finger1, finger2)

        # dp[i][finger1][finger2] = min(dp[i-1][prev_finger1][finger2] + dist(finger1, prev_finger1), dp[i-1][finger1][prev_finger2] + dist(finger2, prev_finger2))

        n = len(word)
        prevdp = [[0] * 26 for _ in range(26)]
        dp = [[inf] * 26 for _ in range(26)]

        for i in range(n):
            curr = ord(word[i]) - ord("A")            
            for prev in range(26):
                for otherFinger in range(26):
                    dp[curr][otherFinger] = min(dp[curr][otherFinger], prevdp[prev][otherFinger]+ distance[prev][curr])
                    dp[otherFinger][curr] = min(dp[otherFinger][curr], prevdp[otherFinger][prev] + distance[prev][curr])
            prevdp = dp
            dp = [[inf] * 26 for _ in range(26)]
            
        return min(map(min, prevdp))
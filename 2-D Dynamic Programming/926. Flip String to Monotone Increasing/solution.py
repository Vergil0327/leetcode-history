# Prefix Sum + Suffix Sum
# https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/183851/C%2B%2BJava-4-lines-O(n)-or-O(1)-DP
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        count1FromLeft = [0] * (n+1)
        for i in range(1, n+1):
            count1FromLeft[i] = count1FromLeft[i-1] + (1 if s[i-1] == "1" else 0)
        count0FromRight = [0] * (n+1)
        for i in range(n-1, -1, -1):
            count0FromRight[i] = count0FromRight[i+1] + (1 if s[i] == "0" else 0) 

        # for every position i to make left and right substring valid is
        # make left-side 1 to 0 and make right-side 0 to 1
        res = float("inf")
        for i in range(n+1):
            res = min(res, count1FromLeft[i] + count0FromRight[i])
        return res

# Most Optimzied, very straight-forward, we just maintin a valid s[:i]
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # occurence of 1 until s[:i]
        occur1 = 0
        
        # counter for flips to make s[:i] valid. 0->1, 1->0
        flips = 0
        
        # maintain a valid s[:i] which is monotone increasing
        n = len(s)
        for i in range(n):
            if s[i] == "1":
                occur1 += 1
                # we don't need to flip tailing 1
            else:
                # we can:
                # 1. flip all the previous 1 to 0 -> s[:i] becomes "000000"
                # 2. flip current 0 to 1          -> s[:i] becomes "XXXXX1"
                flips = min(occur1, flips+1)
        return flips

# https://www.youtube.com/watch?v=D8xa8ZMV7AI
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        # dp[i] : the minimum number of flips to make s[:i] monotone increasing.
        # dp[i][0] : the minimum number of flips to make valid s[:i] ending at 0 (i.e. all letters are "0")
        # dp[i][1] : the minimum number of flips to make valid s[:i] ending with 1
        
        dp = [[0, 0] for _ in range (n+1)]
        for i in range(1, n+1):
            if s[i-1] == "0":
                # "XXXX0" + "0" -> no need for flip
                dp[i][0] = dp[i-1][0]
                # XXXX0 + "0" -> flip current "0" to "1" to make s valid to end with "1"
                # XXXX1 + "0" -> flip current "0" to "1"
                dp[i][1] = min(dp[i-1][0], dp[i-1][1])+1
            else:
                # "XXXXX0" + "1" -> flip current "1" to "0"
                dp[i][0] = dp[i-1][0] + 1
                # "XXXXX0" + "1" no need to flips
                # "XXXXX1" + "1"
                dp[i][1] = min(dp[i-1][1], dp[i-1][0])
        return min(dp[n][0], dp[n][1])

# BFS solution, TLE
class SolutionTLE:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        
        def check(s):
            for i in range(n):
                if s[i] == "1":
                    if len(set(s[:i])) == 1 and len(set(s[i:])) == 1:
                        return True
                    else:
                        return False
            return len(set(s)) == 1
        
        que = deque([s])
        cnt = 0
        while que:
            sz = len(que)
            for _ in range(sz):
                node = que.popleft()
                
                if check(node):
                    return cnt
                
                for j in range(n):
                    if s[j] == "0":
                        que.append(s[:j]+"1"+s[j+1:])
                    else:
                        que.append(s[:j]+"0"+s[j+1:])
            cnt += 1
        return cnt
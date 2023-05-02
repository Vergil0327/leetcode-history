class Solution:
    def getLengthOfOptimalCompression(self, s: str, K: int) -> int:
        n = len(s)

        # handle special case: s = "aaaaa...aaaa" where s.length = 100
        if K == 0: # just encode
            prev = "#"
            cnt = 0
            res = 0
            for i in range(n):
                if s[i] != prev:
                    if prev != "#":
                        res += 1
                        res += len(str(cnt)) if cnt > 1 else 0
                    cnt = 1
                    curr = s[i]
                else:
                    cnt += 1
            res += 1
            res += len(str(cnt)) if cnt > 1 else 0
            return res


        s = "#" + s

        # dp[i][k][ch][cnt]
        # dp = [[[[inf]*101 for _ in range(27)] for _ in range(K+1)]for _ in range(n+1)]
        dp = [[[[inf]*11 for _ in range(27)] for _ in range(K+2)]for _ in range(n+1)]

        dp[0][0][26][0] = 0 # minimum length for 0 characters, 0 removed, use 26 to represent empty character (0-25 is a-z), 0 number of character

        for i in range(n):
            for k in range(min(i, K)+1):
                for ch in range(27):
                    for cnt in range(11):
                        curr = dp[i][k][ch][cnt]
                        if curr == inf: continue # invalid state

                        # delete s[i+1]
                        dp[i+1][k+1][ch][cnt] = min(dp[i+1][k+1][ch][cnt], curr)

                        # keep s[i+1]
                        if ch != ord(s[i+1])-ord("a"):
                            dp[i+1][k][ord(s[i+1])-ord("a")][1] = min(dp[i+1][k][ord(s[i+1])-ord("a")][1], curr+1)
                        else:
                            added = 0
                            if cnt == 1: # "a" -> "a2"
                                added = 1
                            elif cnt > 1 and cnt <= 8: # "a2" -> "a9"
                                added = 0
                            elif cnt == 9: # "a9" -> "a10"
                                added = 1
                            elif cnt > 9: # "a10" -> "a99"
                                added = 0
                            dp[i+1][k][ch][min(10, cnt+1)] = min(dp[i+1][k][ch][min(10, cnt+1)], curr+added)
        res = inf
        for ch in range(27):
            for cnt in range(11):
                res = min(res, dp[n][K][ch][cnt])
        return res



class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(i: int, last: str, last_count: int, k: int) -> int:
            if k < 0:
                return 9999
            if i >= len(s):
                return 0
            if s[i] == last:
                incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
                return incr + counter(i + 1, last, last_count + 1, k)
            else:
                keep_counter = 1 + counter(i + 1, s[i], 1, k)
                del_counter = counter(i + 1, last, last_count, k - 1)
                return min(keep_counter, del_counter)
        
        return counter(0, "", 0, k)
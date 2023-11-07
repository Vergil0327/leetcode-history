class Solution:
    def longestAwesome(self, s: str) -> int:
        n = len(s)

        seen = {0: -1}
        res = 0
        state = 0
        for i in range(n):
            d = int(s[i])
            state = state ^ (1<<d)

            if state in seen: # even palindrome
                res = max(res, i-seen[state])

            
            # odd palindrome
            for j in range(10):
                if (new_state := state^(1<<j)) in seen:
                    res = max(res, i-seen[new_state])

            if state not in seen: # 由於要找最長awesome substring, 記錄該state的第一個index
                seen[state] = i

        return res

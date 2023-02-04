# top-down
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        counters = []
        for sticker in stickers:
            counters.append(Counter(sticker))
        
        dp = {} # key: subseq. of target, value: minimum number of stickers
        def dfs(target, stick):
            if target in dp: return dp[target]

            res = 1 if stick else 0
            
            remains = ""
            for ch in target:
                if ch in stick and stick[ch] > 0:
                    stick[ch] -= 1
                else:
                    remains += ch
            
            if remains:
                used = float("inf")
                for stk in counters:
                    if remains[0] not in stk: continue
                    used = min(used, dfs(remains, stk.copy()))
                
                dp[remains] = used
                res = res + used if used != float("inf") else used
            return res

        res = dfs(target, {})
        return res if res != float('inf') else -1

# bottom-up
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:        
        # dp[remain_state]: the minimum number of stickers for remain state
        # ex. target = "target"
        # initially, remain_state = 111111 -> means current remain state = "target"
        # remain_state = 111000 -> means current remain state = "tar"
        n = len(target)
        dp = [inf] * (1<<n)
        dp[0] = 0

        counters = [Counter(sticker) for sticker in stickers]
        def findNextState(state, sticker, target):
            n = len(target)

            cpy = sticker.copy()
            for i in range(n):
                if ((state>>i)&1) == 0 and cpy[target[i]] > 0:
                    state |= (1<<i)
                    cpy[target[i]] -= 1

            return state
        
        for state in range(1<<n):
            if dp[state] == inf: continue
            
            for sticker in counters:
                next_state = findNextState(state, sticker, target)
                dp[next_state] = min(dp[next_state], dp[state]+1)

        return dp[(1<<n)-1] if dp[(1<<n)-1] != inf else -1

# TLE
class Solution_TLE:
    def minStickers(self, stickers: List[str], target: str) -> int:        
        # dp[i][state]: the minimum number of stickers for remain state by using stickers[0:i]
        m = len(stickers)
        n = len(target)
        dp = [[inf] * (1<<n) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 0

        counters = [Counter(sticker) for sticker in stickers]
        counters = [{}] + counters

        for i in range(1, m+1):
            for state in range(1, 1<<n):
                count = counters[i].copy()
                dp[i][state] = dp[i-1][state]

                submask = state
                for j in range(n):
                    if (submask>>j)&1 and count[target[j]] > 0:
                        count[target[j]] -= 1
                        submask ^= (1<<j)
                
                dp[i][state] = min(dp[i][state], dp[i][submask]+1)
                
        return dp[m][(1<<n)-1] if dp[m][(1<<n)-1] != inf else -1
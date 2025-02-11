class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        OFFSET = ord("a")

        dp = [[[-1]*4 for _ in range(27)] for _ in range(n+1)]
        def dfs(i, prev, consecutive):
            if i >= n:
                return 0 if consecutive >= 3 else inf
            if dp[i][prev][consecutive] != -1: return dp[i][prev][consecutive]
            
            cur = ord(caption[i])-OFFSET
            res = inf

            if prev != 26:
                cost = dfs(i+1, prev, min(3, consecutive+1)) + abs(cur - prev)
                res = min(res, cost)

            if prev == 26 or consecutive >= 3:
                for j in range(26):
                    cost = dfs(i+1, j, 1)
                    res = min(res, cost + abs(cur-j))

            dp[i][prev][consecutive] = res
            return dp[i][prev][consecutive]
                
        cost = dfs(0, 26, 0)
        if cost == inf: return ""

        self.res = [""] * n
        def build(i, prev, consecutive):
            if i >= n: return

            cur = ord(caption[i])-OFFSET
            ch, cost = 26, inf

            # turn caption[i] into prev and append
            if prev != 26:
                cst = dfs(i+1, prev, min(3, consecutive+1))
                if cst < inf and cst + abs(cur - prev) < cost:
                    cost = cst + abs(cur - prev)
                    ch = prev

            # start new groups with j character
            if prev == 26 or consecutive >= 3:
                for j in range(26):
                    cst = dfs(i+1, j, 1)
                    if cst < inf:
                        if cst + abs(cur - j) < cost:
                            cost = cst + abs(cur  - j)
                            ch = j
                        elif cst + abs(cur  - j) == cost:
                            ch = min(ch, j)

            self.res[i] = chr(ch + OFFSET)
            if ch == prev:
                build(i+1, ch, min(3, consecutive+1))
            else:
                build(i+1, ch, 1)
        
        build(0, 26, 0)
        return "".join(self.res)
    

class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        inf = float('inf')

        if n < 3: return ""
        
        # Initialize dp array with tuples (cost, char)
        # Using inf for invalid states to simplify comparison
        # dp[i][ch][j] - means [minimum operations, best character] to have streak of j symbols `ch` ending at i-th index 
        dp = {}
        GOOD = (0, 0)
        BAD = (inf, 27)
        
        # Base case initialization
        for last in range(26):
            for repetition in range(4):
                dp[n,last,repetition] = GOOD if repetition >= 3 else BAD
        
        # Bottom-up DP
        for i in range(n-1, -1, -1):
            curr_ch = ord(caption[i]) - ord('a')
            
            for last in range(26):
                for repetition in range(4):
                    best_char = 27
                    best_cost = inf
                    
                    for ch in range(26):
                        # Skip if breaking consecutive character constraint
                        if 1 <= repetition < 3 and ch != last: continue

                        change_cost = abs(curr_ch - ch)
                            
                        next_cnt = min(3, 1 + (ch == last) * repetition)
                        
                        cost, _ = dp[i + 1,ch,next_cnt]
                        if cost == inf: continue
                            
                        # Update if we found a better cost
                        if (best := change_cost + cost) < best_cost:
                            best_cost = best
                            best_char = ch
                            
                    dp[i,last,repetition] = (best_cost, chr(best_char + ord('a')))
        
        # Build result string
        result = [''] * n
        curr = dp[0,0,0]
        repetition = 0
        
        for i in range(n):
            result[i] = curr[1]
            
            if i != n-1:
                next_cnt = min(3, 1 + (i > 0 and result[i] == result[i-1]) * repetition)
                repetition = next_cnt
                curr = dp[i + 1,ord(result[i]) - ord('a'),next_cnt]
        
        return ''.join(result)
    

class Solution:
    """
    aabbcc : aaaccc

    abddcc : bbbccc

    addee  : ddddd

    azzk   : kkkk

    azzsk  : sssss
    """
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)

        if n < 3: return ""

        # Find the median character of substring, and compute the required operation
        @cache
        def get_cost(substring: str):
            substring = sorted(list(substring))
            length = len(substring)
            mc = substring[(length - 1) // 2]
            target = ord(mc)
            cost = 0
            for c in substring:
                if c == mc: continue
                cost += abs(ord(c) - target)
            return cost, mc * length
        
        # dp[i][0] is the minimun operations for caption[:i]
        # dp[i][1] is the caption after minimun operations
        # NOTE "!" can be any string, since it should not appear in the final answer
        dp = [(float("inf"), "!")] * (n + 1)
        dp[0] = None

        # Initial dp with base cases
        for i in range(3, min(6, n + 1)):
            dp[i] = get_cost(caption[:i])
        
        # Start Dynamic Programing
        for i in range(6, n + 1):
            dp[i] = (float("inf"), "!")
            
            # Compare the three possible partitions
            for j in range(3, 6):
                cost, s = get_cost(caption[i - j:i])
                pre_cost, pre_s = dp[i-j]
                compare = cost + pre_cost
                
                if dp[i][0] > compare:
                    dp[i] = (compare, pre_s + s)
                elif dp[i][0] == compare:
                    dp[i] = (dp[i][0], min(dp[i][1], pre_s + s))

            # For saving memory, otherwise it will MLE
            dp[i-5] = None
            
        return dp[-1][1]
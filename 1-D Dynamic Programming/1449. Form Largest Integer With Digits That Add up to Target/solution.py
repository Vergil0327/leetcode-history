# Top-Down + Memorization
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        n = len(cost)
        cost2Idx = defaultdict(list)
        for i in range(n-1, -1, -1):
            cost2Idx[cost[i]].append(i)

        @functools.lru_cache(None)
        def dfs(i, target):
            if target == 0: return ""
            if i == n or target < 0: return "N"
            
            s1 = dfs(i+1, target)
            s2 = dfs(i, target-cost[i]) + str(cost2Idx[cost[i]][0]+1)

            res = []
            if "N" not in s1: res.append(s1)
            if "N" not in s2: res.append(s2)
            
            if not res: return "N"
            if len(res) == 1: return res[0]

            # or simply just this one line
            # return sorted(res, key=lambda s: (len(s), s))[-1] if res else "N"
            if len(s1) > len(s2):
                return s1
            elif len(s2) > len(s1):
                return s2
            else:
                return s1 if s1 > s2 else s2
        
        ans = dfs(0, target)
        return "".join(sorted(ans, reverse=True)) if ans != "N" else "0"


# Bottom-Up
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        n = len(cost)
        PLACEHOLDER = "#"
        
        # dp[cost] : the maximum integer 
        dp = [""] * 5001
        for c in range(1, target+1):
            dp[c] = PLACEHOLDER
            for i in range(1, n+1): # 1-9
                if c < cost[i-1] or dp[c-cost[i-1]] == PLACEHOLDER: continue
                candidate = dp[c-cost[i-1]] + str(i)
                if len(candidate) > len(dp[c]) or (len(candidate) == len(dp[c]) and candidate > dp[c]):
                    dp[c] = candidate
        
        return dp[target] if dp[target] != PLACEHOLDER else "0"

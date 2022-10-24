class Solution:
    def maxLength(self, arr: List[str]) -> int:
        uniq = [x for x in arr if len(set(x)) == len(x)]

        @functools.lru_cache()
        def dfs(state, i):
            if i == len(uniq): return 0

            longest = 0
            for j in range(i, len(uniq)):
                if any(x in state for x in uniq[j]):
                    continue

                longest = max(longest, len(uniq[j]) + dfs(state+uniq[j], j+1))
            return longest
        
        return dfs("", 0)

class BottomUpSolution:
    def maxLength(self, arr: List[str]) -> int:
        uniq = [x for x in arr if len(set(x)) == len(x)]
        
        dp = []
        
        # exhaustively try all possible combination
        for i, word in enumerate(uniq):
            wordSet = set(word)
            for i in range(len(dp)):
                if bool(wordSet & dp[i][0]): continue
                dp.append((dp[i][0] | wordSet, dp[i][1]+len(word)))
            dp.append((wordSet, len(word)))
        
        return max(length for _, length in dp) if dp else 0

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        maxLen = max(len(word) for word in words)

        # length2wordCost = {length: {word: cost}}
        length2wordCost = [{} for _ in range(maxLen+1)]
        for word, cost in zip(words, costs):
            if word not in length2wordCost[len(word)]:
                length2wordCost[len(word)][word] = cost
            else:
                length2wordCost[len(word)][word] = min(length2wordCost[len(word)][word], cost)

        lengths = [i for i in range(len(length2wordCost)) if len(length2wordCost[i]) > 0]

        n = len(target)

        dp = [inf] * (n+1)
        dp[0] = 0

        for i in range(n):
            for length in lengths:
                if i+length > n: break
                
                word = target[i:i+length]
                if word in length2wordCost[length]:
                    cost = length2wordCost[length][word]
                    if dp[i+length] > dp[i] + cost:
                        dp[i+length] = dp[i] + cost

                
        return dp[n] if dp[n] < inf else -1

# MLE
# class Solution:
#     def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
#         maxLen = max(len(word) for word in words)

#         # length2wordCost = {length: {word: cost}}
#         length2wordCost = [defaultdict(lambda: inf) for _ in range(maxLen+1)]
#         for word, cost in zip(words, costs):
#             length2wordCost[len(word)][word] = min(length2wordCost[len(word)][word], cost)

#         lengths = [i for i in range(len(length2wordCost)) if len(length2wordCost[i]) > 0]

#         n = len(target)

#         dp = [-1] * n
#         def dfs(i):
#             if i == n: return 0
#             if dp[i] != -1: return dp[i]

#             dp[i] = inf
#             for length in lengths:
#                 if i + length > n: break

#                 cost = length2wordCost[length][target[i:i+length]]
#                 if cost < inf: # target[i:i+length] exists in words
#                     dp[i] = min(dp[i], dfs(i+length) + cost)
#             return dp[i]
#         ans = dfs(0)
#         return ans if ans < inf else -1

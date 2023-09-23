# O(n * L*L + nlogn), L is len(word)
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = defaultdict(lambda: 1)

        # O(L*L)
        def check(word):
            maxLen = 1
            for j in range(len(word)):
                s = word[:j] + word[j+1:]
                if s in dp:
                    maxLen = max(maxLen, dp[s]+1)
            return maxLen

        for word in sorted(words, key=len):
            dp[word] = check(word)

        return max(dp.values())

# daily challenge 2023/09/23
class Solution:
    def longestStrChain(self, words: List[str]) -> int:        
        dp = defaultdict(lambda: 1)
        for word in sorted(words, key=len):
            for i in range(len(word)):
                if (s := word[:i] + word[i+1:]) in dp:
                    dp[word] = max(dp[word], dp[s]+1)

        return max(dp.values())
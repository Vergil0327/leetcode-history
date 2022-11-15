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

# Barely TLE
# O(n^2*L*L)
# Runtime: 4524 ms, faster than 8.47% of Python3 online submissions
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # dp[i]: the length of the longest possible word chain of words[:i]
        words.sort(key=len)
        
        # O(L*L), string generation is also O(L)
        def check(word, target):
            for i in range(len(target)+1):
                s = target[:i] + target[i+1:]
                if s == word: return True
            return False

        # O(n^2)
        dp = [1] * len(words)
        for i in range(len(words)):
            for j in range(0, i):
                if len(words[i])-1 != len(words[j]): continue
                if check(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
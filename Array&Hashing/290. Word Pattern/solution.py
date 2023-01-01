# Elegant
# we don't care which word match which pattern, thus, we only need to check if their length equal after removing duplicate
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern): return False

        return len(set(words)) == len(set(pattern)) == len(set(zip(words, pattern)))

# Straightforward
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2pattern = {}
        pattern2word = {}
        words = s.split()
        patterns = list(pattern)
        if len(words) != len(patterns): return False

        for word, p in zip(words, patterns):
            if word not in word2pattern:
                if p in pattern2word:
                    if pattern2word[p] != word: return False
                pattern2word[p] = word
                word2pattern[word] = p
            else:
                if word2pattern[word] != p:
                    return False
        return True
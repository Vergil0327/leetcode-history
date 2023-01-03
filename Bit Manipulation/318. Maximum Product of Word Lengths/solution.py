# Brute Force
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = list(set(words))

        maxProduct = 0
        for i in range(len(words)):
            a = set(words[i])
            for j in range(i+1, len(words)):
                b = set(words[j])
                if not a&b:
                    maxProduct = max(maxProduct, len(words[i]) * len(words[j]))
        return maxProduct

# Bit Manipulation
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = list(set(words))

        bits = defaultdict(int) # { bitmask: len(word)}
        for word in words:
            bitmask = 0
            for c in word:
                bitmask |= 1<<(ord(c)-ord("a"))
            bits[bitmask] = max(bits[bitmask], len(word))

        maxProduct = 0
        for mask1 in bits:
            for mask2 in bits:
                if mask1 == mask2: continue
                if not mask1&mask2:
                    maxProduct = max(maxProduct, bits[mask1] * bits[mask2])
        return maxProduct
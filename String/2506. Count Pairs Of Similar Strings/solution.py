# Brute Force: O(n^3)
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        sets = [set(word) for word in words]
        
        n = len(words)
        cnt = 0
        for i in range(0, n-1):
            for j in range(i+1, n):
                # if len(sets[i] & sets[j]) == len(sets[i]|sets[j]):
                if sets[i] == sets[j]:
                    cnt += 1
        return cnt

# Bitmask solution
# Intuition:
# since only 26 letters at most, we can use bitmask to represent as string
# time: O(n*L) where n is length of words and L is length of word
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        freq = defaultdict(int)
        for word in words:
            mask = 0
            for ch in word:
                mask |= 1 << ord(ch)-ord("a")
            if mask in freq: # found pairs
                res += freq[mask]
            freq[mask] += 1
        return res
class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        n = len(words)
        
        count = Counter()
        for word in words:
            for ch in word:
                count[ch] += 1
        
        pairs = mid = 0
        for cnt in count.values():
            pairs += cnt//2
            mid += cnt%2
        
        sizes = [len(word) for word in words]
        sizes.sort()

        for i in range(n):
            need_pair = sizes[i]//2
            if pairs >= need_pair:
                pairs -= need_pair
                sizes[i] -= need_pair*2
            else:
                break

        mid += pairs * 2
        res = 0
        for i in range(n):
            if sizes[i] == 0:
                res += 1
            elif sizes[i] == 1 and mid > 0:
                mid -= 1
                res += 1
            else:
                break
        return res

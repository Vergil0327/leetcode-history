class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = list(sorted(Counter(word).values()))
        n = len(freq)

        res = len(word)
        pre_deleted = j = 0
        sufsum = sum(freq)
        for i in range(n):
            while j < len(freq) and freq[j]-freq[i] <= k:
                sufsum -= freq[j]
                j += 1
            res = min(res, pre_deleted + sufsum-(n-j)*(freq[i]+k))
            pre_deleted += freq[i]
        return res

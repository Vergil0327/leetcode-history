class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = l = r = 0
        window = defaultdict(int)
        max_freq = 0
        while r < n:
            window[s[r]] += 1
            max_freq = max(max_freq, window[s[r]])
            r += 1

            while l < r and r-l-max_freq > k:
                window[s[l]] -= 1
                l += 1
            res = max(res, r-l)
        return res

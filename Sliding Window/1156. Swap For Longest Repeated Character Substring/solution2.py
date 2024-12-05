from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)

        i, n = 0, len(text)
        res = 1
        while i < n:
            left = right = 0

            while (i + left < n) and (text[i] == text[i + left]):
                left += 1

            start = i + left + 1
            while (start + right < n) and (text[i] == text[start + right]):
                right += 1

            res = max(res, min(count[text[i]], left + right + 1))
            i += left

        return res
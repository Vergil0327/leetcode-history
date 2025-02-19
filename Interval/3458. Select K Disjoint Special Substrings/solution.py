class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        minIdx = defaultdict(lambda: inf)
        maxIdx = defaultdict(lambda: -inf)

        chs = set()
        for i, ch in enumerate(s):
            minIdx[ch] = min(minIdx[ch], i)
            maxIdx[ch] = max(maxIdx[ch], i)
            chs.add(ch)

        intervals = []
        for ch in minIdx.keys():
            l, r = minIdx[ch], maxIdx[ch]

            valid = True
            while l < r:
                if minIdx[s[l]] < minIdx[ch]:
                    valid = False
                    break

                r = max(r, maxIdx[s[l]])
                l += 1
            if valid and r-minIdx[ch]+1 < len(s): # The substring is not the entire string s.
                intervals.append([minIdx[ch], r])

        intervals.sort(key=lambda inv: inv[1])

        count = 0
        prevR = -1
        for l, r in intervals:
            if l > prevR:
                count += 1
                prevR = r
        return count >= k
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)

        n = len(text)
        res = 0
        for ch in count:
            l = r = 0
            cnt = Counter()
            while r < n:
                cnt[text[r]] += 1
                r += 1

                while l < r and r-l-cnt[ch] > 1: # non_repeated_cnt = window_length - cnt[ch] =  (r-l) - cnt[ch]
                    cnt[text[l]] -= 1
                    if cnt[text[l]] == 0:
                        del cnt[text[l]]
                    l += 1

                if count[ch] - cnt[ch] > 0: # can swap 1 character
                    res = max(res, r-l)
                if len(cnt) == 1 and ch in cnt: # repeated `ch` substring
                    res = max(res, r-l)
                
        return res

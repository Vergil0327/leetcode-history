"""
先計算每個character的frequency
s = [X O O O O O O O O O X O O O O X]
       [    可能解      ]   [     ]
如果有任何一個character他的總frequency < k, 那麼合法的substring必次存在於這類character之間
我們持續遞歸處理, 直到整個string內的所有字母的frequency都 >= k, 即返回len(s)
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counter = Counter(s)

        if min(counter.values()) >= k: return len(s)

        res = l = 0
        while l < len(s):
            if counter[s[l]] < k:
                l += 1
                continue

            # s[l:r]內的所有字母總次數皆>=k
            # 從裡面繼續持續遞歸搜索合法解
            r = l
            while r < len(s) and counter[s[r]] >= k:
                r += 1
            res = max(res, self.longestSubstring(s[l:r], k))
            l = r

            l += 1
        return res
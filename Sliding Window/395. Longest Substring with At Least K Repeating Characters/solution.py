"""
由於只要有左右邊界`l`, `r`, 就能定義出subarray, substring
所以首先想到的是two pointers能不能解
但觀察後發現雙指針行不通, 為了滿足每個character都至少有k個, 右pointer會持續往右移動直到盡頭
沒有移動左pointer的條件

所以這題巧妙的是我們必須在sliding window上加個限制, 好讓左pointer有機會移動

由於s長度為n的時候, 每個字母的frequency最低為n/26次, 最高的frequency就是n次
所以我們可以在sliding window上加個條件是:

在sliding window內, 最多有m種不相同的character
然後我們遍歷所有可能的情況: for m in range(1, n+1)
這樣我們就能在每次的sliding window內嘗試更新result, 條件為:
當所有character的frequency都至少有k個時, 我們就能更新result
"""
class Solution_TLE:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        
        res = 0
        for m in range(1, n+1):
            window = defaultdict(int)
            l = r = 0
            while r < n:
                window[s[r]] += 1
                r += 1

                while l < r and len(window) > m:
                    window[s[l]] -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                    l += 1
                if min(window.values()) >= k:
                    res = max(res, r-l)
        return res
    
# slightly optimized
class Solution_TLE:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        
        res = 0
        for m in range(1, n+1):
            window = defaultdict(int)
            cnt = l = r = 0
            while r < n:
                window[s[r]] += 1
                if window[s[r]] == k:
                    cnt += 1
                r += 1

                while l < r and len(window) > m:
                    window[s[l]] -= 1
                    if window[s[l]] == k-1:
                        cnt -= 1
                    if window[s[l]] == 0:
                        del window[s[l]]
                    l += 1
                
                if cnt == len(window): # 代表window內的m個字母都至少有k個
                    res = max(res, r-l)
        return res
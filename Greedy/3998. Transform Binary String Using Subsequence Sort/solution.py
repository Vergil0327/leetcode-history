"""
操作的數學本質
對二元字串的任意子序列排序時，子序列中的 '0' 會被移到前面，'1' 會被移到後面。

- 不變量：字串中 '1' 的總數量永遠不會改變。
- 單調性：'1' 只能向右移動（或留在原地），絕不可能向左移動。因此，對於字串的任意前綴，前綴中 '1' 的數量在經過任意次操作後只可能減少或保持不變，絕不可能增加。

字串 $s$ 能夠經過若干次操作轉換為字串 $t$，當且僅當滿足以下兩個條件：
1. 總數相等：$t$ 中 '1' 的總數量等於 $s$ 中 '1' 的總數量。
2. 前綴上界：對於每個長度為 $k$ 的前綴（$1 \le k \le n$），$t$ 前綴中 '1' 的數量 $\le$ $s$ 前綴中 '1' 的數量。

貪心策略處理 
strs[i] 中的 '?'對於含有 '?' 的目標字串模式 $p$：
- 設 $s$ 中有 $C_1(s)$ 個 '1'。
- 設 $p$ 中固定的 '1' 有 $c_1$ 個，'?' 有 $c_?$ 個。
- 若 $c_1 > C_1(s)$ 或 $c_1 + c_? < C_1(s)$，則無法構建出 '1' 的總數剛好為 $C_1(s)$ 的字串，直接回傳 False。
- 否則，我們必須將恰好 $rem = C_1(s) - c_1$ 個 '?' 替換為 '1'，其餘的 '?' 替換為 '0'。
- 貪心選擇：為了盡可能滿足「所有前綴中 '1' 的數量不超過 $s$」的限制，我們必須盡量將 '1' 放得越靠右越好。因此，我們應該將最後 $rem$ 個 '?' 填入 '1'，之前的 '?' 通通填入 '0'。
"""
class Solution:
    def transformStr(self, s: str, strs: list[str]) -> list[bool]:
        n = len(s)
        c1_s = s.count('1')
        
        # 預先計算 s 的前綴 '1' 數量
        pref_s = [0] * n
        running_sum = 0
        for i, ch in enumerate(s):
            if ch == '1':
                running_sum += 1
            pref_s[i] = running_sum
            
        ans = []
        for p in strs:
            c1_p = p.count('1')
            cq_p = p.count('?')
            
            # 若 '1' 的總數無法符合，直接為 False
            if c1_p > c1_s or c1_p + cq_p < c1_s:
                ans.append(False)
                continue
                
            rem = c1_s - c1_p
            # 最後 rem 個 '?' 變成 '1'，相當於前 (cq_p - rem) 個 '?' 變成 '0'
            threshold = cq_p - rem
            
            cur_ones = 0
            cur_q = 0
            possible = True
            
            for i, ch in enumerate(p):
                if ch == '1':
                    cur_ones += 1
                elif ch == '?':
                    cur_q += 1
                    
                # 當前前綴中，被轉換成 '1' 的 '?' 數量
                q_ones = cur_q - threshold if cur_q > threshold else 0
                
                # 檢查前綴條件：t 的前綴 '1' 數量不能超過 s
                if cur_ones + q_ones > pref_s[i]:
                    possible = False
                    break
                    
            ans.append(possible)
            
        return ans
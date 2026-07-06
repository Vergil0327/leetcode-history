class Solution:
    """
    由於我們被允許最多修改 s 中的一個字元，我們可以將問題拆解：
    如果我們決定將 s[i] 修改成某個合法的字元使其能與 t 中的某個字元匹配，那麼：

    s 中 s[i] 左邊的子字串 s[0 ... i-1] 必須能夠在 t 的前半段無修改地匹配成功。

    s 中 s[i] 右邊的子字串 s[i+1 ... len(s)-1] 必須能夠在 t 的後半段無修改地匹配成功。

    為了有效率地找出每個位置的邊界，我們可以預處理出兩個陣列：

    left[i]：代表 s[0 ... i] 在 t 中由左向右貪心匹配時，所能達到的最早（最小）結束索引。

    right[i]：代表 s[i ... len(s)-1] 在 t 中由右向左貪心匹配時，所能達到的最晚（最大）起始索引。

    預處理完成後，我們遍歷 s 的每一個位置 i，假設我們要修改 s[i]：

    左邊匹配截止於 L = left[i-1]

    右邊匹配起始於 R = right[i+1]

    只要 R - L > 1，就代表 t 在索引 L 和 R 之間至少還有一個閒置的字元，我們完全可以把 s[i] 修改成該字元來串聯起整條路徑！
    """
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        
        # 如果 s 比 t 還長，不論怎麼修改單一字元，長度都不可能塞進 t 當子序列
        if m > n: return False
            
        # left[i] 記錄 s[0...i] 在 t 中由左往右匹配的最早截止位置
        left = [float('inf')] * m
        p = 0
        for i in range(m):
            while p < n and t[p] != s[i]:
                p += 1
            if p < n:
                left[i] = p
                p += 1
            else:
                break
                
        # 如果原本就已經是子序列（不需要任何修改），直接回傳 True
        if left[-1] < n:
            return True
            
        # right[i] 記錄 s[i...] 在 t 中由右往左匹配的最晚起始位置
        right = [float('-inf')] * m
        p = n - 1
        for i in range(m - 1, -1, -1):
            while p >= 0 and t[p] != s[i]:
                p -= 1
            if p >= 0:
                right[i] = p
                p -= 1
            else:
                break
                
        # 枚舉修改 s[i] 的可能性
        for i in range(m):
            L = left[i - 1] if i > 0 else -1
            R = right[i + 1] if i < m - 1 else n
            
            # 只要左右邊界合法，且中間至少留有一個空位給修改後的 s[i]
            if L != float('inf') and R != float('-inf') and R - L > 1:
                return True
                
        return False
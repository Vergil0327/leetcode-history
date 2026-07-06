class Solution:
    """
    當我們由左向右處理字串時，在位置 i 的操作有可能會直接影響到下一個位置 i + 1 的值。具體來說，當我們使用 操作 2（將相鄰的兩個 1 變成 0）時，它會迫使下一格的值變成 0。

    因此，當我們推進到位置 i 時，s1[i] 的狀態只會受到前一格 i - 1 是否對其施加了操作 2 的影響。我們可以設計一個長度為 2 的 DP 狀態陣列：

    dp[0]：處理完當前位置且讓 s1[i] 成功匹配 s2[i] 後，沒有對下一格 i + 1 施加操作 2 的最小代價。

    dp[1]：處理完當前位置且讓 s1[i] 成功匹配 s2[i] 後，有對下一格 i + 1 施加操作 2 的最小代價（這會讓 s1[i + 1] 被強制洗成 0）。

    ⚙️ 狀態轉移規則
    對於每個位置 i，其當前的實際值 cur_v 取決於前一格傳過來的狀態：

    如果前一格有施加操作 2（c = 1），則 cur_v = 0。

    如果前一格沒有施加操作 2（c = 0），則 cur_v = int(s1[i])。

    隨後我們嘗試匹配目標值 t = int(s2[i])，這衍生出兩種選擇：

    不對 (i, i + 1) 使用操作 2：

    若 t == 1：如果 cur_v == 0，需付費 1 次操作 1；若 cur_v == 1 則不需花費。

    若 t == 0：只有在 cur_v == 0 時才合法（花費 0）；若 cur_v == 1 則此路不通。

    對 (i, i + 1) 使用操作 2：

    我們必須先把 s1[i] 和 s1[i + 1] 都準備成 1。

    準備 s1[i] 的花費：1 if cur_v == 0 else 0

    準備 s1[i + 1] 的花費：1 if s1[i + 1] == '0' else 0

    加上執行操作 2 的花費 1。

    關鍵盲點：如果目標 t == 1，由於操作 2 會把 s1[i] 歸零，我們必須在操作 2 結束後額外追加 1 次操作 1 把 s1[i] 翻回 1。
    """
    def minOperations(self, s1: str, s2: str) -> int:
        n = len(s1)
        
        # 特判 n == 1 的情況（因為無法使用操作 2）
        if n == 1:
            if s1[0] == s2[0]: return 0
            if s1[0] == '0' and s2[0] == '1': return 1
            return -1
        
        # dp[0]: next_carried = 0, dp[1]: next_carried = 1
        dp = [0, float('inf')]
        
        for i in range(n - 1):
            next_dp = [float('inf'), float('inf')]
            
            # c 代表從上一格傳過來的影響 (0 或 1)
            for c in range(2):
                if dp[c] == float('inf'): continue
                
                # 算出當前位置受前一格影響後的實際數值
                cur_v = 0 if c == 1 else int(s1[i])
                t = int(s2[i])
                
                # 選擇 1: 不對 (i, i + 1) 使用操作 2 -> 下一格不受影響 (next_carried = 0)
                if t == 1:
                    cost = 0 if cur_v == 1 else 1
                    if dp[c] + cost < next_dp[0]:
                        next_dp[0] = dp[c] + cost
                elif t == 0:
                    if cur_v == 0:
                        if dp[c] < next_dp[0]:
                            next_dp[0] = dp[c]
                            
                # 選擇 2: 對 (i, i + 1) 使用操作 2 -> 下一格被洗成 0 (next_carried = 1)
                cost_i = 1 if cur_v == 0 else 0
                cost_i1 = 1 if s1[i + 1] == '0' else 0
                op2_cost = 1
                post_cost = 1 if t == 1 else 0  # 如果目標是 1，用完操作 2 後必須再補變回 1
                
                total_op2 = cost_i + cost_i1 + op2_cost + post_cost
                if dp[c] + total_op2 < next_dp[1]:
                    next_dp[1] = dp[c] + total_op2
                    
            dp = next_dp
            
        # 最後一格 (i = n - 1) 無法再發動操作 2，做結尾統計
        ans = float('inf')
        for c in range(2):
            if dp[c] == float('inf'):
                continue
            cur_v = 0 if c == 1 else int(s1[n - 1])
            t = int(s2[n - 1])
            
            if t == 1:
                cost = 0 if cur_v == 1 else 1
                if dp[c] + cost < ans:
                    ans = dp[c] + cost
            elif t == 0:
                if cur_v == 0:
                    if dp[c] < ans:
                        ans = dp[c]
                        
        return ans if ans != float('inf') else -1
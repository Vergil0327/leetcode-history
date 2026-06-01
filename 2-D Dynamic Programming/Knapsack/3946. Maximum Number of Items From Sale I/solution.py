class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        # ==========================================
        # 步驟 1：完全背包預處理（純加購，每件收益為 1）
        # pure_knap[b] 表示用預算 b 自由加購，最多可獲得幾件商品
        # ==========================================
        pure_knap = [0] * (budget + 1)
        for factor, price in items:
            for b in range(price, budget + 1):
                pure_knap[b] = max(pure_knap[b], pure_knap[b - price] + 1)
                
        # ==========================================
        # 步驟 2：計算每個商品「買第一件」時的真正總件數收益
        # gain[i] = 1 (自己) + 所有能被 factor_i 整除的商品數量
        # ==========================================
        gain = [1] * n
        for i in range(n):
            fac_i = items[i][0]
            for j in range(n):
                if i == j:
                    continue
                fac_j = items[j][0]
                # 如果 factor_i 可以整除 factor_j，代表買 i 會免費送 j
                if fac_j % fac_i == 0:
                    gain[i] += 1
                    
        # ==========================================
        # 步驟 3：0/1 背包，決定哪些商品要買「第一件」
        # dp[b] 表示花費預算 b 在第一件商品購買上，最多獲得的總件數
        # ==========================================
        dp = [float('-inf')] * (budget + 1)
        dp[0] = 0 # 基礎狀態：不買任何商品的第一件，花費 0，獲得 0
        
        for i in range(n):
            price = items[i][1]
            g = gain[i]
            # 0/1 背包，必須從大到小逆序遍歷預算
            for b in range(budget, price - 1, -1):
                if dp[b - price] != float('-inf'):
                    dp[b] = max(dp[b], dp[b - price] + g)
                    
        # ==========================================
        # 步驟 4：窮舉分配給「第一件」的預算，結合「自由加購」
        # ==========================================
        max_total_items = 0
        for b in range(budget + 1):
            if dp[b] != float('-inf'):
                # 總收益 = 買第一件得到的件數 + 剩餘預算拿去純加購的件數
                total = dp[b] + pure_knap[budget - b]
                if total > max_total_items:
                    max_total_items = total
                    
        return max_total_items
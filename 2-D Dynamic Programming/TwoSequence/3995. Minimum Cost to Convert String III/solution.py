from functools import cache

class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        
        # 1. 預處理規則：將開銷加上 '*' 的數量，預先算好真實 Cost
        processed_rules = []
        for (pattern, replacement), base_cost in zip(rules, costs):
            total_cost = base_cost + pattern.count('*')
            processed_rules.append((pattern, replacement, len(pattern), total_cost))

        @cache
        def dfs(i: int) -> float:
            # 基底條件：已成功匹配完整個字串
            if i == n: return 0
            
            res = float('inf')
            
            # 選擇 1：若當前字元相同，可不套用任何規則，直接前進 1 位 (Cost = 0)
            if source[i] == target[i]:
                res = min(res, dfs(i + 1))
                
            # 選擇 2：嘗試在位置 i 套用每一條合法的規則
            for pattern, replacement, m, total_cost in processed_rules:
                if i + m <= n:
                    # 檢查 replacement 是否與 target[i : i + m] 完全吻合
                    if target[i : i + m] == replacement:
                        # 檢查 pattern 是否與 source[i : i + m] 匹配 (考慮通配符 '*')
                        match = True
                        for j in range(m):
                            if pattern[j] != '*' and pattern[j] != source[i + j]:
                                match = False
                                break
                        
                        # 匹配成功，嘗試狀態轉移
                        if match:
                            res = min(res, dfs(i + m) + total_cost)
                            
            return res

        ans = dfs(0)
        return int(ans) if ans < float('inf') else -1
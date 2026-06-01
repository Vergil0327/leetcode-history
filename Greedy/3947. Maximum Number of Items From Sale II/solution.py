from typing import List
from collections import Counter
from collections import defaultdict

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        
        # ====================================================
        # 步驟 1: 計算每個 factor 的 gain (一對一配對的上限)
        # ====================================================
        max_factor = max(item[0] for item in items)
        factor_counts = Counter(item[0] for item in items)
        
        factor_gain = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if factor_counts[f] == 0:
                continue
            for multiple in range(f, max_factor + 1, f):
                factor_gain[f] += factor_counts[multiple]
            factor_gain[f] -= 1
            
        # ====================================================
        # 步驟 2: 找出全域最低價，並將商品依價格從小到大排序
        # ====================================================
        min_price = min(item[1] for item in items)
        items.sort(key=lambda x: x[1])
        
        total_items = 0
        current_budget = budget
        
        # ====================================================
        # 步驟 3: 第一輪——評估每種商品「價值 2」的限量配額
        # ====================================================
        for factor, price in items:
            g = factor_gain[factor]
            if g == 0:
                continue
                
            # 計算當前預算下，這商品最多能買幾件「價值 2」的複本
            max_can_buy = current_budget // price
            actual_copies = min(g, max_can_buy)
            
            if actual_copies == 0:
                continue
                
            # 方案 A: 買這商品的超值方案
            cost_for_this = actual_copies * price
            items_from_this = actual_copies * 2
            
            # 方案 B: 把相同的錢留著，留到最後去無腦加購最低價商品
            items_from_min_price = cost_for_this // min_price
            
            # 💡 終極 PK 條件：只有當超值方案得到的件數「嚴格大於」無腦加購時，才出手！
            # 如果兩者相等，因為最低價商品可能在後續還能跟其他剩餘預算湊出更完美的除法整除，
            # 或是我們希望保留預算彈性，因此「唯有嚴格大於」才值得放棄預算彈性。
            if items_from_this > items_from_min_price:
                current_budget -= cost_for_this
                total_items += items_from_this
                
        # ====================================================
        # 步驟 4: 第二輪——剩餘的預算，全部砸在全宇宙最便宜的商品上 (價值 1)
        # ====================================================
        if current_budget > 0:
            total_items += current_budget // min_price
            
        return total_items

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        if not items or budget <= 0:
            return 0
            
        # 1. Find the global minimum price item
        min_price = min(price for _, price in items)
        
        # 2. Group items by factor to compute limits efficiently
        factor_map = defaultdict(list)
        for factor, price in items:
            factor_map[factor].append(price)
            
        unique_factors = list(factor_map.keys())
        
        total_multiples_count = defaultdict(int)
        for f1 in unique_factors:
            for f2 in unique_factors:
                if f2 % f1 == 0:
                    total_multiples_count[f1] += len(factor_map[f2])

        # 3. Collect valid deals
        valid_items = []
        for f, prices in factor_map.items():
            c_i = total_multiples_count[f] - 1
            if c_i <= 0:
                continue
            for price in prices:
                if price < 2 * min_price:
                    value = 2 * min_price - price
                    valid_items.append((price, value, c_i))
                    
        # 4. Sort items by price ascending (cheapest items dominate completely)
        valid_items.sort(key=lambda x: x[0])
        
        total_value = 0
        remaining_budget = budget
        
        # 5. Pure Greedy accumulation
        for price, value, count in valid_items:
            if remaining_budget <= 0:
                break
                
            # Determine how many copies we can afford vs how many are available
            max_affordable = remaining_budget // price
            take = min(max_affordable, count)
            
            total_value += take * value
            remaining_budget -= take * price
            
        # 6. Apply final optimal items formula
        return (budget + total_value) // min_price
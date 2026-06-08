from typing import List

# Greedy
class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(nums)
        total_score = 0
        
        i = 0
        while i < n:
            if s[i] == '0':
                i += 1
                continue
            
            # 記錄連續 '1' 區塊的起點
            block_start = i
            current_sum = 0
            min_val = float('inf')
            
            # 收集所有連續的 '1'
            while i < n and s[i] == '1':
                current_sum += nums[i]
                min_val = min(min_val, nums[i])
                i += 1
                
            # 檢查這個區塊左邊有沒有 '0' 可以讓代幣移過去
            if block_start > 0:
                # 左邊有 '0'，把左邊這個位置也納入此區塊的爭奪範圍
                left_idx = block_start - 1
                current_sum += nums[left_idx]
                min_val = min(min_val, nums[left_idx])
                
                # 總位置數為 k + 1，代幣只有 k 個，必須放棄一個最小值
                total_score += (current_sum - min_val)
            else:
                # 左邊沒位置了 (block_start == 0)，代幣只能留在原地往右排滿
                # 總位置數為 k，代幣也有 k 個，全部都能覆蓋，不需扣除任何值！
                total_score += current_sum
                
        return total_score
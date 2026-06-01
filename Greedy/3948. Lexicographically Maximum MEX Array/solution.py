from collections import Counter
from typing import List

class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # 1. 統計全域中每個數字的出現次數
        total_count = Counter(nums)
        
        result = []
        i = 0
        target_mex = 0
        
        while i < n:
            # 💡 每次要切新片段時，先在原地動態找出目前剩餘數字中，真正能達到的最大 MEX 天花板
            # 這裡的 target_mex 指針只會往上走，在整趟外層迴圈中最多增加 N 次，所以是 O(N)
            while total_count[target_mex] > 0:
                target_mex += 1
                
            # 狀況 A：如果天花板是 0 (代表接下來沒 0 了)，貪心切長度 1
            if target_mex == 0:
                result.append(0)
                total_count[nums[i]] -= 1
                i += 1
                continue
                
            # 狀況 B：天花板大於 0，開始用內層指針 j 尋找最短能湊齊這個 target_mex 的前綴
            window_set = set()
            current_mex = 0
            while i < n:
                val = nums[i]
                window_set.add(val)
                total_count[val] -= 1
                
                # 更新目前視窗內湊出來的 mex
                while current_mex in window_set:
                    current_mex += 1
                    
                i += 1

                # 一旦湊到了目標天花板，這段就是最短的完美切片，立刻中斷
                if current_mex == target_mex:
                    break
                
            # 將這個最高分寫入結果
            result.append(target_mex)
            
            # 💡 重置下一輪的天花板起點：
            # 因為剛才在 [i 到 j] 的切片中，某些數字的總總頻率可能被歸零了，
            # 下一輪的天花板絕對不可能比「剛剛被歸零的最小數字」還要大。
            # 為了保證效率，我們把 target_mex 重置為 0，讓它在下一輪開頭重新拉高到極限。
            # （由於總頻率只減不增，這不會影響 O(N) 的效能）
            target_mex = 0
            
        return result
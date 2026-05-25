from typing import List

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # 初始值設為負無窮大，以支援全負數矩陣
        ans = float('-inf')
        
        # =========================================================
        # 1. 處理 Hint 2：剛好只有 1 個共享格子的情況
        # 官方規定：這單一格子絕對不能在第一行/最後一行/第一列/最後一列
        # =========================================================
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                ans = max(ans, grid[i][j])
                
        # =========================================================
        # 2. 處理 Hint 4：微調版 Kadane 演算法（強制長度 >= 2，支援負數）
        # 檢查所有行 (Rows)
        # =========================================================
        for i in range(m):
            if n < 2:
                continue
            # 建立標準一維不歸零 Kadane
            # single_end_here 紀錄以 j 結尾的「任意長度（包含長度1）」最大子陣列和
            single_end_here = grid[i][0]
            
            for j in range(1, n):
                # 強制長度 >= 2 的核心：前一格的最優任意長度 + 當前這一格
                current_len_ge_2 = single_end_here + grid[i][j]
                ans = max(ans, current_len_ge_2)
                
                # 更新單格結尾的最優解（要嘛自己獨立一格，要嘛接續前人）
                single_end_here = max(grid[i][j], single_end_here + grid[i][j])

        # =========================================================
        # 3. 檢查所有列 (Columns)，邏輯與行完全相同
        # =========================================================
        for j in range(n):
            if m < 2:
                continue
            single_end_here = grid[0][j]
            
            for i in range(1, m):
                current_len_ge_2 = single_end_here + grid[i][j]
                ans = max(ans, current_len_ge_2)
                
                single_end_here = max(grid[i][j], single_end_here + grid[i][j])
                
        return ans
class Solution:
    """
    這道題的核心突破口在於一個非常關鍵的提示：陣列中的所有元素皆為正數（1 <= nums[i] <= 10^9）。
    
    因為所有元素都是正數，當我們固定任一中心點時，將迴文子陣列向外擴展得愈長，其總和就絕對愈大。因此，我們不需要考慮短的迴文，只需要找出以每個位置為中心的最長迴文子陣列，並透過前綴和（Prefix Sum）算出它的各別總和，最後取全域最大值即可。
    要高效地在 $O(N)$ 時間內找到所有中心點的最長迴文，最完美的工具就是 Manacher 演算法
    """
    def getSum(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. 建立前綴和陣列，以便在 O(1) 時間內計算任何子陣列的和
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        # 2. 預處理陣列以統一處理奇數長度與偶數長度的迴文 (插空填入 -1)
        # 為了防止越界，開頭與結尾加上不同的哨兵值 (-2 與 -3)
        A = [-2]
        for x in nums:
            A.append(-1)
            A.append(x)
        A.append(-1)
        A.append(-3)
        
        n_A = len(A)
        P = [0] * n_A  # P[i] 紀錄以 A[i] 為中心的最長迴文半徑
        C = 0          # 當前最大迴文的中心點
        R = 0          # 當前最大迴文的右邊界
        
        max_sum = 0
        
        # 3. 執行標準 Manacher 演算法
        for i in range(1, n_A - 1):
            i_mirror = 2 * C - i
            
            if R > i:
                P[i] = min(R - i, P[i_mirror])
            else:
                P[i] = 0
                
            # 嘗試向外擴展
            while A[i + 1 + P[i]] == A[i - 1 - P[i]]:
                P[i] += 1
                
            # 如果目前擴展的迴文超出了舊的右邊界，更新中心與右邊界
            if i + P[i] > R:
                C = i
                R = i + P[i]
                
            # 4. 將 A 陣列中的迴文邊界映射回原始 nums 陣列
            # 迴文在 A 中的範圍是 [i - P[i] + 1, i + P[i] - 1]
            start_A = i - P[i] + 1
            end_A = i + P[i] - 1
            
            # 我們只關心 A 中真正屬於 nums 的元素（其索引在 A 中必為偶數）
            if start_A % 2 != 0: start_A += 1
            if end_A % 2 != 0: end_A -= 1
            
            if start_A <= end_A:
                # 換算回 nums 的真實索引 l 與 r
                l = (start_A - 2) // 2
                r = (end_A - 2) // 2
                
                # 利用前綴和 O(1) 算出該迴文子陣列的總和
                current_sum = pref[r + 1] - pref[l]
                if current_sum > max_sum:
                    max_sum = current_sum
                    
        return max_sum
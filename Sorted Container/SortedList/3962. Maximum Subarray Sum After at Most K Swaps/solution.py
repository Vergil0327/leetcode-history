"""
核心原理解析:

傳統的做法是固定子陣列 $[i, j]$ 後，試圖去找出內部最小的 $t$ 個和外部最大的 $t$ 個進行交換。這種「一進一出」的動態維護在 Python 中很容易因為常數過大而超時。
而該解法提出了一個顛覆性的視角：假設當前子陣列的長度為 $L = j - i + 1$。原本的交換公式是：

    $$\text{新子陣列和} = \text{原內部元素和} - \sum(\text{內部最小的 } t \text{ 個}) + \sum(\text{外部最大的 } t \text{ 個})$$

這等價於：
    $$\text{新子陣列和} = \sum(\text{內部最大的 } L - t \text{ 個}) + \sum(\text{外部最大的 } t \text{ 個})$$

這就意味著：我們本質上只是要在「全域所有元素」中，挑選出剛好 $L$ 個元素，使得其中來自外部的元素不能超過 $k$ 個，並讓這 $L$ 個元素的總和最大！

基於這個結論，對於任何一個長度為 $L$ 的子陣列，最優選擇只有以下兩種情況：

1. 全域貪心無約束（Case 1）
如果我們什麼都不管，挑選整個陣列中最大的前 $L$ 個元素。統計這 $L$ 個元素中，有多少個元素的原始位置是在子陣列外部。

- 如果外部元素的數量 $\le k$，說明這是一個完全合法的交換方案（完全在 $k$ 次交換許可內）。
- 此時，該子陣列的最大可能和，就直接等於全域前 $L$ 大元素的總和！這可以用前綴和在 $O(1)$ 內得到。

2. 邊界約束受限（Case 2）
如果全域前 $L$ 大元素中，屬於外部的元素數量 $> k$，說明我們沒有足夠的交換次數去拿這麼多外部好處。因為效益函數具有凹函數（Concave）的單調性，最優解必然死死卡在邊界上：

- 我們強行拿滿外部最大的 $k$ 個元素。
- 剩下的 $L - k$ 個名額，全部拿內部最大的 $k$ 個元素。
- 此時，最大可能和 = $\sum(\text{外部最大 } k \text{ 個}) + \sum(\text{內部最大 } L - k \text{ 個})$。

如何優化到 $O(N^2 \log N)$？

利用 sortedcontainers 庫中的 SortedList，我們可以動態地在 $O(\log N)$ 內維護內部集合（$I$）和外部集合（$O$）。當右端點 $j$ 往右移動時：

1. nums[j] 從外部集合移入內部集合（$O(1)$ 次 SortedList 操作）。
2. 我們可以用 $O(1)$ 的時間動態更新「全域前 $L$ 大元素中有多少個在內部/外部」。
3. 同時動態維護外部前 $k$ 大之和、以及內部前 $L-k$ 大之和。
"""

from sortedcontainers import SortedList

class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = float('-inf')
        k = min(k, n)
        
        # 特判 k = 0 的情況：標準的 Kadane's Algorithm，極速 O(N) 一趟過
        if k == 0:
            cur_max = float('-inf')
            run_sum = 0
            for x in nums:
                run_sum += x
                if run_sum > cur_max: cur_max = run_sum
                if run_sum < 0: run_sum = 0
            return max(nums) if cur_max == 0 else cur_max

        # 1. 全局排序與排名預處理 (由大到小排序)
        sorted_with_idx = sorted(range(n), key=lambda x: nums[x], reverse=True)
        sorted_nums = [nums[idx] for idx in sorted_with_idx]
        
        # 全局前綴和，用於 Case 1 的 O(1) 查詢
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + sorted_nums[i]
            
        # rank[idx] 儲存 nums[idx] 在全局由大到小排序後的排名
        rank = [0] * n
        for r, idx in enumerate(sorted_with_idx):
            rank[idx] = r

        # 外層枚舉左端點 i
        for i in range(n):
            # 初始化動態平衡容器
            O_large = SortedList()  # 維護外部最大的至多 k 個元素
            O_small = SortedList(nums)
            O_large_sum = 0
            
            I_large = SortedList()  # 維護內部最大的至多 (L - k) 個元素
            I_small = SortedList()
            I_large_sum = 0
            
            # 初始狀態：子陣列為空，所有元素都在外部，將 O_large 填滿前 k 大
            while len(O_large) < k and O_small:
                best = O_small.pop() # SortedList 預設升序，pop() 彈出最大值
                O_large.add(best)
                O_large_sum += best
                
            in_top_L = 0 # 記錄全局前 L 大元素中，落入當前內部 [i, j] 的數量
            
            # 內層枚舉右端點 j
            for j in range(i, n):
                val = nums[j]
                L = j - i + 1
                
                # ------ 步驟 A: 將 nums[j] 從外部動態移出 ------
                if len(O_large) > 0 and val >= O_large[0]:
                    if val in O_large:
                        O_large.remove(val)
                        O_large_sum -= val
                        if O_small:
                            promoted = O_small.pop()
                            O_large.add(promoted)
                            O_large_sum += promoted
                    else:
                        O_small.remove(val)
                else:
                    O_small.remove(val)
                
                # ------ 步驟 B: 將 nums[j] 動態移入內部 ------
                if I_large and val > I_large[0]:
                    I_large.add(val)
                    I_large_sum += val
                    demoted = I_large.pop(0) # 彈出 I_large 中最小的
                    I_large_sum -= demoted
                    I_small.add(demoted)
                else:
                    I_small.add(val)
                
                # 調整內部 I_large 的窗口大小至剛好符合 max(0, L - k)
                target_I_size = max(0, L - k)
                if len(I_large) < target_I_size and I_small:
                    promoted = I_small.pop()
                    I_large.add(promoted)
                    I_large_sum += promoted
                    
                # ------ 步驟 C: O(1) 更新全局前 L 大元素落在內部的數量 ------
                # 點 1: 新納入內部的 nums[j] 是否屬於新的全局前 L 大？ (排名為 0 ~ L-1)
                if rank[j] < L: 
                    in_top_L += 1

                # 點 2: 全局前 L 大的窗口此時向右吞進了 sorted_nums[L-1]，檢查其原先是否已在內部
                orig_idx = sorted_with_idx[L - 1]
                if i <= orig_idx < j: # 這裡保持 < j，確保不與點 1 的索引 j 衝突
                    in_top_L += 1
                
                # ------ 步驟 D: 依據 Case 1 / Case 2 理論直接計算答案 ------
                c = L - in_top_L # 挑選的全局前 L 大中，有多少個目前在外部
                
                if c <= k:
                    current_subarray_max = pref_sum[L]
                else:
                    current_subarray_max = O_large_sum + I_large_sum
                    
                if current_subarray_max > ans:
                    ans = current_subarray_max
                    
        return ans
"""
核心思維與離散化

狀態轉換(Grouping)：根據題目條件，我們可以將 nums 中的每個元素分類為三組：
- 小於 $a$ 的元素：標記為 0
- 介於 $[a, b]$ 之間的元素：標記為 1
- 大於 $b$ 的元素：標記為 2

問題等價轉換（Sorting & Inversions）：
要讓陣列成為「Good Array」，目標就是把陣列排成非遞減的順序（所有的 0 在最前面，接著是所有的 1，最後是所有的 2）。
透過相鄰交換（Adjacent Swaps）將陣列排序所需的最少交換次數，正好等於該陣列中的「逆序對（Inversion Count）」數量。

$O(N)$ 極速統計逆序

對：因為陣列元素只有 0、1、2 三種，我們不需要使用樹狀陣列（BIT）或分治法（Merge Sort），只需在由左向右掃描時，用三個變數記錄目前出現過的 0、1、2 個數：當遇到 0 時：它與先前出現過的所有 1 和 2 都構成逆序對（交換次數 $+ cnt1 + cnt2$）。當遇到 1 時：它只與先前出現過的所有 2 構成逆序對（交換次數 $+ cnt2$）。當遇到 2 時：它比前面的 0 和 1 都大，不產生逆序對。
"""
class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        MOD = 10**9 + 7
        cnt0 = cnt1 = cnt2 = 0
        ans = 0
        
        for x in nums:
            if x < a:
                # 遇到 0，會與前面所有的 1 和 2 形成逆序對
                ans = (ans + cnt1 + cnt2) % MOD
                cnt0 += 1
            elif x <= b:
                # 遇到 1，會與前面所有的 2 形成逆序對
                ans = (ans + cnt2) % MOD
                cnt1 += 1
            else:
                # 遇到 2，前面沒有比它大的數，不增加逆序對
                cnt2 += 1
                
        return ans
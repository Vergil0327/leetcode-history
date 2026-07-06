import math

class Solution:
    """
    如果你盲目地去檢查所有可能的 $k$，由於 $k$ 最大可達 $10^6$，外層循環配上內層 $O(N)$ 的 Kadane 演算法，總計算量會高達 $10^9$ 導致 TLE。因此，這題需要一個關鍵的數學降維觀察。

    核心數學剪枝：為什麼我們只需要檢查「質數」與 $2$？

    假設我們選擇了一個合數 $k$（例如 $k = 6$），它有一個質因數 $a = 2$。
    我們來比較 $k=6$ 與 $a=2$ 對於陣列元素的轉換影響：

    - 如果某個元素能被 $6$ 整除，它一定也能被 $2$ 整除（轉換後維持 $+nums[i]$）。
    - 如果某個元素不能被 $6$ 整除，它有可能可以被 $2$ 整除（轉換後從 $-nums[i]$ 變成 $+nums[i]$）。

    這意味著：當我們把 $k$ 縮小到它的質因數 $a$ 時，轉換後的陣列在每一個位置上的數值都「大於或等於」原先 $k$ 的陣列。

    根據 Kadane's Algorithm 的特性，當陣列中的每個元素都變大或不變時，算出來的「最大子陣列和」也必然會大於或等於原先的結果。再者，題目要求當分數相同時，優先選擇較小的 $k$。既然質因數 $a$ 算出來的分數更高（或相等），且 $a < k$（更小），合數 $k$ 就永遠不可能打敗它的質因數。

    因此，我們的候選人名單只需要包含：

    1. $k = 2$：作為全域最小的基準（用來應付所有元素都是奇數，或沒有任何數能被選中時的墊底情況）。
    2. nums 中所有元素的所有「質因數」。

    一個不大於 $10^6$ 的數字，最多只會有 $7$ 個不同的質因數（因為 $2 \times 3 \times 5 \times 7 \times 11 \times 13 \times 17 > 10^6$）。在 $N = 1000$ 的限制下，全域不重複的質因數最多只有幾千個，這讓總計算量直接暴降到可輕鬆通過的級別！
    """
    def divisibleGame(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        
        # 1. 收集所有候選的 k：預設包含 2，並加上所有元素的所有質因數
        primes = {2}
        for x in nums:
            temp = x
            d = 2
            # 經典 $O(\sqrt{X})$ 質因數分解
            while d * d <= temp:
                if temp % d == 0:
                    primes.add(d)
                    while temp % d == 0:
                        temp //= d
                d += 1
            if temp > 1:
                primes.add(temp)
        
        max_score = -math.inf
        best_k = None
        
        # 2. 將候選人由小到大排序，這樣遇到分數相同（Tie）時，自然會保留最小的 k
        for k in sorted(primes):
            current_max = -math.inf
            current_sum = 0
            
            # 標準 Kadane's Algorithm
            for x in nums:
                # 根據是否能被 k 整除進行數值轉換
                val = x if x % k == 0 else -x
                current_sum += val
                
                if current_sum > current_max:
                    current_max = current_sum
                    
                # 如果目前累積和小於 0，及時斷尾求生
                if current_sum < 0:
                    current_sum = 0
            
            # 嚴格大於才更新，完美符合「分數最大優先；分數相同時，k 最小優先」
            if current_max > max_score:
                max_score = current_max
                best_k = k
                
        # 3. 依題目要求回傳 (最大得分差 * 最優 k) % (10^9 + 7)
        # Python 的 % 運算子原生支援負數的數學取模（例如 -2 % 7 = 5），非常安全
        return (max_score * best_k) % MOD
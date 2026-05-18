"""
這道題目可以使用 二分搜尋法 (Binary Search) 搭配 滾動雜湊 (Rolling Hash / Rabin-Karp) 來達成最佳的時間複雜度。

解題觀念與單調性 (Monotonicity)如果存在一個長度為 len 的唯一子陣列（只出現過一次），那麼只要把這個子陣列兩端再隨便擴充、增長，產生的長度為 len + 1、len + 2 的子陣列必然也是唯一的。
這代表答案具備單調性，所以我們可以對子陣列的「長度」進行二分搜尋。二分搜尋的範圍為：l = 1 到 r = n。滾動雜湊 (Rolling Hash) 的實作技巧在 check(length) 函式中，我們需要檢查陣列中所有長度為 length 的子陣列，看看是否至少有一個子陣列的出現次數為 1。
因為 $N \le 10^5$，如果每次都直接複製或比對子陣列，會退化成 $O(N^2)$ 導致 TLE。

使用滾動雜湊可以讓我們在 $O(1)$ 的時間內算出下一個滑動視窗的雜湊值：

1. 雜湊公式：$H = (H \times \text{base} + \text{num}) \pmod{\text{mod}}$
2. 防碰撞 (Collision)：因為單一模數（如 $10^9+7$）在強大測資下容易發生碰撞（例如 GitHub 上提到的反向補碼攻擊），最穩健的做法是採用 雙雜湊 (Double Hash)。使用兩個不同的質數作為模數，兩個雜湊值都相同才算相同。
"""
from collections import Counter
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 雙雜湊所使用的參數
        BASE1, MOD1 = 13131, 1000000007
        BASE2, MOD2 = 131313, 1000000009

        def check(length):
            # 如果長度超過陣列，不合法
            if length > n: return False
            
            # 計算最高位的權重：base^(length-1) % mod
            power1 = pow(BASE1, length - 1, MOD1)
            power2 = pow(BASE2, length - 1, MOD2)
            
            # 計算第一個視窗 (0 到 length-1) 的雜湊值
            h1, h2 = 0, 0
            for i in range(length):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2
            
            # 統計各個雜湊組合出現的次數
            hash_counts = Counter()
            hash_counts[(h1, h2)] += 1
            
            # 開始滾動滑動視窗
            for i in range(length, n):
                # 移除最左邊移出視窗的元素
                out_val = nums[i - length]
                h1 = (h1 - out_val * power1) % MOD1
                h2 = (h2 - out_val * power2) % MOD2
                
                # 加上最右邊新移入視窗的元素
                in_val = nums[i]
                h1 = (h1 * BASE1 + in_val) % MOD1
                h2 = (h2 * BASE2 + in_val) % MOD2
                
                # 修正 Python 的負數餘數
                h1 = (h1 + MOD1) % MOD1
                h2 = (h2 + MOD2) % MOD2
                
                hash_counts[(h1, h2)] += 1
            
            # 檢查是否至少有一個雜湊值只出現過 1 次
            return any(count == 1 for count in hash_counts.values())

        # 二分搜尋長度
        l, r = 1, n
        ans = n
        
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                ans = mid     # 這個長度可行，紀錄答案並嘗試尋找更短的
                r = mid - 1
            else:
                l = mid + 1   # 這個長度不行，必須更長
                
        return ans
"""
這道題目可以使用 二分搜尋法 (Binary Search) 搭配 滾動雜湊 (Rolling Hash / Rabin-Karp) 來達成最佳的時間複雜度。

解題觀念與單調性 (Monotonicity)如果存在一個長度為 len 的唯一子陣列（只出現過一次），那麼只要把這個子陣列兩端再隨便擴充、增長，產生的長度為 len + 1、len + 2 的子陣列必然也是唯一的。
這代表答案具備單調性，所以我們可以對子陣列的「長度」進行二分搜尋。二分搜尋的範圍為：l = 1 到 r = n。滾動雜湊 (Rolling Hash) 的實作技巧在 check(length) 函式中，我們需要檢查陣列中所有長度為 length 的子陣列，看看是否至少有一個子陣列的出現次數為 1。
因為 $N \le 10^5$，如果每次都直接複製或比對子陣列，會退化成 $O(N^2)$ 導致 TLE。

使用滾動雜湊可以讓我們在 $O(1)$ 的時間內算出下一個滑動視窗的雜湊值：

1. 雜湊公式：$H = (H \times \text{base} + \text{num}) \pmod{\text{mod}}$
2. 防碰撞 (Collision)：因為單一模數（如 $10^9+7$）在強大測資下容易發生碰撞（例如 GitHub 上提到的反向補碼攻擊），最穩健的做法是採用 雙雜湊 (Double Hash)。使用兩個不同的質數作為模數，兩個雜湊值都相同才算相同。

在設計滾動雜湊 (Rolling Hash) 時，選擇 BASE（進位基數）和 MOD（模數）並不是隨便填填就好，而是有一套嚴格的密碼學與數學原理。你看到的 13131 和 131313 是競賽程式（如 LeetCode、Codeforces）中非常經典的「經驗數值」。

以下為你拆解為什麼要這樣選，以及如何決定你自己的 BASE。

1. 基數 (BASE) 必須大於字元集的大小

把滾動雜湊想像成進位制（例如十進位、二進位）。
- 如果你要處理進位制，基數必須大於系統中的最大數字。例如：十進位用基數 10，裡面的數字只有 0 到 9；二進位用基數 2，數字只有 0 和 1。
- 在這題中，nums[i] 的範圍是 $1 \le \text{nums}[i] \le 10^5$。

核心規則： BASE 必須大於陣列中可能出現的最大數值（即 BASE > 100000）。
如果 BASE 小於最大值，就會發生嚴重的「低位元衝突」。例如：在基數為 10 的系統中，1 乘以 10 加上 2 是 12，但如果遇到超出範圍的符號，雜湊值就會輕易重疊。

2. 為什麼選 13131 和 131313？

這涉及了質數（Prime Number） 與雜湊分佈均勻度的考量。
原因 A：它們是質數（或偽質數）在數論中，如果 BASE 和 MOD 互質（Coprime），雜湊值在經過多次乘法與取模運算後，在空間中的分布會最均勻，最不容易擠在同一個餘數區塊。
    - 13131 雖然不是質數（$13131 = 3 \times 19 \times 231$），但它與常規的模數（如 $10^9+7$）互質。
    - 131313 也與大質數模數互質。
    - 更常見的標準大質數其實是 1313131（這是一個真質數，且大於 $10^5$）。

原因 B：順手與好記（競賽梗）在字串處理（字元集大小只有 26 或 256）的題目中，大家習慣用 131、1313、13331。這題因為數值範圍到了 $10^5$，所以程式設計師很直覺地把習慣的數字「往後延伸」變大，成了 13131 或 131313。

3. 如何正確決定你的 BASE？（實戰公式）

如果你想寫出一個絕對安全、無法被測資惡意擊破的滾動雜湊，請遵循以下步驟設定 BASE：

    1. 找出最大值： 看看題目限制的最大數值是多少（假設為 $M$）。
    2. 選擇大於 $M$ 的質數： 挑選一個大於 $M$ 的隨機質數作為 BASE。💡 
    
    
最安全萬用解：隨機質數 (Randomized Base)如果你的 BASE 在程式碼裡是固定的（例如固定寫死 13131），出題者可以故意設計一組特殊的極端測資（稱為 Anti-hash test），讓你的 App 或演算法產生雜湊碰撞而得到 Wrong Answer。

最強大的防禦方式是在執行時期（Runtime）隨機生成一個大質數：

```py
import random

# 題目最大值是 100,000，我們隨機在 100,001 到 200,000 之間挑一個質數
# 這裡用幾個確保是質數的數字讓系統隨機選
BASE_OPTIONS = [100003, 100019, 100043, 100049, 100057, 100069]
BASE1 = random.choice(BASE_OPTIONS)

```

總結

- 為什麼用 131313？因為這題數字最大到 $10^5$，131313 大於 $10^5$ 且與 MOD 互質，能像「進位制」一樣完美區隔每個數位。
- 為什麼要用兩個（13131 和 131313）？因為這叫雙雜湊 (Double Hash)。單一雜湊的碰撞機率是 $\frac{1}{\text{MOD1}}$，雙雜湊的碰撞機率降到 $\frac{1}{\text{MOD1} \times \text{MOD2}}$（幾乎等於 0），雙重保險防止被 LeetCode 刁鑽的隱藏測資卡死！
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
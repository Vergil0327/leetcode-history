from collections import deque
from typing import List

class Solution:
    """
    向左旋轉 (Rotate Left) 和 翻轉 (Reverse) 這兩種操作，無論怎麼組合，都只能產生原陣列的「循環移位 (Rotations)」或「翻轉後的循環移位」。
    也就是說，一個陣列如果能夠被排好序，它在初始狀態就必須具備特殊的結構：它要嘛是循環遞增 (Cyclically Increasing)，要嘛是循環遞減 (Cyclically Decreasing)。如果不是這兩種，直接回傳 -1。
    因此，我們可以把這個問題看作是圖論的最短路徑問題，將所有可能的陣列狀態簡化成 $2n$ 個狀態。
    
    從最終狀態返回來, 利用BFS找到轉成nums的最低步數

    我們從「已經排好序的目標陣列 $[0, 1, \dots, n-1]$」出發，定義狀態 (is_reversed, shift)：
        - is_reversed = 0：代表陣列是正向遞增的循環移位。
        - is_reversed = 1：代表陣列是反向遞減的循環移位。
        - shift：代表目標陣列向左旋轉了幾次。

    Steps:
    - Rotate Left:(0, shift) $\to$ (0, (shift + 1) % n)，成本為 1。(1, shift) $\to$ (1, (shift + 1) % n)，成本為 1。
    - Reverse:翻轉一個已經向左移位 shift 次的遞增陣列，會讓它變成一個向左移位 (n - shift) % n 次的遞減陣列。(0, shift) $\to$ (1, (n - shift) % n)，成本為 1。(1, shift) $\to$ (0, (n - shift) % n)，成本為 1。

    由於圖中所有邊的權重都是 1，且總狀態數只有 $2n$ 個（對於 $n=10^5$，狀態數僅 $2 \times 10^5$），我們可以直接從目標狀態 (0, 0) 開始跑一次 BFS，求出到所有狀態的最短步數！
    """
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
            
        # 1. BFS 計算從標準有序狀態 (0, 0) 出發到所有狀態的最短步數
        dist = [[-1] * n for _ in range(2)]
        queue = deque([(0, 0)])
        dist[0][0] = 0
        
        while queue:
            rev, shift = queue.popleft()
            d = dist[rev][shift]
            
            # 操作一：Rotate Left
            next_shift = (shift + 1) % n
            if dist[rev][next_shift] == -1:
                dist[rev][next_shift] = d + 1
                queue.append((rev, next_shift))
                
            # 操作二：Reverse
            next_rev = 1 - rev
            next_shift_rev = (n - shift) % n
            if dist[next_rev][next_shift_rev] == -1:
                dist[next_rev][next_shift_rev] = d + 1
                queue.append((next_rev, next_shift_rev))
                
        # 2. 判定目前 nums 的類型與移位量
        idx_zero = nums.index(0)
        
        # 檢查是否為正向循環遞增
        is_inc = True
        for i in range(n):
            if nums[(idx_zero + i) % n] != i:
                is_inc = False
                break
                
        if is_inc:
            # 正向遞增時，0 在 idx_zero 點，代表向左移位了 idx_zero 次
            return dist[0][idx_zero]
            
        # 檢查是否為反向循環遞減
        is_dec = True
        for i in range(n):
            if nums[(idx_zero - i + n) % n] != i:
                is_dec = False
                break
                
        if is_dec:
            # 標準反向陣列 [2, 1, 0] 的 0 在最後一個位置 (n-1)。
            # 如果 0 移到了 idx_zero，代表整體向左移動了 (n - 1 - idx_zero) 步
            target_shift = (n - 1 - idx_zero + n) % n
            return dist[1][target_shift]
            
        return -1
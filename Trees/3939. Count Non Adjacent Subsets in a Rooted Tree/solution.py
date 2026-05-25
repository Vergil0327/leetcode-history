from typing import List

class Solution:
    """
    dp0[u][r]：代表不選擇節點 $u$ 時，以 $u$ 為根的子樹中，所選節點價值總和模 $k$ 餘數為 $r$ 的組合數。
    dp1[u][r]：代表選擇節點 $u$ 時，以 $u$ 為根的子樹中，所選節點價值總和模 $k$ 餘數為 $r$ 的組合數。

    初始狀態：
    在還沒有考慮任何子節點時，子樹只有節點 $u$ 自己：如果不選 $u$：目前的價值總和是 $0$，餘數也是 $0$。所以 dp0[u][0] = 1，其餘為 $0$。
    如果選擇 $u$：目前的價值總和是 nums[u]，餘數是 nums[u] % k。所以 dp1[u][nums[u] % k] = 1，其餘為 $0$。

    如果 $u$ 被選擇了 (計算新 dp1)：
    因為相鄰節點不能同時選擇，子節點 $v$ 絕對不能被選擇。因此，$u$ 只能跟 $v$ 的 dp0[v] 進行合併：
        $$\text{next\_dp1}[(r_1 + r_2) \% k] = \sum \text{dp1}[u][r_1] \times \text{dp0}[v][r_2]$$

    如果 $u$ 沒有被選擇 (計算新 dp0)：
    因為 $u$ 沒被選，子節點 $v$ 選不選都可以。因此，$u$ 可以跟 $v$ 的 (dp0[v] + dp1[v]) 進行合併：
        $$\text{next\_dp0}[(r_1 + r_2) \% k] = \sum \text{dp0}[u][r_1] \times (\text{dp0}[v][r_2] + \text{dp1}[v][r_2])$$

    複雜度分析
    
    時間複雜度：$O(n \cdot k^2)$。樹上的每個節點 $u$ 只會跟它的子節點合併一次，每次合併需要雙重迴圈遍歷長度為 $k$ 的狀態空間，因此需要 $O(k^2)$。總共有 $n-1$ 條邊，故總時間為 $O(n \cdot k^2)$。帶入數值：$1000 \times 100^2 = 10^7$ 次運算。
    空間複雜度：$O(n \cdot k)$。主要用於儲存 $n$ 個節點的 dp0 與 dp1 陣列，以及 DFS 的遞迴系統棧空間。
    """
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        n = len(parent)
        MOD = 10**9 + 7
        
        # 1. 建立鄰接表 (樹的結構)
        graph = [[] for _ in range(n)]
        for child, p in enumerate(parent):
            if p != -1:
                graph[p].append(child)
                
        # dp0[u] 和 dp1[u] 分別儲存節點 u 不選與選的餘數組合數
        dp0 = [[0] * k for _ in range(n)]
        dp1 = [[0] * k for _ in range(n)]
        
        # 2. 進行後序遍歷 (從葉子節點往上遞迴)
        def dfs(u):
            # 初始化節點 u 自身的狀態
            dp0[u][0] = 1
            dp1[u][nums[u] % k] = 1
            
            for v in graph[u]:
                dfs(v) # 先遞迴計算子節點
                
                # 準備臨時陣列來儲存合併子節點 v 後的新狀態
                next_dp0 = [0] * k
                next_dp1 = [0] * k
                
                # 雙重迴圈列舉餘數進行背包合併
                for r1 in range(k):
                    if dp0[u][r1] == 0 and dp1[u][r1] == 0:
                        continue
                        
                    for r2 in range(k):
                        r_next = (r1 + r2) % k
                        
                        # 狀況 A: u 沒選，v 可選可不選
                        if dp0[u][r1] > 0:
                            v_choices = (dp0[v][r2] + dp1[v][r2]) % MOD
                            next_dp0[r_next] = (next_dp0[r_next] + dp0[u][r1] * v_choices) % MOD
                            
                        # 狀況 B: u 選了，v 絕對不能選 (只能用 dp0[v])
                        if dp1[u][r1] > 0:
                            next_dp1[r_next] = (next_dp1[r_next] + dp1[u][r1] * dp0[v][r2]) % MOD
                            
                # 將更新後的狀態覆蓋回 u
                dp0[u] = next_dp0
                dp1[u] = next_dp1

        # 從樹根 0 開始 DFS
        dfs(0)
        
        # 3. 根據 Hint 3 計算最終答案
        # 總和能被 k 整除代表餘數為 0
        # 記得減去「一個節點都沒選」的空集合狀況 (-1)
        ans = (dp0[0][0] + dp1[0][0] - 1) % MOD
        
        # 修正 Python 的負數餘數問題
        return (ans + MOD) % MOD
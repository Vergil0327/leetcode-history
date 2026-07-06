from functools import lru_cache

class Solution:
    """
    轉成 Top-down DP（DFS + 記憶化）在邏輯上會更直覺，因為它就像是在模擬我們「查字典選字」的過程。

    不過，如果我們要在 Top-down 中維持先前 Bottom-up 的「狀態位元（status 記錄哪邊選過）」，總狀態數會變成 $M \times N \times L \times 3 \times 4 \approx 1.2 \times 10^7$。這個狀態量對 Python 的 @cache 來說稍微有點沉重，容易導致 MLE（記憶體超限） 或遞迴過深。

    優化思維：排容原理 (Inclusion-Exclusion Principle)
    為了讓 Top-down DP 在 Python 中跑得又快又省記憶體，我們可以用數學上的排容原理把 status 這個累贅徹底拿掉：$$\text{合法總方法數} = \text{任意挑選組成 target 的方法數} - \text{只從 word1 挑選的方法數} - \text{只從 word2 挑選的方法數}$$

        $$\text{合法總方法數} = \text{任意挑選組成 target 的方法數} - \text{只從 word1 挑選的方法數} - \text{只從 word2 挑選的方法數}$$

    這樣一來，我們的主程式就退化成一個純粹的 3D DP，狀態數直接暴降到原先的四分之一（約 $3 \times 10^6$）！
    用一個 mode 來決定目前是要「從兩字串中做決策（mode=0）」、「在 word1 中往後掃描（mode=1）」還是「在 word2 中往後掃描（mode=2）」：
    """
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        mod = 10**9 + 7
        m, n, L = len(word1), len(word2), len(target)

        # =========================================================
        # 1. 主 DP：計算不論限制，利用 word1 和 word2 能組成 target 的「所有」方法數
        # mode: 0 -> 決定要在 word1 還是 word2 找 target[k]
        #       1 -> 正在 word1 中向後尋找與 target[k] 匹配的字元
        #       2 -> 正在 word2 中向後尋找與 target[k] 匹配的字元
        # =========================================================
        @lru_cache(None)
        def dfs_any(i, j, k, mode):
            if k == L: 
                return 1 if mode == 0 else 0
            
            if mode == 0:
                # 可以選擇從 word1 挑選，或者從 word2 挑選來匹配 target[k]
                return (dfs_any(i, j, k, 1) + dfs_any(i, j, k, 2)) % mod
            
            if mode == 1:
                if i == m: return 0
                # 選擇一：跳過目前的 word1[i]，繼續往後找 target[k]
                res = dfs_any(i + 1, j, k, 1)
                # 選擇二：如果字元匹配，拿它來當 target[k]，並讓 target 推進到 k+1
                if word1[i] == target[k]:
                    res += dfs_any(i + 1, j, k + 1, 0)
                return res % mod
            
            if mode == 2:
                if j == n: return 0
                # 選擇一：跳過目前的 word2[j]，繼續往後找 target[k]
                res = dfs_any(i, j + 1, k, 2)
                # 選擇二：如果字元匹配，拿它來當 target[k]，並讓 target 推進到 k+1
                if word2[j] == target[k]:
                    res += dfs_any(i, j + 1, k + 1, 0)
                return res % mod

        # =========================================================
        # 2. 輔助 DP：計算「只用 word1」能組成 target 的方法數
        # =========================================================
        @lru_cache(None)
        def dfs_only1(i, k):
            if k == L: return 1
            if i == m: return 0
            res = dfs_only1(i + 1, k)
            if word1[i] == target[k]:
                res += dfs_only1(i + 1, k + 1)
            return res % mod

        # =========================================================
        # 3. 輔助 DP：計算「只用 word2」能組成 target 的方法數
        # =========================================================
        @lru_cache(None)
        def dfs_only2(j, k):
            if k == L: return 1
            if j == n: return 0
            res = dfs_only2(j + 1, k)
            if word2[j] == target[k]:
                res += dfs_only2(j + 1, k + 1)
            return res % mod

        # 根據排容原理：全部可能的組合 - 純word1的組合 - 純word2的組合
        total_ways = dfs_any(0, 0, 0, 0)
        only_w1 = dfs_only1(0, 0)
        only_w2 = dfs_only2(0, 0)

        # avoid MLE
        dfs_any.cache_clear()
        dfs_only1.cache_clear()
        dfs_only2.cache_clear()

        return (total_ways - only_w1 - only_w2) % mod
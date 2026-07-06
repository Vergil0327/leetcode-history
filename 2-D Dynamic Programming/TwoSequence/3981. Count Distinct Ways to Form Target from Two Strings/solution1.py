"""
程式碼核心盲點
1. 貪心跳過導致「漏算重複字元」（最致命的錯誤）
在你的程式碼中，你使用了 while 迴圈來尋找下一個匹配的字元：

```Python
ii = i
while ii < m and word1[ii] != target[k]:
    ii += 1
if ii < m:
    res += dfs(ii+1, j, k+1)
```
這個寫法會讓程式只停在「第一個」匹配的字元位置。如果 word1 後面還有其他完全相同的字元也可以用來匹配 target[k]，你的程式碼會將它們徹底忽略！

舉例： 假設 word1 = "aac", word2 = "z", target = "az"。
當要匹配 target[0] = 'a' 時，word1[0] 和 word1[1] 都是合法的選擇。但你的 while 迴圈找到 word1[0] 就收工了，直接漏掉了選擇 word1[1] 的合法路徑。

2. 用索引判斷「是否用過該字串」不夠精準
你在基底條件中使用 i > 0 and j > 0 來檢查是否 word1 和 word2 都至少被選中過一次。雖然在某些情況下 index 變大代表有選，但這種與狀態高度耦合的寫法很容易在複雜邊界（例如 index 剛好是 0 的時候）產生非預期的 Bug。最安全的做法是使用明確的布林狀態位元（Status Bitmask）。


如果我們把 while 迴圈改成走訪所有匹配字元，內層會多出一個 $O(M)$ 或 $O(N)$ 的迴圈。當總狀態數為 $100 \times 100 \times 100 = 10^6$ 時，再乘上內層迴圈，總計算量會飆到 $2 \times 10^8$，在 Python 中絕對會 TLE（超時）。

為了達到真正的 $O(1)$ 狀態轉移，我們可以倒過來思考。當我們在看 target[k] 時，如果想知道從 word1[i:] 後綴中所有能匹配 target[k] 的位置貢獻，我們不需要每次都用迴圈去掃描，可以用一個 A 陣列與 B 陣列（後綴和） 在 $O(1)$ 時間內直接轉移！
"""
class Solution:
    def interleaveCharacters(self, word1: str, word2: str, target: str) -> int:
        mod = 10**9 + 7
        m, n, L = len(word1), len(word2), len(target)

        # dp[i][j][status] 代表完成 target[k:] 的合法組合數
        # status 位元設計：0=都沒選, 1=選過word1, 2=選過word2, 3=兩者都選過
        dp = [[[0] * 4 for _ in range(n + 1)] for _ in range(m + 1)]
        
        # 基礎狀態：當 target 完全匹配成功 (k == L) 時，只有當 status == 3 (兩者都選過) 才算 1 次成功
        for i in range(m + 1):
            for j in range(n + 1):
                dp[i][j][3] = 1

        # 從 target 的最後一個字元倒過來做動態規劃
        for k in range(L - 1, -1, -1):
            next_dp = [[[0] * 4 for _ in range(n + 1)] for _ in range(m + 1)]

            # 1. 預計算 A 表：代表從 word1[i:] 中挑選與 target[k] 匹配的後綴累積和
            A = [[[0] * 4 for _ in range(n + 1)] for _ in range(m + 1)]
            for j in range(n + 1):
                for i in range(m - 1, -1, -1):
                    for s in range(4):
                        # 如果當前字元匹配，就可以納入計算，並將狀態與 1 做 OR 運算
                        match_val = dp[i + 1][j][s | 1] if word1[i] == target[k] else 0
                        A[i][j][s] = (A[i + 1][j][s] + match_val) % mod

            # 2. 預計算 B 表：代表從 word2[j:] 中挑選與 target[k] 匹配的後綴累積和
            B = [[[0] * 4 for _ in range(n + 1)] for _ in range(m + 1)]
            for i in range(m + 1):
                for j in range(n - 1, -1, -1):
                    for s in range(4):
                        # 如果當前字元匹配，就可以納入計算，並將狀態與 2 做 OR 運算
                        match_val = dp[i][j + 1][s | 2] if word2[j] == target[k] else 0
                        B[i][j][s] = (B[i][j + 1][s] + match_val) % mod

            # 3. 合併 A、B 兩表的結果到當前層
            for i in range(m + 1):
                for j in range(n + 1):
                    for s in range(4):
                        next_dp[i][j][s] = (A[i][j][s] + B[i][j][s]) % mod

            # 滾動更新
            dp = next_dp

        # 最終答案即為：從 word1[0:], word2[0:] 開始，初始狀態為 0 的總方法數
        return dp[0][0][0]
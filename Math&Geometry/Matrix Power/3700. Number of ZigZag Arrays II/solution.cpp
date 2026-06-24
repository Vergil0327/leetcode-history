#include <vector>

using namespace std;

/*
第一步：狀態向量化（把多維變一維）
在原本的 DP 中，我們的狀態是 dp[dir][x]：

dir 有 2 種可能（0 = 下一個要變小, 1 = 下一個要變大）。
x 有 $m$ 種可能（目前結尾的數字）。

因為矩陣快速冪的形式是： $$\text{新狀態向量} = \text{轉移矩陣} \times \text{舊狀態向量}$$

我們必須把這 $2 \times m$ 個狀態「拉直」成一個長度為 $2m 的一維長條向量 $V$。
我們規定這個長條向量的排法如下：
- 前半段（索引 $0 \dots m-1$）：放 dir = 0 (DOWN) 的 $m$ 個狀態。
- 後半段（索引 $m \dots 2m-1$）：放 dir = 1 (UP) 的 $m$ 個狀態。

舉例：如果 $m = 3$（可選數字為 1, 2, 3，索引為 0, 1, 2）：

- $V[0], V[1], V[2]$ 分別代表目前以 1, 2, 3 結尾，且下一個要 DOWN。
- $V[3], V[4], V[5]$ 分別代表目前以 1, 2, 3 結尾，且下一個要 UP。

第二步：搞懂矩陣乘法的轉移方向
在標準的線性代數中，如果我們用「列向量（Column Vector）」：$$V_{\text{next}} = T \times V_{\text{curr}}$$

展開某個具體位置的計算會長這樣：$$V_{\text{next}}[i] = \sum (T[i][j] \times V_{\text{curr}}[j])$$
也就是矩陣的橫列（Row $i$）代表「下一格的狀態」；直欄（Column $j$）代表「現在這一格的狀態」。
$T[i][j] = 1$ 代表：我們可以從現在的狀態 $j$，轉移到未來的狀態 $i$。

第三步：將轉移矩陣切成「四個象限」

既然我們的向量長度是 $2m$，轉移矩陣 $T$ 自然就是 $2m \times 2m$。因為向量分成「前半段（DOWN）」和「後半段（UP）」，我們可以把整個轉移矩陣切成 $4$ 個 $m \times m$ 的小區塊（四象限）：
我們可以一行行來分析這四個區塊該填什麼：

1. 左上區塊（從 DOWN 轉移到 DOWN）
現在狀態：下一個要 DOWN（屬於前半段 $0 \dots m-1$）。
未來狀態：下一個還要 DOWN（屬於前半段 $0 \dots m-1$）。
分析：這違反了 ZigZag 增減交替的規則（不能連續兩次 DOWN）。因此，整個左上區塊全都是 0。

2. 右下區塊（從 UP 轉移到 UP）
分析：同理，不能連續兩次 UP。所以，整個右下區塊也全都是 0。

3. 右上區塊（從 UP 轉移到 DOWN）
現在狀態 $j$：屬於後半段，其真實數值是 $x = j - m$。此時下一個動作要變大（UP）。
未來狀態 $i$：屬於前半段，其真實數值是 $y = i$。此時因為剛變大完，所以下一個動作要變小（DOWN）。
轉移條件：既然是變大，未來的數值 $y$ 必須嚴格大於現在的數值 $x$（即 $y > x$）。
結論：當 $y > x$ 時，填入 1。這會在這個小區塊中形成一個嚴格上三角矩陣。

4. 左下區塊（從 DOWN 轉移到 UP）
現在狀態 $j$：屬於前半段，其真實數值是 $x = j$。此時下一個動作要變小（DOWN）。
未來狀態 $i$：屬於後半段，其真實數值是 $y = i - m$。此時因為剛變小完，所以下一個動作要變大（UP）。
轉移條件：既然是變小，未來的數值 $y$ 必須嚴格小於現在的數值 $x$（即 $y < x$）。
結論：當 $y < x$ 時，填入 1。這會在這個小區塊中形成一個嚴格下三角矩陣。

ex. 如果 $m = 3$，整個 $6 \times 6$ 的轉移矩陣填完後，視覺化出來會長得非常有規律：
現在 (curr) 的狀態 j
             [ - DOWN - ]  [ -- UP -- ]
             x=1  x=2  x=3  x=1  x=2  x=3
             ----------------------------
未來   y=1 |  0    0    0  |  0    0    0  | -> (未來 y=1 > 現在 x，無人符合)
(next) y=2 |  0    0    0  |  1    0    0  | -> (自現在 x=1 變大而來)
Row i  y=3 |  0    0    0  |  1    1    0  | -> (自現在 x=1, x=2 變大而來)
      ----------------------------
       y=1 |  0    1    1  |  0    0    0  | -> (自現在 x=2, x=3 變小而來)
       y=2 |  0    0    1  |  0    0    0  | -> (自現在 x=3 變小而來)
       y=3 |  0    0    0  |  0    0    0  | -> (未來 y=3 < 現在 x，無人符合)

矩陣丟進快速冪裡乘上 $n-1$ 次，它就能在 $O(\log n)$ 的時間內，同時完成所有數值之間的增減交替遞推
*/

class Solution {
private:
    // 矩陣乘法優化 (i -> k -> j 順序具備快取友善性，且主動跳過 0)
    vector<vector<long long>> multiply(const vector<vector<long long>>& A, const vector<vector<long long>>& B, long long mod) {
        int sz = A.size();
        vector<vector<long long>> C(sz, vector<long long>(sz, 0));
        for (int i = 0; i < sz; ++i) {
            for (int k = 0; k < sz; ++k) {
                if (A[i][k] == 0) continue; // 由於轉移矩陣有大半是 0，此處剪枝效益極大
                for (int j = 0; j < sz; ++j) {
                    C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod;
                }
            }
        }
        return C;
    }

    // 快速冪計算 T^exp
    vector<vector<long long>> matrixPower(vector<vector<long long>> base, int exp, long long mod) {
        int sz = base.size();
        vector<vector<long long>> res(sz, vector<long long>(sz, 0));
        for (int i = 0; i < sz; ++i) res[i][i] = 1; // 初始化為單位矩陣

        while (exp > 0) {
            if (exp % 2 == 1) res = multiply(res, base, mod);
            base = multiply(base, base, mod);
            exp /= 2;
        }
        return res;
    }

public:
    int zigZagArrays(int n, int l, int r) {
        int m = r - l + 1;
        int sz = 2 * m;
        long long MOD = 1e9 + 7;

        // 建立轉移矩陣 T
        vector<vector<long long>> T(sz, vector<long long>(sz, 0));

        for (int y = 0; y < m; ++y) {
            // DOWN, y 狀態接收來自於比自己小的 UP, x 狀態
            for (int x = 0; x < y; ++x) {
                T[y][m + x] = 1;
            }
            // UP, y 狀態接收來自於比自己大的 DOWN, x 狀態
            for (int x = y + 1; x < m; ++x) {
                T[m + y][x] = 1;
            }
        }

        // 計算 T^(n-1)
        T = matrixPower(T, n - 1, MOD);

        // 最終所有可能路徑總數即為 T^(n-1) 內所有元素的總和
        long long total_ans = 0;
        for (int i = 0; i < sz; ++i) {
            for (int j = 0; j < sz; ++j) {
                total_ans = (total_ans + T[i][j]) % MOD;
            }
        }

        return total_ans;
    }
};
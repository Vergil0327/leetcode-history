#include <vector>
using namespace std;

class Solution {
public:
    int zigZagArrays(int n, int l, int r) {
        int range_size = r - l + 1;
        long long MOD = 1e9 + 7;

        // dp0[x]: 結尾為 x，且下一個位置必須變小 (DOWN)
        // dp1[x]: 結尾為 x，且下一個位置必須變大 (UP)
        vector<long long> dp0(range_size, 0);
        vector<long long> dp1(range_size, 0);

        // 基礎狀態初始化 (長度為 2 的情況)
        // 對於任何 y，前面有 y 個比它小的數（可形成 UP 趨勢，故下一個要 DOWN，歸入 dp0）
        // 同理，後面有 (m - 1 - y) 個比它大的數（可形成 DOWN 趨勢，故下一個要 UP，歸入 dp1）
        for (int y = 0; y < range_size; ++y) {
            dp0[y] = y;
            dp1[y] = (range_size - 1) - y;
        }

        // 從長度 3 開始遞推到長度 n
        for (int step = 3; step <= n; ++step) {
            vector<long long> next_dp0(range_size, 0);
            vector<long long> next_dp1(range_size, 0);

            // 1. 利用前綴和優化計算 next_dp0
            long long prefix_sum = 0;
            for (int y = 0; y < range_size; ++y) {
                next_dp0[y] = prefix_sum;
                prefix_sum = (prefix_sum + dp1[y]) % MOD;
            }

            // 2. 利用後綴和優化計算 next_dp1
            long long suffix_sum = 0;
            for (int y = range_size - 1; y >= 0; --y) {
                next_dp1[y] = suffix_sum;
                suffix_sum = (suffix_sum + dp0[y]) % MOD;
            }

            // 滾動滾動更新 DP 陣列
            dp0 = move(next_dp0);
            dp1 = move(next_dp1);
        }

        // 統計長度為 n 時的所有合法組合總數
        long long ans = 0;
        for (int i = 0; i < range_size; ++i) {
            ans = (ans + dp0[i] + dp1[i]) % MOD;
        }

        return ans;
    }
};
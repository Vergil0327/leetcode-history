#include <vector>

using namespace std;
class Solution {
public:
    int subsequencePairCount(vector<int>& nums) {
        int n = nums.size();
        int max_val = 200; // 根據題目測資限制 nums[i] <= 200
        long long MOD = 1e9 + 7;

        // 建立三維動態規劃記憶表，初始化為 -1 代表尚未計算過
        // 空間大小：n * 201 * 201
        vector<vector<vector<int>>> memo(n, vector<vector<int>>(max_val + 1, vector<int>(max_val + 1, -1)));

        // 定義 Top-down DFS Lambda 函式
        // 這裡 self 必須使用引用傳遞 &self
        auto dfs = [&](int i, int g1, int g2, auto& self) -> int {
            // 基底條件：當所有數字都考慮完畢時
            if (i >= n) {
                // 只有當兩個子序列都「非空」(g1 > 0, g2 > 0) 且「GCD 相等」時，才算找到 1 種合法配對
                return (g1 > 0 && g2 > 0 && g1 == g2) ? 1 : 0;
            }

            // 查表：如果這個狀態先前已經算過，直接回傳答案
            if (memo[i][g1][g2] != -1) {
                return memo[i][g1][g2];
            }

            // 選擇 1：將 nums[i] 丟棄，不放入任何一個子序列
            long long res = self(i + 1, g1, g2, self);

            // 選擇 2：將 nums[i] 放入第一個子序列 (seq1)
            // std::gcd(0, x) 在 C++ 中會自動回傳 x，完美處理初始情況
            res = (res + self(i + 1, gcd(g1, nums[i]), g2, self)) % MOD;

            // 選擇 3：將 nums[i] 放入第二個子序列 (seq2)
            res = (res + self(i + 1, g1, gcd(g2, nums[i]), self)) % MOD;

            // 寫入緩存並回傳
            return memo[i][g1][g2] = res;
        };

        // 從索引 0 開始，此時兩個子序列的初始 GCD 皆為 0
        return dfs(0, 0, 0, dfs);
    }
};
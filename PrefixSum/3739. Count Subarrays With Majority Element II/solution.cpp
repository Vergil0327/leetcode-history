#include <vector>

using namespace std;

class Solution {
public:
    long long countMajoritySubarrays(vector<int>& nums, int target) {
        int n = nums.size();
        
        // 前綴和範圍在 [-n, n] 之間
        // 加上 offset = n + 1，將其映射到 [1, 2*n + 1] 區間，防止負數索引
        int offset = n + 1;
        vector<int> bit(2 * n + 2, 0);

        // 樹狀陣列標準操作：單點增加
        auto update = [&](int idx, int val) {
            for (; idx < bit.size(); idx += idx & -idx) {
                bit[idx] += val;
            }
        };

        // 樹狀陣列標準操作：前綴和查詢
        auto query = [&](int idx) {
            int sum = 0;
            for (; idx > 0; idx -= idx & -idx) {
                sum += bit[idx];
            }
            return sum;
        };

        long long res = 0;
        int presum = 0;

        // 初始狀態：當還沒包含任何元素時，l-1 = -1 的前綴和為 0
        // 將 0 映射後放入 BIT 中
        update(0 + offset, 1);

        for (int num : nums) {
            // 轉換為 +1 / -1
            presum += (num == target ? 1 : -1);
            
            // 我們需要找符合 previous_presum < presum 的個數
            // 即為查詢小於等於 presum - 1 的所有歷史紀錄總數
            res += query(presum - 1 + offset);
            
            // 將當前的 presum 記錄進 BIT 中
            update(presum + offset, 1);
        }

        return res;
    }
};
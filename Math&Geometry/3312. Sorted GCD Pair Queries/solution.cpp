// 這道題的關鍵在於 nums[i] 的數值範圍非常小（$\le 5 \times 10^4$）。如果我們直接枚舉所有兩兩配對並計算 GCD，總配對數可達 $5 \times 10^9$，勢必會超出時間限制。
// 我們可以反過來思考：直接統計「GCD 剛好等於 $g$」的配對到底有幾個。利用類似篩法（Sieve）與排容原理（Inclusion-Exclusion Principle）的思維，我們可以在極短的時間內完成統計，接著使用前綴和搭配二分搜尋法來快速回應所有的查詢。

// 解題思維拆解統計倍數個數：令 M 為 nums 中的最大值。我們統計每個數字出現的頻率後，可以計算出「陣列中是 $g$ 的倍數的元素總共有幾個」，記為 multiples[g]。計算包含公因數 $g$ 的配對數：如果兩個數都是 $g$ 的倍數，那麼這兩個數的 GCD 也一定是 $g$ 的倍數。這類配對的總數為：$$\text{total\_pairs} = \frac{\text{multiples}[g] \times (\text{multiples}[g] - 1)}{2}$$
// 倒推求得「精確 GCD」 (排容原理)：上述算出的 total_pairs 不僅包含了 GCD 剛好為 $g$ 的配對，也包含了 GCD 為 $2g, 3g, 4g \dots$ 的配對。因此，我們只要從大到小（從 M 倒推回 1）計算，每次扣掉所有更大倍數的精確配對數，就能得到「GCD 剛好為 $g$ 的精確配對數」，記為 exact[g]：$$\text{exact}[g] = \text{total\_pairs} - \sum_{k=2}^{\lfloor M/g \rfloor} \text{exact}[k \cdot g]$$前綴和 + 二分搜尋：將 exact 陣列做前綴和得到 pref。因為 gcdPairs 是由小到大排序的，所以 GCD 為 1 的會排在最前面，接著是 2...以此類推。對於每一個詢問的索引 q，我們只要在 pref 陣列中做 std::upper_bound，找到第一個前綴和大於 q 的位置，該位置的索引就是我們要找的 GCD 值。

#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

class Solution {
public:
    vector<int> gcdValues(vector<int>& nums, vector<long long>& queries) {
        int M = *max_element(nums.begin(), nums.end());
        
        // 1. 統計每個數字的出現頻率
        vector<long long> cnt(M + 1, 0);
        for (int x : nums) {
            cnt[x]++;
        }
        
        // 2. 統計身為 g 的倍數的元素個數
        vector<long long> multiples(M + 1, 0);
        for (int g = 1; g <= M; ++g) {
            for (int k = g; k <= M; k += g) {
                multiples[g] += cnt[k];
            }
        }
        
        // 3. 倒推計算「GCD 剛好等於 g」的精確配對數 (排容原理)
        vector<long long> exact(M + 1, 0);
        for (int g = M; g >= 1; --g) {
            long long total_pairs = (multiples[g] * (multiples[g] - 1)) / 2;
            // 扣除所有以 g 為因數的更大 GCD 配對 (如 2g, 3g, 4g...)
            for (int k = 2 * g; k <= M; k += g) {
                total_pairs -= exact[k];
            }
            exact[g] = total_pairs;
        }
        
        // 4. 建立前綴和陣列以供區間定位
        vector<long long> pref(M + 1, 0);
        for (int g = 1; g <= M; ++g) {
            pref[g] = pref[g - 1] + exact[g];
        }
        
        // 5. 透過二分搜尋 (upper_bound) 線性回答所有查詢
        vector<int> ans;
        ans.reserve(queries.size());
        for (long long q : queries) {
            // 尋找第一個累積配對數大於 q 的 GCD 門檻
            auto it = upper_bound(pref.begin(), pref.end(), q);
            ans.push_back(distance(pref.begin(), it));
        }
        
        return ans;
    }
};
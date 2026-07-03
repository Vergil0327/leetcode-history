#include <vector>
#include <algorithm>

using namespace std;

/**
 * 
 * 既然「一邊要最小化，一邊要最大化」會打架，最好的解法就是用二分搜尋法把他們拆開：
 * 
 * 二分猜測分數（mid）：我們盲猜這條路徑的最低分數是 mid。既然分數必須 $\ge mid$，那圖中所有花費小於 mid 的邊我們直接裝作看不見（不走）。
 * 拓撲排序最短路徑：因為題目保證這是一個 DAG（有向無環圖），在過濾掉「小於 mid 的邊」和「離線節點」後，我們只要用最簡單的拓撲排序 + 動態規劃（DP），就能在 $O(V+E)$ 的極速時間內，算出從 $0$ 到 $n-1$ 的最少花費。
 * 如果這個最少花費 $\le k$，說明 mid 是可行的！
 */
class Solution {
public:
    int findMaxPathScore(vector<vector<int>>& edges, vector<bool>& online, long long k) {
        int n = online.size();
        
        // 1. 乾淨地建立鄰接表，並記錄全域最高的花費作為二分搜尋的上限
        vector<vector<pair<int, int>>> graph(n);
        int max_cost = 0;
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], c = edge[2];
            graph[u].push_back({v, c});
            max_cost = max(max_cost, c);
        }

        // 2. 預先做一次拓撲排序 (只走在線上的節點)
        vector<int> topo;
        vector<bool> visited(n, false);
        
        auto dfs = [&](auto& self, int u) -> void {
            visited[u] = true;
            for (const auto& [v, c] : graph[u]) {
                if (!visited[v] && online[v]) {
                    self(self, v);
                }
            }
            topo.push_back(u);
        };
        
        // 從起點 0 開始進行拓撲排序
        dfs(dfs, 0);
        reverse(topo.begin(), topo.end());

        // 3. 檢查函數：是否存在一條路徑，其所有邊都 >= mid，且總花費 <= k
        auto check = [&](int mid) -> bool {
            vector<long long> dp(n, LLONG_MAX);
            dp[0] = 0;

            for (int u : topo) {
                if (dp[u] == LLONG_MAX) continue;
                for (const auto& [v, c] : graph[u]) {
                    // 💥關鍵過濾：分數不達標的邊直接不走
                    if (c >= mid) {
                        if (dp[u] + c < dp[v]) {
                            dp[v] = dp[u] + c;
                        }
                    }
                }
            }
            return dp[n - 1] <= k;
        };

        // 4. 二分搜尋最大化路徑分數
        int low = 0, high = max_cost, ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid)) {
                ans = mid;      // 記錄可行解
                low = mid + 1;  // 試圖挑戰更高的分數
            } else {
                high = mid - 1; // 門檻太高了，降低要求
            }
        }

        return ans;
    }
};
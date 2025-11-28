#include <vector>
#include <functional>
using namespace std;


class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        vector<vector<int>> graph(n, vector<int>(0, 0));
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        for (auto& value : values) {
            value %= k;
        }

        function<pair<int,int>(int, int)> dfs = [&](int node, int prev) -> pair<int,int> {
            int cur = values[node];
            int split = 0;
            for (auto& nxt : graph[node]) {
                if (nxt == prev) continue;
                auto [sum, cnt] = dfs(nxt, node);
                cur += sum;
                split += cnt;
            }

            cur %= k;
            if (cur == 0) {
                split++;
            }

            return {cur, split};
        };

        return dfs(0, -1).second;
    }
};
/*
想法是由於我們是起點出發
所以起點往其他城市的路要轉向, 耗費cost=1, 也就是
connections[i] = [a, b] (a -> b) 加上cost=1, 代表我們reorienting connections[i]這條邊
同時加上connections[j] = [b, a] (b -> a) 加上cost=0
透過這些資訊後我們從起點city-0出發, BFS掃過一遍即可
*/

class Solution {
public:
    int minReorder(int n, vector<vector<int>>& connections) {
        vector<vector<pair<int, int>>> graph(n); // {u: [v, cost]}
        for (auto conn : connections) {
            graph[conn[0]].push_back({conn[1], 1});
            graph[conn[1]].push_back({conn[0], 0});
        }

        queue<int> q;
        q.push(0);

        vector<int> visited(n, 0);
        visited[0] = 1;

        int res = 0;
        while (!q.empty()) {
            int len = q.size();
            while (len--) {
                int city = q.front();
                q.pop();

                for (auto [dst, cost] : graph[city]) {
                    if (visited[dst]) continue;
                    visited[dst] = 1;

                    res += cost;
                    q.push(dst);
                }
            }
        }
        return res;
    }
};
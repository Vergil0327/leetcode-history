#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int maximumSafenessFactor(vector<vector<int>>& grid) {
        int n = grid.size();
        
        // 邊界特判：起點或終點直接有竊賊，安全係數直接為 0
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) return 0;

        // 用於計算到最近竊賊距離的佇列：儲存 {r, c}
        queue<pair<int, int>> q;
        // dist[r][c] 儲存該格子到最近竊賊的距離，初始為 -1 代表未訪問
        vector<vector<int>> dist(n, vector<int>(n, -1));

        // 1. 將所有竊賊的位置放入佇列中作為 BFS 起點
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    q.push({i, j});
                    dist[i][j] = 0; // 竊賊所在格子的距離為 0
                }
            }
        }

        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // 2. 多源 BFS：計算全地圖所有點到最近竊賊的曼哈頓距離
        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            for (const auto& dir : dirs) {
                int row = r + dir[0], col = c + dir[1];
                if (row >= 0 && row < n && col >= 0 && col < n && dist[row][col] == -1) {
                    dist[row][col] = dist[r][c] + 1;
                    q.push({row, col});
                }
            }
        }

        // 3. Dijkstra 演算法：尋找最大化安全係數的路徑
        // 優先佇列儲存：{該路徑至今為止的最小安全係數, r, c}，預設為最大堆（大頂堆）
        priority_queue<vector<int>> pq;
        vector<vector<bool>> visited(n, vector<bool>(n, false));

        pq.push({dist[0][0], 0, 0});
        visited[0][0] = true;

        while (!pq.empty()) {
            auto curr = pq.top();
            pq.pop();
            
            int fac = curr[0], r = curr[1], c = curr[2];

            // 抵達終點，此時的 fac 必然是全域最優解
            if (r == n - 1 && c == n - 1) return fac;

            for (const auto& dir : dirs) {
                int row = r + dir[0], col = c + dir[1];
                if (row >= 0 && row < n && col >= 0 && col < n && !visited[row][col]) {
                    visited[row][col] = true;
                    // 路徑上的瓶頸安全係數取決於「先前的瓶頸」與「新格子安全度」的較小值
                    pq.push({min(fac, dist[row][col]), row, col});
                }
            }
        }

        return -1;
    }
};
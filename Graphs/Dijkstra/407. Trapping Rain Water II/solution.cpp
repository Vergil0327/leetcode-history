class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        int m = heightMap.size(), n = heightMap[0].size();

        vector<vector<bool>> visited(m, vector<bool>(n, false));
        priority_queue<pair<int, pair<int,int>>, 
                       vector<pair<int, pair<int,int>>>, 
                       greater<>> border;

        // Add border cells
        for (int j = 0; j < n; j++) {
            border.push({heightMap[0][j], {0, j}});
            border.push({heightMap[m-1][j], {m-1, j}});
            visited[0][j] = visited[m-1][j] = 1;
        }
        for (int i = 1; i < m-1; i++) {
            border.push({heightMap[i][0], {i, 0}});
            border.push({heightMap[i][n-1], {i, n-1}});
            visited[i][0] = visited[i][n-1] = 1;
        }

        int direction[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
        int trapped = 0;

        while (!border.empty()) {
            auto [h, pos] = border.top(); border.pop();
            int x = pos.first, y = pos.second;

            for (auto& [dx, dy] : direction) {
                int nx = x + dx, ny = y + dy;
                if (nx < 0 || ny < 0 || nx >= m || ny >= n || visited[nx][ny]) continue;
    
                visited[nx][ny] = true;
                trapped += max(0, h - heightMap[nx][ny]);
                border.push({max(h, heightMap[nx][ny]), {nx, ny}});
            }
        }

        return trapped;
    }
};
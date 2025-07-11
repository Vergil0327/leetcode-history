
#define pii pair<int,int>
class Solution {
    int dirs[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    int visited = 5;
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m=grid.size(), n=grid[0].size();

        queue<pii> q;
        int fresh = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i, j});
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }
        if (fresh == 0) return 0;

        int t = 0;
        while (!q.empty()) {
            int len=q.size();
            while (len--) {
                auto [r,c] = q.front();
                q.pop();
    
                for (auto [dr, dc] : dirs) {
                    int row=r+dr, col=c+dc;
                    if (row<0 || row >= m || col<0 || col>=n) continue;
                    if (grid[row][col] != 1) continue;
                    fresh--;
                    grid[row][col] = 2;
                    q.push({row, col});
                }
            }
            t++;
            if (fresh == 0) return t;
        }
        return -1;
    }
};

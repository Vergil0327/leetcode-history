class Solution {
    int dirs[4][2]={{1,0},{-1,0},{0,1},{0,-1}};
public:
    int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
        int m=maze.size(), n=maze[0].size();

        queue<pair<int,int>> q;
        q.push({entrance[0], entrance[1]});

        int step = 0;
        while (!q.empty()) {
            int len = q.size();
            while (len--) {
                auto [r,c] = q.front();
                q.pop();

                if ((r!=entrance[0] || c!=entrance[1]) && (r==0 || r==m-1 || c==0 || c==n-1)) return step;
                if (maze[r][c] == '+') continue;
                maze[r][c] = '+';

                for (auto [dr, dc] : dirs) {
                    int row=r+dr, col=c+dc;
                    if (row<0 || row >=m || col<0 || col>=n) continue;
                    if (maze[row][col] == '+') continue;
                    q.push({row, col});
                }   
            }
            step++;
        }
        return -1;
    }
};

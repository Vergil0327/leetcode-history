using pii = pair<int,int>;

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1,T2> &p) const {
        auto h1 = std::hash<T1>{}(p.first);
        auto h2 = std::hash<T2>{}(p.second);

        // Mainly for demonstration purposes, i.e. works but is overly simple
        // In the real world, use sth. like boost.hash_combine
        return h1 ^ h2;  
    }
};

class Solution {
private:
    int m, n;
    unordered_map<pii, pii, pair_hash> dirs {
        {{1,-1}, {-1,-1}},
        {{-1,-1}, {-1,1}},
        {{-1,1}, {1,1}},
        {{1,1}, {1,-1}},
    };

    int memo[505][505][3][2][7];

    int dfs(int r, int c, int v, pii direction, bool didTurn, vector<vector<int>>& grid) {

        int m = grid.size(), n = grid[0].size();
        int hashD = 2 * direction.first + direction.second + 3;
        if (memo[r][c][v][didTurn][hashD] > 0) return memo[r][c][v][didTurn][hashD];

        int wanted = 2-v;
        int row = r+direction.first, col = c+direction.second;
        if (0 <= row && row < m && 0 <= col && col < n) {
            if (v == 1 && grid[row][col] == 2) {
                memo[r][c][v][didTurn][hashD] = max(memo[r][c][v][didTurn][hashD], dfs(row, col, grid[row][col], direction, didTurn, grid) + 1);
            } else if ((v == 2 || v == 0) && grid[row][col] == wanted) {
                memo[r][c][v][didTurn][hashD] = max(memo[r][c][v][didTurn][hashD], dfs(row, col, grid[row][col], direction, didTurn, grid) + 1);
            }
        }

        if (!didTurn) {
            pii new_dir = dirs[direction];
            memo[r][c][v][didTurn][hashD] = max(memo[r][c][v][didTurn][hashD], dfs(r, c, v, new_dir, 1, grid));
        }
        return memo[r][c][v][didTurn][hashD];
    }
public:
    int lenOfVDiagonal(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();

        int res = 0;
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == 1) {
                    for (auto& it : dirs) {
                        res = max(res, dfs(i, j, grid[i][j], it.first, 0, grid)+1);
                    }
                }
            }
        }
        return res;
    }
};

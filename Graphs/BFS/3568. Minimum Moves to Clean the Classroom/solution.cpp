#include <vector>
#include <string>
#include <queue>

using namespace std;

class Solution {
public:
    int minMoves(vector<string>& classroom, int energy) {
        int m = classroom.size(), n = classroom[0].size();
        
        int start_r = -1, start_c = -1;
        vector<vector<int>> litter_id(m, vector<int>(n, -1));
        int total_litter = 0;

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (classroom[i][j] == 'S') {
                    start_r = i;
                    start_c = j;
                } else if (classroom[i][j] == 'L') {
                    litter_id[i][j] = total_litter++;
                }
            }
        }

        int target_mask = (1 << total_litter) - 1;
        
        // bestEnergy[r][c][mask] stores the max remaining energy seen for state (r, c, mask)
        vector<vector<vector<int>>> bestEnergy(
            m, vector<vector<int>>(n, vector<int>(1 << total_litter, -1))
        );

        int start_mask = 0;
        if (classroom[start_r][start_c] == 'L') {
            start_mask |= (1 << litter_id[start_r][start_c]);
        }

        queue<vector<int>> q;
        q.push({start_r, start_c, start_mask, energy});
        bestEnergy[start_r][start_c][start_mask] = energy;

        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int steps = 0;

        while (!q.empty()) {
            int sz = q.size();
            while (sz--) {
                auto cur = q.front();
                q.pop();

                int r = cur[0], c = cur[1], mask = cur[2], e = cur[3];

                if (mask == target_mask) return steps;

                // Cannot make any further moves from (r, c) if energy is 0
                if (e == 0) continue;

                for (const auto& d : dirs) {
                    int nr = r + d[0], nc = c + d[1];

                    if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                    if (classroom[nr][nc] == 'X') continue;

                    int next_e = e - 1;
                    int next_mask = mask;

                    if (classroom[nr][nc] == 'L') {
                        next_mask |= (1 << litter_id[nr][nc]);
                    }

                    if (classroom[nr][nc] == 'R') {
                        next_e = energy;
                    }

                    if (next_e > bestEnergy[nr][nc][next_mask]) {
                        bestEnergy[nr][nc][next_mask] = next_e;
                        q.push({nr, nc, next_mask, next_e});
                    }
                }
            }
            steps++;
        }

        return -1;
    }
};
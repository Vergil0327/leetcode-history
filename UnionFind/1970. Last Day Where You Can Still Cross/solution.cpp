#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <numeric>
#include <map>

using namespace std;

class Solution {
public:
    struct DSU {
        vector<int> parent;
        DSU(int n) {
            parent.resize(n);
            iota(parent.begin(), parent.end(), 0);
        }
        int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        void unite(int x, int y) {
            int rootX = find(x);
            int rootY = find(y);
            if (rootX != rootY) parent[rootX] = rootY;
        }
    };

    int latestDayToCross(int m, int n, vector<vector<int>>& cells) {
        // Grid to track land (0) vs water (1). 
        // We start with all water because we are going backwards in time.
        vector<vector<int>> grid(m, vector<int>(n, 1));
        
        DSU dsu(m * n + 2);
        int TOP = m * n;
        int BOTTOM = m * n + 1;
        int dirs[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        // Iterate from the last day backwards
        for (int i = cells.size() - 1; i >= 0; --i) {
            int r = cells[i][0] - 1; // Convert 1-based to 0-based
            int c = cells[i][1] - 1;
            
            grid[r][c] = 0; // Turn water to land
            int key = r * n + c;

            // Connect to virtual TOP/BOTTOM nodes
            if (r == 0) dsu.unite(key, TOP);
            if (r == m - 1) dsu.unite(key, BOTTOM);

            // Connect to existing land neighbors
            for (auto& d : dirs) {
                int row = r + d[0];
                int col = c + d[1];
                if (row >= 0 && row < m && col >= 0 && col < n && grid[row][col] == 0) {
                    dsu.unite(key, row * n + col);
                }
            }

            // Check if a path exists
            if (dsu.find(TOP) == dsu.find(BOTTOM)) {
                return i;
            }
        }

        return 0;
    }
};
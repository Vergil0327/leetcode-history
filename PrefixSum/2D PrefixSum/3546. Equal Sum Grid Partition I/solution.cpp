#include <vector>

using namespace std;

using LL = long long;

class RegionSum {
    // Padding with size + 1 to avoid manual boundary checks
    vector<vector<LL>> presum;
public:
    RegionSum(vector<vector<int>>& A) {
        int m = A.size();
        int n = A[0].size();
        presum.assign(m + 1, vector<LL>(n + 1, 0));
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Formula: current + up + left - diagonal_up_left
                presum[i + 1][j + 1] = A[i][j] + presum[i][j + 1] + presum[i + 1][j] - presum[i][j];
            }
        }
    }

    // Change return type to LL to prevent overflow
    LL query(int r1, int c1, int r2, int c2) {
        // Standard 2D Range Sum Query formula
        return presum[r2 + 1][c2 + 1] - presum[r1][c2 + 1] - presum[r2 + 1][c1] + presum[r1][c1];
    }
};

class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        RegionSum region(grid);

        LL total = region.query(0, 0, m - 1, n - 1);
        
        // If the total is odd, we can never partition it into two equal integers
        if (total % 2 != 0) return false;
        LL target = total / 2;

        // Try Horizontal Cuts (must leave at least one row on each side)
        for (int i = 0; i < m - 1; i++) {
            if (region.query(0, 0, i, n - 1) == target) return true;
        }

        // Try Vertical Cuts (must leave at least one column on each side)
        for (int j = 0; j < n - 1; j++) {
            if (region.query(0, 0, m - 1, j) == target) return true;
        }

        return false;
    }
};
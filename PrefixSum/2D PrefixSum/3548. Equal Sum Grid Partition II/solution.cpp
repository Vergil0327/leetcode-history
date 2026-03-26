#include <vector>
#include <unordered_map>

using namespace std;

using LL = long long;

class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        LL totalSum = 0;
        unordered_map<int, int> totalFreq;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                totalSum += grid[i][j];
                totalFreq[grid[i][j]]++;
            }
        }

        // --- 1. Horizontal Cuts ---
        LL topSum = 0;
        unordered_map<int, int> topFreq;
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n; j++) {
                topSum += grid[i][j];
                topFreq[grid[i][j]]++;
            }
            LL bottomSum = totalSum - topSum;
            
            // Check Top Section
            if (check(topSum, bottomSum, i + 1, n, topFreq, {grid[i][0], grid[i][n-1], grid[0][0], grid[0][n-1]})) return true;
            // Check Bottom Section (Bottom Freq = Total Freq - Top Freq)
            if (check(bottomSum, topSum, m - 1 - i, n, topFreq, {grid[i+1][0], grid[i+1][n-1], grid[m-1][0], grid[m-1][n-1]}, &totalFreq)) return true;
        }

        // --- 2. Vertical Cuts ---
        LL leftSum = 0;
        unordered_map<int, int> leftFreq;
        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m; i++) {
                leftSum += grid[i][j];
                leftFreq[grid[i][j]]++;
            }
            LL rightSum = totalSum - leftSum;

            // Check Left Section
            if (check(leftSum, rightSum, m, j + 1, leftFreq, {grid[0][j], grid[m-1][j], grid[0][0], grid[m-1][0]})) return true;
            // Check Right Section
            if (check(rightSum, leftSum, m, n - 1 - j, leftFreq, {grid[0][j+1], grid[m-1][j+1], grid[0][n-1], grid[m-1][n-1]}, &totalFreq)) return true;
        }

        return false;
    }

private:
    bool check(LL s1, LL s2, int rows, int cols, unordered_map<int, int>& f1, vector<int> ends, unordered_map<int, int>* totalF = nullptr) {
        if (s1 == s2) return true;
        LL target = s1 - s2;
        if (target <= 0 || target > 1e9) return false;
        int t = (int)target;

        // Determine if target exists in this section
        bool exists = false;
        if (!totalF) { // We are checking the "current" built section (Top/Left)
            exists = f1.count(t) && f1[t] > 0;
        } else { // We are checking the "remaining" section (Bottom/Right)
            exists = ((*totalF).count(t) ? (*totalF)[t] : 0) - (f1.count(t) ? f1[t] : 0) > 0;
        }

        if (!exists) return false;

        // Connectivity Rule:
        // If 2D (rows > 1 && cols > 1), any existing cell is a valid discount.
        if (rows > 1 && cols > 1) return true;
        
        // If 1D, target must be one of the ends
        for (int e : ends) if (e == t) return true;
        
        return false;
    }
};
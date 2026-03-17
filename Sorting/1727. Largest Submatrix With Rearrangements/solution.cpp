#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <queue>

using namespace std;

class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();

        int res = 0;
        vector<int> histogram(n, 0);
        for (int r=0; r<m; r++) {
            for (int c=0; c<n; c++) {
                if (matrix[r][c] == 1) {
                    histogram[c]++;
                } else {
                    histogram[c] = 0;
                }
            }

            // Create a copy to sort so we don't scramble the column heights
            vector<int> sortedHeights = histogram;
            sort(sortedHeights.rbegin(), sortedHeights.rend());

            int height = INT_MAX;
            for (int c=0; c<n; c++) {
                height = min(height, sortedHeights[c]);
                int width = c+1;
                res = max(res, width * height);
            }
        }

        return res;
    }
};

class Solution
{
public:
    int largestSubmatrix(vector<vector<int>>& matrix)
    {
        int m = matrix.size(), n = matrix[0].size();
        int ans = 0;
        for(int j = 0; j < n; j++){
            for(int i = 1; i < m; i++)
                if(matrix[i][j] == 1)
                    matrix[i][j] += matrix[i-1][j];
        }
        for(int i = 0; i < m; i++)
        {
            sort(matrix[i].begin(), matrix[i].end());
            reverse(matrix[i].begin(), matrix[i].end());
            for(int j = 0; j < n; j++)
                ans = max(ans, matrix[i][j]*(j+1));
        }
        return ans;
    }
};
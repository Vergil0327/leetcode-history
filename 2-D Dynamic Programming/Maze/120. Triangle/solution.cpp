class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int n = triangle.size();
        int m = triangle[n-1].size();

        vector<vector<int>> dp(n, vector(m, INT_MAX));
        dp[0][0] = triangle[0][0];

        queue<pair<int,int>> q;
        q.push({0, 0}); // {row, col}

        for (int i=0; i<n-1; i++) {
            for (int j=0; j<i+1; j++) {
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+triangle[i+1][j]);
                dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+triangle[i+1][j+1]);
            }
        }
        return *min_element(dp[n-1].begin(), dp[n-1].end());
    }
};

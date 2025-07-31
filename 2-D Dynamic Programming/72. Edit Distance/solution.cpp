class Solution {
public:
    int minDistance(string word1, string word2) {
        int m=word1.size(), n=word2.size();
        word1 = "#" + word1;
        word2 = "#" + word2;
        vector<vector<int>> dp(m+1, vector<int>(n+1, INT_MAX/2));
        dp[0][0] = 0;
        for (int i=1; i<=m; i++) {
            dp[i][0] = i; // delete
        }
        for (int j=1; j<=n; j++) {
            dp[0][j] = j; // insert
        }
        for (int i=1; i<=m; i++) {
            for (int j=1; j<=n; j++) {
                if (word1[i] == word2[j]) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    // dp[i-1][j]+1 // delete text1[i]
                    // dp[i][j-1]+1 // insert text2[j] to text1
                    // dp[i-1][j-1]+1 // replace text1[i] with text2[j], now we only need to the ways to make text1[:i-1] == text2[:j-1]
                    dp[i][j] = min({dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1});
                }
            }
        }

        return dp[m][n]; // consider the min distance
    }
};

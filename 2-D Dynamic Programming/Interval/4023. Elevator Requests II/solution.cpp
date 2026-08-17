#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    long long elevatorRequests(int n, int start, vector<int>& requests) {
        vector<int> reqs;
        for (int r : requests) {
            if (r != start) {
                reqs.push_back(r);
            }
        }
        if (reqs.empty()) return 0;
        
        sort(reqs.begin(), reqs.end());
        int m = reqs.size();
        
        int pos = 0;
        while (pos < m && reqs[pos] < start) {
            pos++;
        }
        
        const long long INF = 1e18;
        vector<vector<vector<long long>>> dp(m, vector<vector<long long>>(m, vector<long long>(2, INF)));
        
        if (pos - 1 >= 0) {
            long long dist = start - reqs[pos - 1];
            dp[pos - 1][pos - 1][0] = dist * m;
            dp[pos - 1][pos - 1][1] = dist * m;
        }
        if (pos < m) {
            long long dist = reqs[pos] - start;
            dp[pos][pos][0] = dist * m;
            dp[pos][pos][1] = dist * m;
        }
        
        for (int len = 1; len <= m; ++len) {
            for (int i = 0; i <= m - len; ++i) {
                int j = i + len - 1;
                long long rem = m - len;
                
                // Expand left
                if (i > 0) {
                    long long cost_left = rem * (reqs[i] - reqs[i - 1]);
                    dp[i - 1][j][0] = min(dp[i - 1][j][0], dp[i][j][0] + cost_left);
                    
                    long long cost_right = rem * (reqs[j] - reqs[i - 1]);
                    dp[i - 1][j][0] = min(dp[i - 1][j][0], dp[i][j][1] + cost_right);
                }
                
                // Expand right
                if (j + 1 < m) {
                    long long cost_left = rem * (reqs[j + 1] - reqs[i]);
                    dp[i][j + 1][1] = min(dp[i][j + 1][1], dp[i][j][0] + cost_left);
                    
                    long long cost_right = rem * (reqs[j + 1] - reqs[j]);
                    dp[i][j + 1][1] = min(dp[i][j + 1][1], dp[i][j][1] + cost_right);
                }
            }
        }
        
        return min(dp[0][m - 1][0], dp[0][m - 1][1]);
    }
};
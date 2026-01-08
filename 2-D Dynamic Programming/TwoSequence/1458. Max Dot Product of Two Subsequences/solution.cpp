#include <string>
#include <vector>
#include <numeric>

using namespace std;

class Solution
{
public:
    int maxDotProduct(vector<int> &nums1, vector<int> &nums2)
    {
        int m = nums1.size();
        int n = nums2.size();

        nums1.insert(nums1.begin(), 0);
        nums2.insert(nums2.begin(), 0);

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, INT_MIN / 2));
        dp[0][0] = 0;

        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                dp[i][j] = max({dp[i][j], dp[i - 1][j], dp[i][j - 1]});
                dp[i][j] = max({dp[i][j], nums1[i] * nums2[j], dp[i - 1][j - 1] + nums1[i] * nums2[j]});
            }
        }

        return dp[m][n];
    }
};
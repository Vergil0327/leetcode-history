class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();
        prices.insert(prices.begin(), 0);

        // dp[i][0]: bought
        // dp[i][1]: sold
        vector<vector<int>> dp(n+1, vector<int>(2, INT_MIN/2));
        dp[0][1] = 0;

        for (int i=1; i<=n; i++) {
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]); // buy / not but
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee); // not sold / sold
        }
        return dp[n][1];
    }
};

// space-optimized
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int n = prices.size();
        if (n == 1) return 0;

        int bought = -prices[0], new_bought;;
        int sold = 0, new_sold;
        for (int i=1; i<n; i++) {
            new_sold = max(sold, bought + prices[i] - fee);
            new_bought = max(bought, sold - prices[i]);
            swap(sold, new_sold);
            swap(bought, new_bought);
        }
        return sold;
    }
};

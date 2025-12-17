#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    long long maximumProfit(vector<int>& prices, int k) {
        int n = prices.size();

        vector<vector<vector<long long>>>memo(n+1, vector<vector<long long>>(k+1, vector<long long>(3, -1)));

        function<long long (int i, int k, int type)> dfs = [&](int i, int k, int type) -> long long {
            if (i >= n) return (k >= 0 && type == 0 ? 0 : LLONG_MIN/2);

            if (memo[i][k][type] == -1) {
                memo[i][k][type] = dfs(i+1, k, type);
                if (k > 0) {
                    if (type == 0) {
                        long long res1 = dfs(i+1, k, 1) - prices[i];
                        long long res2 = dfs(i+1, k, 2) + prices[i];
                        memo[i][k][type] = max(memo[i][k][type], max(res1, res2));
                    } else if (type == 1) /* normal tx */ {
                        memo[i][k][type] = max(memo[i][k][type], dfs(i+1, k-1, 0) + prices[i]);
                    } else if (type == 2) /* sell short */ {
                        memo[i][k][type] = max(memo[i][k][type], dfs(i+1, k-1, 0) - prices[i]);
                    }
                }
            }

            return memo[i][k][type];
        };

        return dfs(0, k, 0);
    }
};


class Solution {
public:
    long long maximumProfit(vector<int>& prices, int k) {
        static const long long NEG_INF = LLONG_MIN/2;

        vector<long long> bought(k, NEG_INF);
        vector<long long> sold(k, NEG_INF);
        vector<long long> result(k + 1, NEG_INF);
        result[0] = 0;
        for (const auto& x : prices) {
            for (int kk = k - 1; kk >= 0; --kk) {
                if (bought[kk] != NEG_INF) {
                    result[kk + 1] = max(result[kk + 1], bought[kk] + x);
                }
                if (sold[kk] != NEG_INF) {
                    result[kk + 1] = max(result[kk + 1], sold[kk] - x);
                }
                if (result[kk] != NEG_INF) {
                    bought[kk] = max(bought[kk], result[kk] - x);
                    sold[kk] = max(sold[kk], result[kk] + x);
                }
            }
        }

        long long res = LLONG_MIN;
        for (const auto rslt : result) {
            res = max(res, rslt);
        }
        return res;
    }
};
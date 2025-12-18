#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    long long maxProfit(vector<int>& prices, vector<int>& strategy, int k) {
        int n = prices.size();
        vector<long long> presum(n+1, 0);
        vector<long long> preprof(n+1, 0);
        long long res = 0;
        for (int i=0; i<n; i++) {
            res += prices[i] * strategy[i];
            presum[i+1] = presum[i] + prices[i];
            preprof[i+1] = preprof[i] + prices[i] * strategy[i];
        }

        for (int i=k-1; i<n; i++) {
            long long operation = presum[i+1] - presum[i+1-k/2];
            long long right = preprof[n] - preprof[i+1];
            long long left = preprof[i+1-k];
            res = max(res, left + operation + right);
        }
        return res;
    }
};

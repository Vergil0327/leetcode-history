class Solution {
private:
    double servings[4][2] = {{4, 0}, {3, 1}, {2, 2}, {1, 3}};
public:
    double soupServings(int n) {
        int m = ceil(n / 25.0);

        unordered_map<int, unordered_map<int, double>> dp;

        function<double(int, int)> dfs = [&](int A, int B) -> double {
            if (A <= 0 && B <= 0) {
                return 0.5;
            }
            if (A <= 0) {
                return 1;
            }
            if (B <= 0) {
                return 0;
            }
            if (dp[A].count(B)) {
                return dp[A][B];
            }

            for (const auto& [dA, dB] : servings) {
                dp[A][B] += 0.25 * dfs(A-dA, B-dB);
            }
            return dp[A][B];
        };

        for (int k = 1; k <= m; k++) {
            if (dfs(k, k) > 1 - 1e-5) { // 0.99999... almost 1.0
                return 1;
            }
        }
        return dfs(m, m);
    }
};
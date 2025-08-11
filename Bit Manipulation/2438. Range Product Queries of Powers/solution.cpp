class Solution {
private:
    long long mod = 1e9+7;
public:
    vector<int> productQueries(int n, vector<vector<int>>& queries) {
        vector<long long> powers;
        int base = 0;
        while (n > 0) {
            if ((n&1) == 1) {
                powers.push_back((long long) pow(2, base) % mod);
            }
            base++;
            n >>= 1;
        };

        vector<int> res(queries.size(), 1);
        for (int i=0; i< queries.size(); i++) {
            for (int j=queries[i][0]; j<=queries[i][1]; j++) {
                res[i] = (res[i] * powers[j]) % mod;
            }
        }
        return res;
    }
};
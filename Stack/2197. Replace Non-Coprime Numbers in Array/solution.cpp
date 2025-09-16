class Solution {
public:
    vector<int> replaceNonCoprimes(vector<int>& nums) {
        vector<int> stk;
        for (auto& num : nums) {
            if (!stk.empty()) {
                long long num2 = stk.back();
                long long GCD = gcd(num2, num);
                while (GCD > 1) {
                    stk.pop_back();
                    long long LCM = num2 * num / GCD;
                    num = LCM;

                    if (!stk.empty()) {
                        num2 = stk.back();
                        GCD = gcd(num2, num);
                    } else {
                        break;
                    }
                }
                stk.push_back(num);
            } else {
                stk.push_back(num);
            }
        }
        return stk;
    }
};
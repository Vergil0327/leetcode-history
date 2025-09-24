class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        
        string ans = "";
        
        // Handle sign
        if ((numerator > 0) ^ (denominator > 0)) {
            ans += "-";
        }
        
        // Use long long to prevent overflow
        long long dividend = abs((long long)numerator);
        long long divisor = abs((long long)denominator);
        
        // Integer part
        ans += to_string(dividend / divisor);
        dividend %= divisor;
        
        if (dividend == 0) return ans;
        
        // Decimal part
        ans += ".";
        unordered_map<long long, int> seen;
        
        while (dividend != 0) {
            if (seen.count(dividend)) {
                // Found repeating cycle
                int pos = seen[dividend];
                ans.insert(pos, "(");
                ans += ")";
                return ans;
            }
            
            seen[dividend] = ans.size();
            dividend *= 10;
            ans += to_string(dividend / divisor);
            dividend %= divisor;
        }
        
        return ans;
    }
};
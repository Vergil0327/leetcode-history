#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size();
        int res = 0;
        for (int i = 0; i < n; i++) {
            int counts[26] = {0};
            int distinctCount = 0;
            int maxFreq = 0;
            int charsAtMaxFreq = 0;

            for (int j = i; j < n; j++) {
                int idx = s[j] - 'a';
                if (counts[idx] == 0) distinctCount++;
                counts[idx]++;
                
                if (counts[idx] > maxFreq) {
                    maxFreq = counts[idx];
                    charsAtMaxFreq = 1;
                } else if (counts[idx] == maxFreq) {
                    charsAtMaxFreq++;
                }

                // If number of chars having the max frequency 
                // equals the total number of distinct chars
                if (charsAtMaxFreq == distinctCount) {
                    res = max(res, j - i + 1);
                }
            }
        }
        return res;
    }
};
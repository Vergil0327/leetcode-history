#include <string>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        string res = "";
        map<char, int> count;
        for (const char& c : s) {
            count[c]++;
        }
        int n = target.size();

        string perm = "";
        auto dfs = [&](int i, bool strictGreater, auto self) -> bool {
            if (i >= n) {
                if (strictGreater) {
                    res = perm;
                    return true;
                }
                return false;
            }

            // Iterate over a copy of keys/counts or use a reference without mutating keys
            for (auto& [ch, cnt] : count) {
                if (cnt == 0) continue;

                // If not already strictly greater, we can only pick characters >= target[i]
                if (!strictGreater && ch < target[i]) continue;

                cnt--;
                perm.push_back(ch);

                bool nextStrict = strictGreater || (ch > target[i]);
                if (self(i + 1, nextStrict, self)) return true;

                // Backtrack
                perm.pop_back();
                cnt++;
            }
            return false;
        };

        dfs(0, false, dfs);
        return res;
    }
};

// Algorithm Approach:
// 1. Count character frequencies of 's'.
// 2. Try to match 'target' as long as possible (character by character).
// 3. Check if we can make a choice at position L (where L ranges from N-1 down to 0) by picking a character > target[L].
// 4. If valid, construct the prefix, append the strictly larger character, and fill the rest greedily with smallest available characters.

// Complexity:
// - Time Complexity: O(26 * N) = O(N), where N <= 300. Iterating down L takes O(N) steps, and finding the candidate takes O(26) steps.
// - Space Complexity: O(N) for string construction and O(26) frequency arrays.
class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.length();
        vector<int> total_cnt(26, 0);
        for (char c : s) total_cnt[c - 'a']++;

        // Find how many characters of target can be matched from index 0
        int matched_len = 0;
        vector<int> curr_cnt = total_cnt;
        for (int i = 0; i < n; ++i) {
            if (curr_cnt[target[i] - 'a'] > 0) {
                curr_cnt[target[i] - 'a']--;
                matched_len++;
            } else {
                break;
            }
        }

        // Try pivot L from matched_len down to 0
        for (int L = matched_len; L >= 0; --L) {
            if (L == n) continue;

            // Recompute available characters after matching target[0...L-1]
            vector<int> avail = total_cnt;
            for (int i = 0; i < L; ++i) {
                avail[target[i] - 'a']--;
            }

            // Find smallest char > target[L]
            int target_char = target[L] - 'a';
            int candidate = -1;
            for (int c = target_char + 1; c < 26; ++c) {
                if (avail[c] > 0) {
                    candidate = c;
                    break;
                }
            }

            if (candidate != -1) {
                string res = target.substr(0, L);
                res += (char)('a' + candidate);
                avail[candidate]--;

                // Append remaining available characters in sorted order
                for (int c = 0; c < 26; ++c) {
                    while (avail[c] > 0) {
                        res += (char)('a' + c);
                        avail[c]--;
                    }
                }
                return res;
            }
        }

        return "";
    }
};
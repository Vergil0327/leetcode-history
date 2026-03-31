#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.size(), m = str2.size();
        vector<char> word(n + m - 1);
        vector<bool> T(n + m - 1);

        for (int i=0; i<n; i++) {
            if (str1[i] == 'T') {
                for (int j=0; j<m; j++) {
                    if (word[i+j] && word[i+j] != str2[j]) return "";
                    word[i+j] = str2[j];
                    T[i+j] = true;
                }
            }
        }

        for (int i=0; i<n+m-1; i++) {
            if (!word[i]) {
                word[i] = 'a';
            }
        }

        for (int i=0; i<n; i++) {
            if (str1[i] == 'F') {
                bool diff = false;
                for (int j=0; j<m; j++) {
                    if (word[i+j] != str2[j]) {
                        diff = true;
                        break;
                    }
                }
                if (diff) continue;

                bool change = false;
                for (int j=m-1; j>=0; j--) {
                    if (T[i+j]) continue;

                    // Why changing to 'b' is enough
                    // Since str2 consists of lowercase letters, if a substring currently matches str2 and we change one character that isn't fixed by a 'T', we can always make it not match.

                    // If str2[j] was 'a', we change it to 'b'.

                    // If str2[j] was anything else, our default 'a' would have already made it different.

                    // Therefore, the only reason an 'F' substring matches str2 is if str2 itself has a specific pattern that matches our 'T's and 'a's. A single flip to 'b' (or the next available char) breaks the match.
                    if (word[i+j] == 'a') {
                        word[i+j] = 'b';
                    }

                    change = true;
                    break;
                }

                if (!change) {
                    return "";
                }
            }
        }

        string res(word.begin(), word.end());
        return res;
    }
};
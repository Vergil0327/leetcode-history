// ab -> ba
// ba -> ab
class Solution {
public:
    int check(string s, int x, int y, bool reverse) {
        string s1 = "ab", s2 = "ba";

        if (reverse) {
            swap(s1, s2);
            swap(x, y);
        }

        stack<char> st;
        int res = 0;
        for (char& c : s) {
            if (!st.empty() && st.top() == s1[0] && c == s1[1]) {
                st.pop();
                res += x;
            } else {
                st.push(c);
            }
        }

        stack<char> st2;
        while (!st.empty()) {
            char c = st.top();
            st.pop();

            if (!st2.empty() && st2.top() == s1[0] && c == s1[1]) {
                st2.pop();
                res += y;
            } else {
                st2.push(c);
            }
        }
        return res;
    }
    int maximumGain(string s, int x, int y) {
        return max(check(s, x, y, false), check(s, x, y, true));
    }
};



class Solution {
public:
    string decodeString(string s) {
        string ss;
        int cnt = 0;
        stack<tuple<string,int>> stk;
        for (char c : s) {
            if (isdigit(c)) {
                cnt = cnt*10 + (c-'0');
            } else if (c == '[') {
                stk.push(tuple<string,int> {ss, cnt});
                ss = "";
                cnt = 0;
            } else if (c == ']') {
                auto [prefix, times] = stk.top();
                stk.pop();

                string tmp = prefix;
                for (int i=0; i<times; i++) {
                    tmp += ss;
                }
                ss = tmp;
            } else {
                ss += c;
            }
        }
        
        return ss;
    }
};


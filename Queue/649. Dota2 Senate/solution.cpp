class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> R;
        queue<int> D;

        for (int i=0; i<senate.size(); i++) {
            if (senate[i] == 'R') {
                R.push(i);
            } else {
                D.push(i);
            }
        }

        // ban round by round
        int n = senate.size();
        while (!R.empty() && !D.empty()) {
            int i = R.front();
            R.pop();
            int j = D.front();
            D.pop();

            if (i < j) {
                // R ban D
                R.push(i+n); // keep it in queue because R still can be banned by R
            } else {
                // D ban R
                D.push(j+n);
            }
        }

        return R.empty() ? "Dire" : "Radiant";
    }
};

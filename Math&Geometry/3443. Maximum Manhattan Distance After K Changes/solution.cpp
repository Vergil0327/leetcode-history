class Solution {
public:
    int maxDistance(string s, int k) {
        int x=0, y=0;
        int N=0, S=0, E=0, W=0;
        int res = 0;
        for (int i=0; i < s.size(); i++) {
            if (s[i] == 'N') {
                y += 1;
                N += 1;
            } else if (s[i] == 'S') {
                y -= 1;
                S += 1;
            } else if (s[i] == 'E') {
                x += 1;
                E += 1;
            } else {
                x -= 1;
                W += 1;
            }

            int dist = abs(x) + abs(y);
            res = max(res, dist);
            
            int xx = min(E, W);
            int yy = min(N, S);
            res = max(res, dist + 2 * min(xx+yy, k)); // use k operations to replace minimum opposite direction and we can gain `2k` at most
        }
        return res;
    }
};
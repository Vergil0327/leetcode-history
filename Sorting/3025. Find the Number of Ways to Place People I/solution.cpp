class Solution {
public:
    int numberOfPairs(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [](const auto &a, const auto &b) {
            return a[0] == b[0] ? a[1] > b[1] : a[0] < b[0];
        });

        int res = 0, n = points.size();
        for (int i = 0; i < n; i++) {
            int y1 = points[i][1], last = -1;
            for (int j = i + 1; j < n; j++) {
                int y2 = points[j][1];
                if (y2 <= y1 && y2 > last) {
                    last = y2;
                    res++;
                }
            }
        }

        return res;
    }
};
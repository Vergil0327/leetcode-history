class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // be cautious: don't write `[](vector<int> a, vector<int> b) {...}`. otherwise, you'll copy vector in sorting and slow you program.
        sort(intervals.begin(), intervals.end(), [](vector<int>& a, vector<int>& b) {
            if (a[1] == b[1]) {
                return a[0] < b[0];
            }
            return a[1] < b[1];
        });

        int last = intervals[0][1];
        int res = 0;
        for (int i=1; i<intervals.size(); i++) {
            if (intervals[i][0] >= last) {
                last = intervals[i][1];
            } else {
                res++;
            }
        }
        return res;
    }
};

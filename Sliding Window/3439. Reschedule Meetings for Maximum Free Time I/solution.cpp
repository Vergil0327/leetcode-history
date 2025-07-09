class Solution {
public:
    int maxFreeTime(int eventTime, int k, vector<int>& startTime, vector<int>& endTime) {
        if (endTime.back() != eventTime) {
            endTime.push_back(eventTime);
            startTime.push_back(eventTime);
        }
        if (startTime[0] != 0) {
            startTime.insert(startTime.begin(), 0);
            endTime.insert(endTime.begin(), 0);
        }
        
        vector<int> space;
        for (int i=0; i<startTime.size()-1; i++) {
            space.push_back(startTime[i+1] - endTime[i]);
        }

        
        // sliding window merged k space at most
        int n = space.size();
        int res = 0;
        int duration = 0;
        int l=0, r=0;
        while (r < n) {
            duration += space[r];
            r++;

            while (l < r && r-l > k+1) {
                duration -= space[l];
                l++;
            }

            res = max(res, duration);
        }

        return res;
    }
};
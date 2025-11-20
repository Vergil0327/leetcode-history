#include <vector>
using namespace std;


class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const auto& lhs, const auto& rhs) {
            if (lhs[1] == rhs[1]) return lhs[0] > rhs[0];
            return lhs[1] < rhs[1];
        });

        vector<int> arr = {intervals[0][1]-1, intervals[0][1]};
        for (int i=1; i<intervals.size(); i++) {
            int l = intervals[i][0], r = intervals[i][1];
            int n = arr.size();
            if (l <= arr[n-2]) continue; // overlap 2
            if (l <= arr[n-1]) { // overlap 1
                arr.push_back(r);
            } else {
                arr.push_back(r-1);
                arr.push_back(r);
            }
        }
        return arr.size();
    }
};

// 但其實我們只在意前個interval, 所以我們可以用O(1) space就好

class Solution {
public:
    int intersectionSizeTwo(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](const auto& lhs, const auto& rhs) {
            if (lhs[1] == rhs[1]) return lhs[0] > rhs[0];
            return lhs[1] < rhs[1];
        });

        int prevL = intervals[0][1]-1, prevR = intervals[0][1];
        int count = 2;
        for (int i=1; i<intervals.size(); i++) {
            int l = intervals[i][0], r = intervals[i][1];
            
            if (l <= prevL) continue; // overlap 2
            if (l <= prevR) { // overlap 1
                prevL = prevR;
                prevR = r;
                count++;
            } else {
                prevL = r-1;
                prevR = r;
                count += 2;
            }
        }
        return count;
    }
};
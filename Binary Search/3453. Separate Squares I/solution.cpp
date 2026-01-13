#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>

using namespace std;

class Solution {
private:
    pair<double, double> check(vector<vector<int>>& squares, double t) {
        double sumUpper = 0, sumLower = 0;
        for (int i=0; i<squares.size(); i++) {
            long long y1 = squares[i][1], l = squares[i][2];
            long long y2 = y1 + l;

            if (t <= y1) {
                sumUpper += l * l;
            } else if (t >= y2) {
                sumLower += l * l;
            } else {
                sumUpper += abs(y2 - t) * l;
                sumLower += abs(t - y1) * l;
            }
        }

        return {sumLower, sumUpper};
    }
public:
    double separateSquares(vector<vector<int>>& squares) {
        double l = 0, r = 1e10;
        while (r - l >= 1e-5) {
            double mid = l + (r-l)/2;

            pair<double, double> sum = check(squares, mid);
            if (sum.first >= sum.second) {
                r = mid;
            } else {
                l = mid;
            }
        }

        return l;
    }
};
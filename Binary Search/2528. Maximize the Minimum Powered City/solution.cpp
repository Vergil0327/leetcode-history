#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    long long maxPower(vector<int>& stations, int R, int k) {
        int n = stations.size();
        
        
        auto check = [&](long long threshold) -> bool {
            vector<int> arr(n, 0);
            copy(stations.begin(), stations.end(), arr.begin());

            long long needStation = 0, power = 0;
            for (int i=0; i<R; i++) {
                power += arr[i];
            }

            for (int i=0; i<n; i++) {
                if (i+R < n) {
                    power += arr[i+R];
                }

                if (power < threshold) {
                    long long diff = threshold - power;
                    if (diff > k - needStation) return false;

                    power += diff;
                    needStation += diff;
                    arr[min(n-1, i+R)] += diff;
                }

                if (i-R >= 0) {
                    power -= arr[i-R];
                }
            }

            return needStation <= k;
        };

        long long l = *min_element(stations.begin(), stations.end()), r = accumulate(stations.begin(), stations.end(), 0LL) + k;;
        while (l < r) {
            long long mid = r - (r-l)/2;

            if (check(mid)) {
                l = mid;
            } else {
                r = mid-1;
            }
        }
        return l;
    }
};

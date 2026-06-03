#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, 
                           vector<int>& waterStartTime, vector<int>& waterDuration) {
        
        vector<pair<int, int>> land;
        for (size_t i = 0; i < landStartTime.size(); ++i) {
            land.push_back({landStartTime[i], landDuration[i]});
        }
        vector<pair<int, int>> water;
        for (size_t i = 0; i < waterStartTime.size(); ++i) {
            water.push_back({waterStartTime[i], waterDuration[i]});
        }

        // Sort both arrays primarily by their start times
        sort(land.begin(), land.end());
        sort(water.begin(), water.end());

        auto findEarliest = [](const vector<pair<int, int>>& arr1, const vector<pair<int, int>>& arr2) -> int {
            int n = arr2.size();
            
            // sufMinFinish[i] stores the minimum (start + duration) from index i to n-1
            vector<int> sufMinFinish(n + 1, 2e9); 
            for (int i = n - 1; i >= 0; --i) {
                sufMinFinish[i] = min(sufMinFinish[i + 1], arr2[i].first + arr2[i].second);
            }
            
            // preMinDuration[i] stores the minimum duration from index 0 to i
            vector<int> preMinDuration(n, 2e9);
            preMinDuration[0] = arr2[0].second;
            for (int i = 1; i < n; ++i) {
                preMinDuration[i] = min(preMinDuration[i - 1], arr2[i].second);
            }

            int ans = 2e9;
            for (const auto& item : arr1) {
                int t1 = item.first;
                int dur1 = item.second;
                int finish1 = t1 + dur1;

                // Binary search for the first ride in arr2 that opens AFTER or AT finish1
                auto it = lower_bound(arr2.begin(), arr2.end(), make_pair(finish1, 0), 
                                      [](const pair<int, int>& elem, const pair<int, int>& target) {
                                          return elem.first < target.first;
                                      });
                
                int j = distance(arr2.begin(), it);

                // Case 1: The second ride starts after or exactly when the first ride ends
                if (j < n) {
                    ans = min(ans, sufMinFinish[j]);
                }
                
                // Case 2: The second ride is already open when the first ride ends
                if (j > 0) {
                    ans = min(ans, finish1 + preMinDuration[j - 1]);
                }
            }
            return ans;
        };
        
        return min(findEarliest(land, water), findEarliest(water, land));
    }
};

class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        int earliestLand = landStartTime[0] + landDuration[0];
        for(int i = 1; i < landStartTime.size(); ++i){
            if(earliestLand > landStartTime[i] + landDuration[i]){
                earliestLand = landStartTime[i] + landDuration[i];
            }
        }

        int earliestWater = waterStartTime[0] + waterDuration[0];
        for(int i = 1; i < waterStartTime.size(); ++i){
            if(earliestWater > waterStartTime[i] + waterDuration[i]){
                earliestWater = waterStartTime[i] + waterDuration[i];
            }
        }

        int minTime = INT_MAX;

        // water first
        for(int i = 0; i < landStartTime.size(); ++i){
            int time;
            if(earliestWater < landStartTime[i]){
                time = landStartTime[i] + landDuration[i];
            } else {
                time = earliestWater + landDuration[i];
            }
            if(time < minTime){
                minTime = time;
            }
        }

        // land first
        for(int i = 0; i < waterStartTime.size(); ++i){
            int time;
            if(earliestLand < waterStartTime[i]){
                time = waterStartTime[i] + waterDuration[i];
            } else {
                time = earliestLand + waterDuration[i];
            }
            if(time < minTime) {
                minTime = time;
            }
        }

        return minTime;
    }
};
class Solution {
public:
    vector<int> avoidFlood(vector<int>& rains) {
        int n = rains.size();
        vector<int> ans(n, -1);
        
        vector<int> dry;
        unordered_map<int,int> rain;
        for (int i=0; i<n; i++) {
            if (rains[i] == 0) {
                dry.push_back(i);
                continue;
            }

            if (rain.find(rains[i]) == rain.end()) {
                rain[rains[i]] = i;
            } else {
                int day = rain[rains[i]];
                auto it = upper_bound(dry.begin(), dry.end(), day);
                if (it == dry.end()) return {};

                ans[*it] = rains[i];
                dry.erase(it);
                rain[rains[i]] = i;
            }
        }

        for (auto& idx : dry) {
            ans[idx] = 1;
        }

        return ans;
    }
};
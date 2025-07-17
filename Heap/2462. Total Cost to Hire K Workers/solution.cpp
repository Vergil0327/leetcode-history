using pii = pair<int,int>;

class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        /*
        Core Logic: "Should a have LOWER priority than b?"
        The compare function returns true if the first element should have lower priority than the second element.
        Return Values:

        return true → a has lower priority than b
        return false → a has higher or equal priority than b
        */
        auto cmp = [](pii a, pii b) {
            if (a.first == b.first) {
                return a.second > b.second;
            }
            return a.first > b.first;
        };
        priority_queue<pii, vector<pii>, decltype(cmp)> min_heap; // or: priority_queue<pii, vector<pii>, greater<pii>> min_heap;
        int l=0, r=costs.size()-1;
        for (int i = 0; i < candidates && l <= r; i++) {
            min_heap.push({costs[l], l});
            l++;
        }
        for (int i = 0; i < candidates && l <= r; i++) {
            min_heap.push({costs[r], r});
            r--;
        }
        
        long long res = 0;
        for (int i=0; i<k; i++) {
            int cost = min_heap.top().first;
            int idx = min_heap.top().second;
            min_heap.pop();
            res += cost;
            
            if (l <= r) {
                if (idx < l) {
                    min_heap.push({costs[l], l});
                    l++;
                } else if (idx > r) {
                    min_heap.push({costs[r], r});
                    r--;
                }
            }
        }
        return res;
    }
};
class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        sort(potions.begin(), potions.end());
        int n = spells.size();
        vector<int> result(n, 0);

        for (int i=0; i<n; i++) {
            // minimum value potion needed
            // spells[i] * potions[j] >= success
            // potions[j] >= ceil((1.0 * success) / spells[i]);
            // use STL lower_bound to find the first valid potion
            auto it = lower_bound(potions.begin(), potions.end(), ceil(1.0*success/spells[i]));
            result[i] = potions.end() - it;
        }

        return result;
    }
};

class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        int n = potions.size();
        sort(potions.begin(), potions.end());

        vector<int> res;
        for (auto& spell : spells) {
            int l=0, r=n;
            while (l < r) {
                int mid = l + (r-l)/2;
                long long product = (long long)spell * potions[mid];
                if (product >= success) {
                    r = mid;
                } else {
                    l = mid+1;
                }
            };
            res.push_back(n - l);
        }
        return res;
    }
};
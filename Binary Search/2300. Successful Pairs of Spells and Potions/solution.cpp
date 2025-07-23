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
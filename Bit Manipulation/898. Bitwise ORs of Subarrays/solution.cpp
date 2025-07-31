class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        unordered_set<int> ans;
        unordered_set<int> curr, next;
        
        for (int& num : arr) {
            next = {num};
            for (int prev : curr) {
                next.insert(prev | num);
            }
            curr = next;

            ans.insert(curr.begin(), curr.end());
        }

        return ans.size();
    }
};
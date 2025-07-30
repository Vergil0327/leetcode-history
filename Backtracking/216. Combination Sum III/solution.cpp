class Solution {
public:
    void dfs(int d, int k, int n, vector<int> curr, vector<vector<int>>& res) {
        if (k==0 && n== 0) {
            res.push_back(curr);
            return;
        }
        if (k <= 0 || n <= 0) {
            return;
        }
        
        for (int i=d+1; i<10; i++) {
            curr.push_back(i);
            dfs(i, k-1, n-i, curr, res);
            curr.pop_back();
        }
        return;
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<vector<int>> res;
        dfs(0, k, n, {}, res);
        return res;
    }
};
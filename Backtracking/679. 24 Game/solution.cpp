class Solution {
public:
    bool judgePoint24(vector<int>& cards) {
        sort(cards.begin(), cards.end());
                
        double epsilon = 1e-6;
        do 
        {
            unordered_set<double> results = dfs(cards, 0, 3);
            for (auto res:results) {
                if (abs(res-24) < epsilon) return true;
            }
        } while (next_permutation(cards.begin(), cards.end()));

        return false;
    }
    
    unordered_set<double> dfs(vector<int> &nums, int l, int r) {
        if (l==r) return {(double) nums[l]};
        
        unordered_set<double>res;
        
        for (int i=l; i<r; i++) {
            unordered_set<double>left = dfs(nums,l,i);
            unordered_set<double>right = dfs(nums,i+1,r);
            for (double x:left)
                for (double y:right) {
                    res.insert(x+y);
                    res.insert(x-y);
                    res.insert(x*y);
                    if (y!=0) {
                        res.insert(x/y);
                    }
                }
        }
        return res;
    }
};
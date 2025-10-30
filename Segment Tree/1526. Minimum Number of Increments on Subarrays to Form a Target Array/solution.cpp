// Greedy: check adjacent difference
class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        int n = target.size();
        int res = 0, currentHeight = 0;
        for (int i=0; i<n; i++) {
            if (target[i] > currentHeight) {
                res += target[i] - currentHeight;
            }

            currentHeight = target[i];
        }
        return res;
    }
};

// segment tree
class Solution {
private:
    class SegTreeNode
    {
        public:
        SegTreeNode* left = NULL;
        SegTreeNode* right = NULL;
        int start, end;
        int info, pos;  // the maximum value of the range
        bool tag;

        
        SegTreeNode(int a, int b, vector<int>& val)  // init for range [a,b] with the same-size array val
        {                 
            tag = 0;
            info = 0;
            start = a, end = b;
            if (a==b)
            {
                info = val[a];
                pos = a;
                return;
            }        
            int mid = (a+b)/2;
            if (left==NULL)
            {
                left = new SegTreeNode(a, mid, val);
                right = new SegTreeNode(mid+1, b, val);            
                if (left->info < right->info) {
                    info = left->info;
                    pos = left->pos;
                } else {
                    info = right->info;
                    pos = right->pos;
                }
            }        
        } 
        
        void pushDown()
        {
            if (tag==1 && left)
            {
                left->info = info;
                right->info = info;
                left->pos = pos;
                right->pos = pos;
                left->tag = 1;
                right->tag = 1;
                tag = 0;
            }        
        } 
        
        pair<int,int> queryRange(int a, int b)     // query the maximum value within range [a,b]
        {
            if (b < start || a > end )
            {
                return {INT_MAX/2,-1};  // check with your own logic
            }
            if (a <= start && end <=b)
            {
                return {info,pos};  // check with your own logic
            }          
            
            if (left)
            {
                pushDown();   
                auto L = left->queryRange(a, b);
                auto R = right->queryRange(a, b);

                if (L.first < R.first) {
                    return L;
                } else {
                    return R;
                }
            }
            
            return {info, pos};   // should not reach here
        }  

    };
public:
    int minNumberOperations(vector<int>& target) {
        int n = target.size();
        SegTreeNode* root = new SegTreeNode(0, n-1, target);
        
        function<int(int,int,int)> dfs = [&](int l, int r, int base) -> int {
            if (l > r) return 0;
            if (l == r) return target[l] - base;

            auto [val, pos] = root->queryRange(l, r);

            int sum = val - base;
            sum += dfs(l, pos-1, val);
            sum += dfs(pos+1, r, val);
            return sum;
        };

        return dfs(0, n-1, 0);
    }
};

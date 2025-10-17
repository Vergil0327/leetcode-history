class Solution {
public:
    int maxPartitionsAfterOperations(string s, int k) {
        int n = s.size();
        map<tuple<int,int,int>, int> memo;
        
        function<int(int, int, int)> dfs = [&](int i, int states, int changed) -> int {
            if (i >= n) return 1; // Count the last partition
            
            auto key = make_tuple(i, states, changed);
            if (memo.count(key)) return memo[key];
            
            int j = s[i] - 'a';
            int res = 0;
            
            // Option 1: Don't change current character
            int new_states = states | (1 << j);
            if (__builtin_popcount(new_states) > k) {
                res = max(res, dfs(i + 1, 1 << j, changed) + 1);
            } else {
                res = max(res, dfs(i + 1, new_states, changed));
            }
            
            // Option 2: Change current character (if not changed yet)
            if (!changed) {
                for (int c = 0; c < 26; c++) {
                    if (c == j) continue;
                    new_states = states | (1 << c);
                    if (__builtin_popcount(new_states) > k) {
                        res = max(res, dfs(i + 1, 1 << c, 1) + 1);
                    } else {
                        res = max(res, dfs(i + 1, new_states, 1));
                    }
                }
            }
            
            return memo[key] = res;
        };
        
        return dfs(0, 0, 0);
    }
};

// unordered_map need custom hash for tuple
class Solution {
public:
    unordered_map<long long, int> memo;
    int solve(int i, string& s, int mask, bool canchange, int k){
        if(i==s.size()){
            return 0;
        }
        long long key = ((long long)i<<27 | (long long)mask<<1 | (canchange ? 1LL : 0LL));

        if(memo.count(key))
            return memo[key];

        int bit = 1<<(s[i]-'a');
        int newmask = bit | mask;
        int best = 0;

        // 1. take actual character
        if(__builtin_popcount(newmask) > k)
            best = 1 + solve(i+1, s, bit, canchange, k);
        else
            best = solve(i+1, s, newmask, canchange, k);
        //2. change the character
        if(canchange){
            for(int c = 0; c<26;c++){
                int bit2 = 1<<c;
                int mask2 = bit2 | mask;
                int candidates;
                if(__builtin_popcount(mask2) > k)
                    candidates = 1 + solve(i+1, s, bit2, false, k);
                else
                    candidates = solve(i+1, s, mask2, false, k);
                best = max(best, candidates);
            }
        }

        memo[key] = best;
        return best;
    }

    int maxPartitionsAfterOperations(string s, int k) {
        return 1 + solve(0, s, 0, true, k);
    }
};

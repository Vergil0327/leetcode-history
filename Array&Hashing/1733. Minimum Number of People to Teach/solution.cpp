class Solution {
public:
    int minimumTeachings(int n, vector<vector<int>>& languages, vector<vector<int>>& friendships) {
        int m = languages.size();

        unordered_map<int, unordered_set<int>> lang2people;
        for (int i=1; i<=m; i++) {
            for (int lang : languages[i-1]) {
                lang2people[lang].insert(i);
            }
        }

        vector<int> need_learn(m+1, false);
        for (auto& friendship : friendships) {
            bool can_communicate = false;
            for (int lang = 1; lang <= n; lang++) {
                if (lang2people[lang].count(friendship[0]) && lang2people[lang].count(friendship[1])) {
                    can_communicate = true;
                    break;
                }
            }

            if (!can_communicate) {
                need_learn[friendship[0]] = true;
                need_learn[friendship[1]] = true;
            }
        }


        int res = m;
        for (int lang=1; lang<=n; lang++) {
            int teached = 0;
            
            for (int i=1; i<=m; i++) {
                if (need_learn[i] && !lang2people[lang].count(i)) teached++;
            }
            res = min(res, teached);
        }
        return res;
    }
};
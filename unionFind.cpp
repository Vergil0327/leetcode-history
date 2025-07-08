class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();

        vector<int> parent(n, 0);
        iota(parent.begin(), parent.end(), 0);

        vector<int> rank(n, 1);

        function<int(int)> find = [&](int x) -> int {
            if (parent[x] != x) {
                parent[x] = find(parent[x]);
            }
            return parent[x];
        };

        auto union_set = [&](int x, int y) -> bool {
            int px=find(x), py=find(y);
            if (px == py) return false;

            if (rank[px] < rank[py]) {
                swap(px, py);
            }
            parent[py] = px;
            rank[px] += rank[py];
            return true;
        };

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (isConnected[i][j]) {
                    union_set(i, j);
                }
            }
        }

        unordered_set<int> count;
        for (auto p : parent) {
            count.insert(find(p));
        }
        return count.size();
    }
};

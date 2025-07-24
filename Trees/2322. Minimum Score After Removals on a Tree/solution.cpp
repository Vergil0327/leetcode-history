class Solution {
    unordered_set<int> graph[1003]; // Adjacency list
    vector<int> nums;
    int xorTotal = 0;

public:
    int getXor(int node, int parent) {
        int xorResult = nums[node]; // Changed variable name to avoid potential issues
        for (int child : graph[node]) {
            if (child == parent) continue; // Fixed: Semicolon instead of colon
            xorResult ^= getXor(child, node); // Fixed: Semicolon instead of colon
        }
        return xorResult;
    }

    int check(int node, int keep) {
        int xorNode = getXor(node, node);
        int xorKeep = xorTotal ^ xorNode;

        int res = INT_MAX;
        dfs(node, node, res, xorNode, xorKeep);
        return res;
    }

    int dfs(int node, int parent, int& res, int xorTotal, int xorKeep) {
        int total = nums[node];

        for (int nxt : graph[node]) {
            if (nxt == parent) continue;

            int xorChild = dfs(nxt, node, res, xorTotal, xorKeep);
            int other = xorTotal ^ xorChild;

            int mx = max(other, max(xorChild, xorKeep));
            int mn = min(other, min(xorChild, xorKeep));
            res = min(res, mx - mn);

            total ^= xorChild;
        }
        return total;
    }

    int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
        this->nums = nums;

        for (auto num : nums) {
            xorTotal ^= num;
        }

        for (auto& edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].insert(v);
            graph[v].insert(u);
        }

        int res = INT_MAX;
        for (auto& edge : edges) { // Fixed: Use reference
            int u = edge[0], v = edge[1]; // Fixed: Use edge[0] and edge[1]

            // First cut
            graph[u].erase(v);
            graph[v].erase(u);

            int res1 = check(u, v);
            int res2 = check(v, u);

            res = min(res, min(res1, res2));

            // Restore the edge
            graph[u].insert(v);
            graph[v].insert(u);
        }

        return res;
    }
};
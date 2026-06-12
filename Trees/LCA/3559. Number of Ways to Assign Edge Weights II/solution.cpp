#include <vector>
#include <algorithm>

using namespace std;

class Solution {
private:
    int n;
    int LOGN;
    vector<int> depth;
    vector<vector<int>> up; // up[i][j] stores the (2^j)-th ancestor of node i

    // 1. Compute depths and the immediate parents (2^0 ancestor) for binary lifting
    void dfs(int node, int parent, int d, const vector<vector<int>>& graph) {
        depth[node] = d;
        up[node][0] = parent;
        
        // Fill the jump table for binary lifting
        for (int i = 1; i < LOGN; ++i) {
            if (up[node][i - 1] != -1) {
                up[node][i] = up[up[node][i - 1]][i - 1];
            } else {
                up[node][i] = -1;
            }
        }

        for (int nxt : graph[node]) {
            if (nxt != parent) {
                dfs(nxt, node, d + 1, graph);
            }
        }
    }

    // 2. Query Lowest Common Ancestor in O(log N) time
    int getLCA(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);

        // Bring both nodes to the same depth level
        int diff = depth[u] - depth[v];
        for (int i = 0; i < LOGN; ++i) {
            if ((diff >> i) & 1) {
                u = up[u][i];
            }
        }

        if (u == v) return u;

        // Lift both nodes simultaneously right below their common ancestor
        for (int i = LOGN - 1; i >= 0; --i) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }

        return up[u][0];
    }

    // 3. Fast Modular Exponentiation
    long long power(long long base, long long exp, long long mod) {
        long long res = 1;
        base %= mod;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % mod;
            base = (base * base) % mod;
            exp /= 2;
        }
        return res;
    }

public:
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        n = edges.size() + 1;
        LOGN = 0;
        while ((1 << LOGN) <= n) LOGN++;

        // Keep graph 1-indexed to stay synchronized with Leetcode's inputs
        vector<vector<int>> graph(n + 1);
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        depth.assign(n + 1, 0);
        up.assign(n + 1, vector<int>(LOGN, -1));

        // Root the tree at node 1 (Parent of root is set to -1)
        dfs(1, -1, 0, graph);

        vector<int> ans;
        ans.reserve(queries.size());
        long long MOD = 1000000007;

        for (const auto& query : queries) {
            int u = query[0], v = query[1];
            
            if (u == v) {
                ans.push_back(0); // 0 edges mean a path sum of 0 (always even)
            } else {
                int lca_node = getLCA(u, v);
                // Number of edges along the simple path between u and v
                int path_edges = (depth[u] - depth[lca_node]) + (depth[v] - depth[lca_node]);
                
                // Using Version I's core identity math: 2^(L-1) % MOD
                ans.push_back(power(2, path_edges - 1, MOD));
            }
        }

        return ans;
    }
};
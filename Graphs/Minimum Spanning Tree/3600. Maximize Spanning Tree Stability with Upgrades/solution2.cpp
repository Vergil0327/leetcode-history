#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <queue>

using namespace std;

struct DSU {
    vector<int> p, r;
    int components;
    DSU(int n): p(n), r(n, 0), components(n) {
        iota(p.begin(), p.end(), 0);
    }
    int find(int x) {
        return p[x] == x ? x : p[x] = find(p[x]);
    }
    bool unite(int a, int b) {
        a = find(a); b = find(b);
        if (a == b) return false;
        if (r[a] < r[b]) swap(a, b);
        p[b] = a;
        if (r[a] == r[b]) ++r[a];
        components--; // Track connectivity in O(1)
        return true;
    }
};

class Solution {
    // We store these as members to avoid passing them repeatedly
    int min_must_s = 2e9 + 7;
    bool has_must = false;

    bool check(int target, int n, int k, const vector<vector<int>>& edges) {
        // 1. Mandatory Bottleneck Check
        if (has_must && target > min_must_s) return false;

        DSU uf(n);
        vector<pair<int, int>> potential_upgrades;

        // 2. First Pass: Mandatory and Strong Optional Edges
        for (const auto& e : edges) {
            int u = e[0], v = e[1], s = e[2], must = e[3];
            if (must) {
                // We already checked cycles in maxStability, so just unite
                uf.unite(u, v);
            } else {
                if (s >= target) {
                    uf.unite(u, v);
                } else if (s * 2 >= target) {
                    potential_upgrades.push_back({u, v});
                }
            }
        }

        // 3. Second Pass: Greedy Upgrade with K budget
        for (const auto& e : potential_upgrades) {
            if (uf.components == 1) break;
            if (k > 0 && uf.unite(e.first, e.second)) {
                k--;
            }
        }

        return uf.components == 1;
    }

public:
    int maxStability(int n, vector<vector<int>>& edges, int k) {
        DSU initial_check(n);
        int max_val = 0;

        // 4. Initial Hardware Check: Detect Mandatory Cycles
        // This is where your test case [0,1,1,1],[1,2,1,1],[2,0,1,1] returns -1
        for (const auto& edge : edges) {
            max_val = max(max_val, edge[2] * 2);
            if (edge[3]) {
                has_must = true;
                min_must_s = min(min_must_s, edge[2]);
                if (!initial_check.unite(edge[0], edge[1])) {
                    return -1; // Mandatory edges formed a cycle
                }
            }
        }

        // 5. Final Connectivity Check: Is it even possible to connect all nodes?
        DSU total_check = initial_check;
        for (const auto& edge : edges) {
            if (!edge[3]) total_check.unite(edge[0], edge[1]);
        }
        if (total_check.components > 1) return -1;

        // 6. Binary Search
        int l = 0, r = max_val;
        int ans = -1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (check(mid, n, k, edges)) {
                ans = mid;
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return ans;
    }
};

struct UnionFind {
    vector<int> parent, rank;
    UnionFind(int n) : parent(n), rank(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    bool unite(int x, int y) {
        int px = find(x), py = find(y);
        if (px == py) return false;
        if (rank[px] < rank[py]) swap(px, py);
        parent[py] = px;
        rank[px] += rank[py];
        return true;
    }
};

class Solution {
public:
    int maxStability(int n, vector<vector<int>>& edges, int k) {
        UnionFind initial_uf(n);
        int min_must_s = 2e9 + 7; // Use a large value for inf
        bool has_must = false;

        // 1. Pre-process mandatory edges
        for (const auto& e : edges) {
            if (e[3]) {
                has_must = true;
                min_must_s = min(min_must_s, e[2]);
                if (!initial_uf.unite(e[0], e[1])) return -1; // Cycle in must-have edges
            }
        }

        auto check = [&](int target) {
            // Stability cannot exceed the weakest mandatory link
            if (has_must && target > min_must_s) return false;

            // Copy initial state (mandatory edges already connected)
            UnionFind uf = initial_uf;
            vector<pair<int, int>> upgrade;

            for (const auto& e : edges) {
                if (e[3]) continue;
                if (e[2] >= target) {
                    uf.unite(e[0], e[1]);
                } else if (e[2] * 2 >= target) {
                    upgrade.push_back({e[0], e[1]});
                }
            }

            int remaining_k = k;
            for (const auto& p : upgrade) {
                if (remaining_k > 0 && uf.find(p.first) != uf.find(p.second)) {
                    uf.unite(p.first, p.second);
                    remaining_k--;
                }
            }

            // Check if all nodes are in the same component
            int root = uf.find(0);
            for (int i = 1; i < n; i++) {
                if (uf.find(i) != root) return false;
            }
            return true;
        };

        // Binary Search
        int l = -1, r = 0;
        for (const auto& e : edges) r = max(r, e[2] * 2);

        while (l < r) {
            int mid = r - (r - l) / 2;
            if (check(mid)) l = mid;
            else r = mid - 1;
        }

        return l;
    }
};
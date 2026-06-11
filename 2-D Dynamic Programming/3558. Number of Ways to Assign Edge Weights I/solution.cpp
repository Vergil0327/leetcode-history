#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <map>

using namespace std;
using LL = long long;
using vll = vector<LL>;


/*
Let $L$ be the number of edges in the path from node 1 to $x$ (which is exactly maxDepth).
Each edge can have a weight of either 1 (odd) or 2 (even).
We want the total sum of the $L$ edges to be odd.

For the total sum to be odd, we must choose an odd number of edges to have a weight of 1. The remaining edges will have a weight of 2.
By standard combinatorial properties, if you have a path of length $L \ge 1$ and each edge has 2 choices (one even, one odd), exactly half of all possible assignments will result in an odd sum, and the other half will be even!

$$\text{Total Assignments} = 2^L$$
$$\text{Valid Odd Assignments} = \frac{2^L}{2} = 2^{L-1}$$
*/
class Solution {
public:
    int depth(int node, int prev, vector<vector<int>>& graph) {
        int res = 0;
        for (const auto& nxt : graph[node]) {
            if (nxt == prev) continue;
            res = max(res, depth(nxt, node, graph)+1);
        }
        return res;
    }
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
    int assignEdgeWeights(vector<vector<int>>& edges) {
        vector<vector<int>> graph(edges.size()+1);
        for (const auto& edge: edges) {
            int u = edge[0]-1, v = edge[1]-1;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        int maxDepth = depth(0, -1, graph);
        return power(2, maxDepth-1, 1000000007);
    }
};
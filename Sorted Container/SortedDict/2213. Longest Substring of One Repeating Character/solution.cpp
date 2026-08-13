#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
private:
    struct Node {
        int max_len;
        int prefix_len;
        char prefix_char;
        int suffix_len;
        char suffix_char;
        int length;
    };

    vector<Node> tree;

    Node merge(const Node& left, const Node& right) {
        Node res;
        res.length = left.length + right.length;

        // Default prefix initialization
        res.prefix_char = left.prefix_char;
        res.prefix_len = left.prefix_len;
        if (left.prefix_len == left.length && left.suffix_char == right.prefix_char) {
            res.prefix_len = left.length + right.prefix_len;
        }

        // Default suffix initialization
        res.suffix_char = right.suffix_char;
        res.suffix_len = right.suffix_len;
        if (right.suffix_len == right.length && right.prefix_char == left.suffix_char) {
            res.suffix_len = right.length + left.suffix_len;
        }

        // Calculate max length
        res.max_len = max(left.max_len, right.max_len);
        if (left.suffix_char == right.prefix_char) {
            res.max_len = max(res.max_len, left.suffix_len + right.prefix_len);
        }

        return res;
    }

    void build(int node, int start, int end, const string& s) {
        if (start == end) {
            tree[node] = {1, 1, s[start], 1, s[start], 1};
            return;
        }
        int mid = start + (end - start) / 2;
        build(2 * node, start, mid, s);
        build(2 * node + 1, mid + 1, end, s);
        tree[node] = merge(tree[2 * node], tree[2 * node + 1]);
    }

    void update(int node, int start, int end, int idx, char ch) {
        if (start == end) {
            tree[node] = {1, 1, ch, 1, ch, 1};
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) {
            update(2 * node, start, mid, idx, ch);
        } else {
            update(2 * node + 1, mid + 1, end, idx, ch);
        }
        tree[node] = merge(tree[2 * node], tree[2 * node + 1]);
    }

public:
    vector<int> longestRepeating(string s, string queryCharacters, vector<int>& queryIndices) {
        int n = s.length();
        int k = queryIndices.size();
        tree.resize(4 * n);

        build(1, 0, n - 1, s);

        vector<int> ans(k);
        for (int i = 0; i < k; ++i) {
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i]);
            ans[i] = tree[1].max_len;
        }

        return ans;
    }
};
#include <vector>
#include <cmath>
#include <algorithm> // for std::max

class SegmentTree {
private:
    std::vector<int> st; // Segment tree array
    int n;               // Size of the leaf nodes (padded to power of 2)
    
    // Helper function to update a node and propagate changes upward
    void update(int i, int val) {
        i += n; // Move to leaf node
        st[i] = val;
        while (i > 1) { // Propagate up to root
            i >>= 1; // Move to parent
            st[i] = std::max(st[i * 2], st[i * 2 + 1]);
        }
    }

public:
    SegmentTree(const std::vector<int>& leaf_nodes) {
        int size = leaf_nodes.size();
        n = 1 << static_cast<int>(std::ceil(std::log2(size))); // Next power of 2
        st.assign(2 * n, 0); // Initialize array with zeros
        // Copy leaf nodes
        for (int i = 0; i < size; ++i) {
            st[i + n] = leaf_nodes[i];
        }
        // Build the tree bottom-up
        for (int i = n - 1; i >= 1; --i) {
            st[i] = std::max(st[i * 2], st[i * 2 + 1]);
        }
    }

    // Find the leftmost index where st[index] >= target
    int find(int target) {
        if (st[1] < target) return -1; // Root value is less than target
        int i = 1;
        while (i < n) {
            if (st[i * 2] >= target) {
                i = i * 2; // Go left
            } else {
                i = i * 2 + 1; // Go right
            }
        }
        return i - n; // Convert to leaf index
    }

    // Update the value at index i to val
    void set(int i, int val) {
        update(i, val);
    }
};

// example:
class Solution {
public:
    int numOfUnplacedFruits(std::vector<int>& fruits, std::vector<int>& baskets) {
        SegmentTree seg(baskets);
        int res = 0;
        for (int fruit : fruits) {
            int node_idx = seg.find(fruit);
            if (node_idx != -1) {
                seg.set(node_idx, -1); // Mark basket as used
            } else {
                res++; // Fruit cannot be placed
            }
        }
        return res;
    }
};

class SegTreeNode {
public:
    int start, end; // Range [start, end] covered by this node
    int info;       // Maximum value in the range
    int index;      // Index of the leftmost maximum value
    int lazy;       // Lazy tag for pending updates
    bool has_lazy;  // Flag to indicate if lazy tag is set
    SegTreeNode *left, *right;

    // Constructor for leaf nodes or recursive nodes
    SegTreeNode(int a, int b, const std::vector<int>& vals) 
        : start(a), end(b), left(nullptr), right(nullptr), lazy(0), has_lazy(false) {
        if (a == b) {
            // Leaf node: set value and index
            info = vals[a];
            index = a;
        } else {
            // Internal node: recursively build children
            int mid = (a + b) / 2;
            left = new SegTreeNode(a, mid, vals);
            right = new SegTreeNode(mid + 1, b, vals);
            // Set info as max of children
            info = std::max(left->info, right->info);
            // Inherit index from left child (leftmost maximum)
            index = (left->info >= right->info) ? left->index : right->index;
        }
    }

    // Destructor to free memory
    ~SegTreeNode() {
        delete left;
        delete right;
    }

    // Push down lazy updates to children
    void pushDown() {
        if (!has_lazy) return; // No lazy update to push
        if (start != end) { // Not a leaf node
            // Propagate lazy value to children
            left->info = lazy;
            right->info = lazy;
            left->lazy = lazy;
            right->lazy = lazy;
            left->has_lazy = true;
            right->has_lazy = true;
            // Update children's index to start of their range
            left->index = left->start;
            right->index = right->start;
        }
        // Clear lazy tag
        has_lazy = false;
        lazy = 0;
    }

    // Update range [l, r] to value val
    void updateRange(int l, int r, int val) {
        // Apply pending lazy updates before processing
        pushDown();

        // No overlap
        if (l > end || r < start) return;

        // Complete overlap
        if (l <= start && end <= r) {
            info = val;
            lazy = val;
            has_lazy = true;
            index = start; // Set index to leftmost position in range
            return;
        }

        // Partial overlap: recurse to children
        left->updateRange(l, r, val);
        right->updateRange(l, r, val);
        // Update info and index (check your own logic)
        info = std::max(left->info, right->info);
        index = (left->info >= right->info) ? left->index : right->index;
    }

    // Find the leftmost index where info >= target
    // (check your own logic)
    int find(int target) {
        // Apply pending lazy updates
        pushDown();

        if (info < target) return -1; // No valid value in this subtree
        if (start == end) {
            // Leaf node: return its index
            return index;
        }
        // Check left child first (to get leftmost index)
        if (left->info >= target) {
            return left->find(target);
        }
        return right->find(target);
    }
};

// example
class Solution {
public:
    int numOfUnplacedFruits(std::vector<int>& fruits, std::vector<int>& baskets) {
        // Initialize segment tree with baskets
        SegTreeNode* root = new SegTreeNode(0, baskets.size() - 1, baskets);
        int res = 0;
        for (int fruit : fruits) {
            int node_idx = root->find(fruit);
            if (node_idx != -1) {
                // Found a suitable basket: mark it as used (point update)
                root->updateRange(node_idx, node_idx, -1);
            } else {
                // No suitable basket: increment result
                res++;
            }
        }
        // Clean up memory
        delete root;
        return res;
    }
};

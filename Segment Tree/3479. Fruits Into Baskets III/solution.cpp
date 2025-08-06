/* vector-based */

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

/* tree-based (recursive) */
#include <vector>
#include <algorithm> // for std::max

class SegTreeNode {
public:
    int start, end; // Range [start, end] covered by this node
    int info;       // Maximum value in the range
    int index;      // Index of the leftmost maximum value (for leaf nodes)
    SegTreeNode *left, *right;

    // Constructor for leaf nodes or recursive nodes
    // The colon (:) introduces an initializer list, which is used to initialize the member variables of the class before the constructor's body (the {} part) executes.
    // Each entry in the initializer list is of the form member_name(value), where:

    // member_name is a class member variable (e.g., start, end, left, right).
    // value is the value or expression used to initialize that member.

    // start(l): Initializes the member variable start (an int) with the parameter l (an int).
    // end(r): Initializes the member variable end (an int) with the parameter r (an int).
    // left(nullptr): Initializes the member variable left (a SegTreeNode*) to nullptr.
    // right(nullptr): Initializes the member variable right (a SegTreeNode*) to nullptr.
    SegTreeNode(int l, int r, const std::vector<int>& vals) : start(l), end(r), left(nullptr), right(nullptr) {
        if (l == r) {
            // Leaf node: set value and index
            info = vals[l];
            index = l;
        } else {
            // Internal node: recursively build children
            int mid = (l + r) / 2;
            left = new SegTreeNode(l, mid, vals);
            right = new SegTreeNode(mid + 1, r, vals);
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

    // Update the value at index i to val
    void update(int i, int val) {
        if (start == end && start == i) {
            // Leaf node: update value
            info = val;
            return;
        }
        if (i < start || i > end) return; // Out of range
        // Recursively update the appropriate child
        if (i <= (start + end) / 2) {
            left->update(i, val);
        } else {
            right->update(i, val);
        }
        // Update info and index
        info = std::max(left->info, right->info);
        index = (left->info >= right->info) ? left->index : right->index;
    }

    // Find the leftmost index where info >= target
    int find(int target) {
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

class Solution {
public:
    int numOfUnplacedFruits(std::vector<int>& fruits, std::vector<int>& baskets) {
        // Initialize segment tree with baskets
        SegTreeNode* root = new SegTreeNode(0, baskets.size() - 1, baskets);
        int res = 0;
        for (int fruit : fruits) {
            int node_idx = root->find(fruit);
            if (node_idx != -1) {
                // Found a suitable basket: mark it as used
                root->update(node_idx, -1);
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
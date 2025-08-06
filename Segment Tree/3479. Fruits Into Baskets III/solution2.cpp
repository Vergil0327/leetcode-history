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
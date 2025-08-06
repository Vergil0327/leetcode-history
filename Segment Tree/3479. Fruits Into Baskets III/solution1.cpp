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
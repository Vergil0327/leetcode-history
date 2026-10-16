/*
### Problem Explanation & Mathematical Formulation

Let `d(i, j)` be the number of distinct elements in the subarray `nums[i..j]`.
We want to find:
   $$\sum_{j=0}^{n-1} \sum_{i=0}^{j} (d(i, j))^2 \pmod{10^9 + 7}$$

#### Key Transition Observation
When we extend the right endpoint from $j-1$ to $j$ (processing element `x = nums[j]`):
- Let `last[x]` be the previous index where `x` appeared in `nums` (or `-1` if it's the first occurrence).
- For any starting index $i \in (\text{last}[x], j]$, the subarray `nums[i..j]` contains the new element `x` for the first time.
- Therefore:
  - $d(i, j) = d(i, j-1) + 1$ for $i \in [\text{last}[x] + 1, j]$
  - $d(i, j) = d(i, j-1)$ for $i \in [0, \text{last}[x]]$

#### Updating the Sum of Squares
Let $d_i = d(i, j-1)$. When we add $1$ to $d_i$ for $i \in [L, R]$ (where $L = \text{last}[x] + 1$ and $R = j$):
$$(d_i + 1)^2 = d_i^2 + 2d_i + 1$$

Summing this over $i \in [L, R]$:
$$\sum_{i=L}^{R} (d_i + 1)^2 = \sum_{i=L}^{R} d_i^2 + 2 \sum_{i=L}^{R} d_i + (R - L + 1)$$

So to maintain the total sum of squares efficiently as $j$ increases:
1. We need a data structure that supports:
   - Range addition of $+1$ to array $D$.
   - Querying the range sum of elements in $D$ (to compute $\sum 2d_i$).
   - Querying the total sum of squares $\sum d_i^2$.
2. A **Segment Tree with Lazy Propagation** handles these operations in $O(\log n)$ per element.

### Segment Tree Design

Each Segment Tree node covering range [l, r] maintains:
- `sum`: $\sum_{i=l}^r d_i$
- `sq_sum`: $\sum_{i=l}^r d_i^2$
- `lazy`: Pending range addition value.

When applying a range add $+v$ to a node covering `len` elements:
- `sq_sum_new = sq_sum + 2 * v * sum + v^2 * len`
- `sum_new = sum + v * len`
- `lazy_new = lazy + v`
*/
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
    static const int MOD = 1e9 + 7;

    struct Node {
        long long sum = 0;
        long long sq_sum = 0;
        long long lazy = 0;
    };

    vector<Node> tree;

    void push(int node, int l, int r) {
        if (tree[node].lazy == 0) return;
        
        long long v = tree[node].lazy;
        int mid = l + (r - l) / 2;
        
        // Push to left child
        apply(node * 2, l, mid, v);
        // Push to right child
        apply(node * 2 + 1, mid + 1, r, v);
        
        tree[node].lazy = 0;
    }

    void apply(int node, int l, int r, long long v) {
        long long len = r - l + 1;
        tree[node].sq_sum = (tree[node].sq_sum + 2 * v % MOD * tree[node].sum % MOD + v * v % MOD * len % MOD) % MOD;
        tree[node].sum = (tree[node].sum + v * len) % MOD;
        tree[node].lazy = (tree[node].lazy + v) % MOD;
    }

    void update(int node, int l, int r, int ql, int qr, long long v) {
        if (ql <= l && r <= qr) {
            apply(node, l, r, v);
            return;
        }
        push(node, l, r);
        int mid = l + (r - l) / 2;
        if (ql <= mid) update(node * 2, l, mid, ql, qr, v);
        if (qr > mid) update(node * 2 + 1, mid + 1, r, ql, qr, v);
        
        tree[node].sum = (tree[node * 2].sum + tree[node * 2 + 1].sum) % MOD;
        tree[node].sq_sum = (tree[node * 2].sq_sum + tree[node * 2 + 1].sq_sum) % MOD;
    }

public:
    int sumCounts(vector<int>& nums) {
        int n = nums.size();
        tree.assign(4 * n, Node());
        
        unordered_map<int, int> last_pos;
        long long total_ans = 0;
        
        for (int j = 0; j < n; ++j) {
            int prev_idx = last_pos.count(nums[j]) ? last_pos[nums[j]] : -1;
            
            // Add +1 to range [prev_idx + 1, j]
            update(1, 0, n - 1, prev_idx + 1, j, 1);
            
            // Accumulate current total sum of squares for all subarrays ending at j
            total_ans = (total_ans + tree[1].sq_sum) % MOD;
            
            last_pos[nums[j]] = j;
        }
        
        return total_ans;
    }
};
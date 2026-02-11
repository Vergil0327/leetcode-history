// 1. Transform the problem: We want a subarray $[j, i]$ where $\text{DistinctEven}(j, i) - \text{DistinctOdd}(j, i) = 0$.
// 2. Maintain "Last Seen" Positions: As we iterate $i$ from $0$ to $n-1$:If nums[i] is even: it contributes $+1$ to any subarray starting after its previous occurrence.If nums[i] is odd: it contributes $-1$ to any subarray starting after its previous occurrence.
// 3. Segment Tree updates: At index $i$, we update the range $[previous[i]+1, i]$ with the contribution.The value at index $j$ in the segment tree represents the balance $\text{Even} - \text{Odd}$ for a subarray starting at $j$ and ending at $i$.
// 4. The Search: We need the smallest $j$ such that the value in the segment tree at index $j$ is $0$.
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class SegmentTree {
    int n;
    vector<int> minVal, maxVal, lazy;

public:
    SegmentTree(int n) : n(n), minVal(4 * n, 0), maxVal(4 * n, 0), lazy(4 * n, 0) {}

    void push(int v) {
        if (lazy[v] != 0) {
            minVal[2 * v] += lazy[v];
            maxVal[2 * v] += lazy[v];
            lazy[2 * v] += lazy[v];
            minVal[2 * v + 1] += lazy[v];
            maxVal[2 * v + 1] += lazy[v];
            lazy[2 * v + 1] += lazy[v];
            lazy[v] = 0;
        }
    }

    void update(int v, int tl, int tr, int l, int r, int add) {
        if (l > r) return;
        if (l == tl && r == tr) {
            minVal[v] += add;
            maxVal[v] += add;
            lazy[v] += add;
        } else {
            push(v);
            int tm = (tl + tr) / 2;
            update(2 * v, tl, tm, l, min(r, tm), add);
            update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add);
            minVal[v] = min(minVal[2 * v], minVal[2 * v + 1]);
            maxVal[v] = max(maxVal[2 * v], maxVal[2 * v + 1]);
        }
    }

    int find_leftmost(int v, int tl, int tr, int target) {
        // If target 0 is not in the range [min, max], it's not here
        if (minVal[v] > target || maxVal[v] < target) return -1;
        if (tl == tr) return tl;
        
        push(v);
        int tm = (tl + tr) / 2;
        int res = find_leftmost(2 * v, tl, tm, target);
        if (res == -1) {
            res = find_leftmost(2 * v + 1, tm + 1, tr, target);
        }
        return res;
    }
};

class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> lastIdx;
        SegmentTree st(n);
        int res = 0;

        for (int i = 0; i < n; i++) {
            int val = nums[i];
            int prev = lastIdx.count(val) ? lastIdx[val] : -1;
            int contrib = (val % 2 == 0) ? 1 : -1;

            // Add contribution only to subarrays where this instance is the FIRST occurrence from the left
            st.update(1, 0, n - 1, prev + 1, i, contrib);

            int j = st.find_leftmost(1, 0, n - 1, 0);
            if (j != -1 && j <= i) {
                res = max(res, i - j + 1);
            }
            lastIdx[val] = i;
        }
        return res;
    }
};
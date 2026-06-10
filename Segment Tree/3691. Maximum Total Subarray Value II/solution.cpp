#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
#include <climits>

using namespace std;

class SegmentTree {
private:
    int n;
    vector<long long> st;
    function<long long(long long, long long)> op;
    long long identity;

public:
    SegmentTree(const vector<int>& A, function<long long(long long, long long)> operation) {
        n = A.size();
        op = operation;
        
        // Use 64-bit bounds to prevent wrap-around overflow bugs
        if (op(LLONG_MAX, LLONG_MIN) == LLONG_MIN) {
            identity = LLONG_MAX; // Min Tree
        } else {
            identity = LLONG_MIN; // Max Tree
        }

        st.resize(2 * n);
        for (int i = 0; i < n; ++i) {
            st[n + i] = A[i];
        }
        for (int i = n - 1; i > 0; --i) {
            st[i] = op(st[i << 1], st[i << 1 | 1]);
        }
    }

    void set(int i, long long v) {
        i += n;
        st[i] = v;
        while (i > 1) {
            st[i >> 1] = op(st[i], st[i ^ 1]);
            i >>= 1;
        }
    }

    long long get(int i) {
        return st[i + n];
    }

    long long query(int l, int r) {
        l += n;
        r += n;
        long long res = identity;

        while (l <= r) {
            if (l == r) {
                res = op(res, st[l]);
                break;
            }
            if ((l & 1) == 1) {
                res = op(res, st[l]);
                l += 1;
            }
            if ((r & 1) == 0) {
                res = op(res, st[r]);
                r -= 1;
            }
            l >>= 1;
            r >>= 1;
        }
        return res;
    }
};

class Solution {
private:
    struct SubarrayState {
        long long value;
        int l;
        int r;

        // Max-heap ordering matching Python's min-heap with negated values
        bool operator<(const SubarrayState& other) const {
            return this->value < other.value;
        }
    };

public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int n = nums.size();
        if (n == 0 || k == 0) return 0;
        
        auto min_op = [](long long a, long long b) { return min(a, b); };
        auto max_op = [](long long a, long long b) { return max(a, b); };

        SegmentTree rootMax(nums, max_op);
        SegmentTree rootMin(nums, min_op);

        auto value = [&](int l, int r) -> long long {
            return rootMax.query(l, r) - rootMin.query(l, r);
        };

        priority_queue<SubarrayState> pq;
        for (int l = 0; l < n; ++l) {
            pq.push({value(l, n - 1), l, n - 1});
        }

        long long res = 0;
        while (k > 0 && !pq.empty()) {
            auto current = pq.top();
            pq.pop();

            res += current.value;
            int l = current.l;
            int r = current.r;

            if (l <= r - 1) {
                pq.push({value(l, r - 1), l, r - 1});
            }
            k--;
        }

        return res;
    }
};
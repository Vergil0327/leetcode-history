#include <map>

using namespace std;

// Square Root Decomposition
// The Problem: High Frequency vs. Low Frequency
// If you process every query with a while loop, a query with $k=1$ could touch all $N$ elements. With $Q$ queries, the worst-case complexity is $O(Q \cdot N)$, which is too slow ($10^5 \cdot 10^5 = 10^{10}$).
// - When $k$ is Large ($k > \sqrt{n}$): The robot jumps so far that it only hits a few elements (at most $\sqrt{n}$ elements). We can just use a while loop. Total work: $O(Q \sqrt{n})$.
// - When $k$ is Small ($k \le \sqrt{n}$): The robot hits many elements. We need a way to "batch" these updates.

// Why $(k, l \pmod k)$?
// Imagine $k=3$. The robot can start at index $0, 1,$ or $2$.
// - If it starts at $0$, it hits indices $\{0, 3, 6, 9...\}$
// - If it starts at $1$, it hits indices $\{1, 4, 7, 10...\}$
// - If it starts at $2$, it hits indices $\{2, 5, 8, 11...\}$

// Notice that these three sets are completely disjoint. They form different "tracks" or buckets. By grouping queries by $k$ and the remainder $l \pmod k$, you are grouping all queries that travel on the exact same track.

// How we Batch the Updates
// For a specific track (e.g., $k=3, \text{remainder}=1$):

// 1. All updates in this group are essentially updating a simple linear array where "index 1" is position 0, "index 4" is position 1, and so on.
// 2. We use a Difference Array (or Prefix Product array) on this track. Instead of multiplying every element, we mark the start ($l$) and the end ($r$) of the update range.
// 3. After processing all queries for that track, we "sweep" through it once to apply all multiplications to the nums array in $O(N/k)$ time.


class Solution {
    const int MOD = 1e9 + 7;

    long long power(long long base, long long exp) {
        long long res = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp % 2 == 1) res = (res * base) % MOD;
            base = (base * base) % MOD;
            exp /= 2;
        }
        return res;
    }

    long long modInverse(long long n) {
        return power(n, MOD - 2);
    }

public:
    int xorAfterQueries(vector<int>& nums, vector<vector<int>>& queries) {
        int n = nums.size();
        int boundary = sqrt(n);

        // Using a map to only store rows for small 'k' that are actually used
        // map<k, diff_array_of_length_n>
        map<int, vector<int>> events;

        for (const auto& q : queries) {
            int l = q[0], r = q[1], k = q[2], v = q[3];
            if (v == 1) continue;

            if (k > boundary) {
                // Large k: Direct update
                for (int i = l; i <= r; i += k) {
                    nums[i] = (1LL * nums[i] * v) % MOD;
                }
            } else {
                // Small k: Difference array logic
                if (events.find(k) == events.end()) {
                    events[k].assign(n, 1);
                }
                
                events[k][l] = (1LL * events[k][l] * v) % MOD;
                
                // Find the first index in the sequence l, l+k, l+2k... that is > r
                // Logic: l + m*k > r  => m*k > r - l => m > (r - l)/k
                int steps = (r - l) / k;
                int r2 = l + (steps + 1) * k;
                
                if (r2 < n) {
                    events[k][r2] = (1LL * events[k][r2] * modInverse(v)) % MOD;
                }
            }
        }

        // Apply small k updates
        for (auto& entry : events) {
            int k = entry.first;
            vector<int>& row = entry.second;

            // Each start index defines a disjoint 'track'
            for (int start = 0; start < k; ++start) {
                long long multiplier = 1;
                for (int j = start; j < n; j += k) {
                    if (row[j] != 1) {
                        multiplier = (multiplier * row[j]) % MOD;
                    }
                    if (multiplier != 1) {
                        nums[j] = (1LL * nums[j] * multiplier) % MOD;
                    }
                }
            }
        }

        int ans = 0;
        for (int x : nums) {
            ans ^= x;
        }
        return ans;
    }
};
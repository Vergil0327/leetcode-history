#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <queue>

using namespace std;

/*
1. The Core Logic Error

In this problem, the only thing that matters for a row is the number of trailing zeros.
- Row 0 needs $n-1$ trailing zeros.
- Row 1 needs $n-2$ trailing zeros....
- and so on.

2. The Logic: The Greedy Strategy

    1. Pre-process: Convert each row into a single integer representing its count of trailing zeros.
    2. Iterate: For each row $i$ from $0$ to $n-1$:
        - Calculate the required trailing zeros: target = n - 1 - i.
        - Find the first row at or below $i$ that satisfies zeros >= target.
        - If no such row exists, return -1.
        - If found at index $j$, the number of swaps needed is $(j - i)$.
        - Physically move that row to position $i$ (simulating the shift).
*/

class Solution {
public:
    int minSwaps(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> trailingZeros(n);

        // Step 1: Count trailing zeros for each row
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = n - 1; j >= 0; --j) {
                if (grid[i][j] == 0) count++;
                else break;
            }
            trailingZeros[i] = count;
        }

        int totalSwaps = 0;

        // Step 2: Greedy Placement
        for (int i = 0; i < n; i++) {
            int target = n - 1 - i;
            int foundIdx = -1;

            // Find the nearest row that satisfies the condition
            for (int j = i; j < n; j++) {
                if (trailingZeros[j] >= target) {
                    foundIdx = j;
                    break;
                }
            }

            if (foundIdx == -1) return -1;

            // Step 3: Simulate the swaps and increment totalSwaps
            totalSwaps += (foundIdx - i);
            
            // Move the found row to the current position i
            // This is like a bubble sort step
            int val = trailingZeros[foundIdx];
            for (int k = foundIdx; k > i; k--) {
                trailingZeros[k] = trailingZeros[k - 1];
            }
            trailingZeros[i] = val;
        }

        return totalSwaps;
    }
};
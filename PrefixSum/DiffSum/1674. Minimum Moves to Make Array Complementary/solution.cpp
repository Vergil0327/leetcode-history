#include <string>
#include <vector>
#include <numeric>
#include <functional>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <queue>
#include <stack>
#include <map>

using namespace std;
using LL = long long;
using vll = vector<LL>;

/*
To solve this problem, you need to transition from thinking about "specific pairs" to thinking about "ranges of possible sums."
For any target sum $S$, we want to know how many moves it takes to make all pairs equal to $S$. For each pair $(A, B)$ (where $A = \text{nums}[i]$ and $B = \text{nums}[n-1-i]$), the number of moves required to reach a target sum $S$ depends on the value of $S$:

1. Categorizing the MovesLet $A \le B$ for simplicity.

    - 0 moves: If $S = A + B$.
    - 1 move: If we change only one number. The smallest possible sum with 1 move is $1 + A$ (replace $B$ with $1$). The largest possible sum is $\text{limit} + B$ (replace $A$ with $\text{limit}$).
        - So, 1 move is enough if $1+A \le S \le \text{limit}+B$, and $S \ne A+B$.
    - 2 moves: If $S$ is outside the 1-move range.
        - The absolute minimum possible sum is $1 + 1 = 2$.
        - The absolute maximum possible sum is $\text{limit} + \text{limit} = 2 \cdot \text{limit}$.

2. Using the Difference Array (Sweep Line)
    - Since we have $10^5$ pairs and $2 \cdot \text{limit}$ possible target sums, we can't iterate through every $S$ for every pair. Instead, we use a Difference Array to mark the moves required for all $S \in [2, 2 \cdot \text{limit}]$.For each pair $(A, B)$:
    - Initially, assume 2 moves for all sums: Add +2 to the range $[2, 2 \cdot \text{limit}]$.
    - Actually, it only takes 1 move if $S \in [1 + \min(A, B), \text{limit} + \max(A, B)]$: Subtract -1 from this range.
    - Actually, it takes 0 moves if $S = A + B$: Subtract another -1 from this specific point.
*/
class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
        // diff[i] stores the change in moves for a target sum 'i'
        // Possible sums range from 2 to 2 * limit
        vector<int> diff(2 * limit + 2, 0);

        for (int i = 0; i < n / 2; ++i) {
            int A = nums[i];
            int B = nums[n - 1 - i];

            // 1. Default: 2 moves for every sum in [2, 2 * limit]
            diff[2] += 2;
            diff[2 * limit + 1] -= 2;

            // 2. Reduce to 1 move for the range [min(A, B) + 1, max(A, B) + limit]
            int min_sum_1_move = min(A, B) + 1;
            int max_sum_1_move = max(A, B) + limit;
            diff[min_sum_1_move] -= 1;
            diff[max_sum_1_move + 1] += 1;

            // 3. Reduce to 0 moves for the exact sum A + B
            diff[A + B] -= 1;
            diff[A + B + 1] += 1;
        }

        int ans = n; // Max moves possible is n (2 per pair)
        int current_moves = 0;
        // Sweep from sum 2 to 2 * limit
        for (int s = 2; s <= 2 * limit; ++s) {
            current_moves += diff[s];
            ans = min(ans, current_moves);
        }

        return ans;
    }
};
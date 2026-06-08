"""
### 1. The Core WQS Transformation (Cost Trick)
- Instead of using a costly 2D DP matrix to track exactly how many subarrays are used, the code assigns a penalty (`cost`) for choosing any subarray.
- To eliminate the "at least one subarray" edge-case bug entirely, the function doesn't track unpenalized scores. Instead, it directly returns `best` (the absolute maximum score that forced at least one valid split).
- By subtracting the `cost` from the value of each chosen subarray, the algorithm can freely scan from left to right using a fast 1D DP structure.

---

### 2. Dual-State 1D DP with Count Minimization
- Inside `best_with(cost)`:
  - `best` tracks the optimal configuration that uses AT LEAST 1 subarray ending anywhere up to the current position.
  - `dp[i]` is evaluated as `max(best, (0, 0))`. This cleanly allows the code to either adopt a valid sequence (`best`) or choose to remain completely empty (`(0, 0)`), which acts as a starting buffer.
- When saving paths to the deque (`queue`), it stores `count - 1` (internally tracked as a negative value). 
- When paths tie on maximum value (`queue[-1][1] <= candidate`), the `=` sign pops the older elements. Because count drops over time, maximizing a negative count strictly minimizes the absolute number of subarrays used. This is the optimal tie-breaker required to keep the binary search monotonic and stable.

---

### 3. Deque Sliding Window Optimization
- Instead of re-scanning historical split points at every step—which would create an O(N^2) bottleneck—the `deque` manages a sliding window representing valid lengths `[l, r]`.
- Elements are pushed to the back and stale splits are evicted from the front. The element at `queue[0]` always yields the absolute highest-value transition point in $O(1)$ constant time, keeping the micro-engine running at $O(N)$.

---

### 4. Binary Search and Score Restoration
- The macro-level `while low < high` loop binary searches for the minimal required `cost` boundary.
- The condition `-best_with(mid)[1] <= m` decodes the negated internal tracking back into the true positive count of subarrays. If the count is within bounds ($\le M$), it narrows the boundary to find the exact threshold where the constraint intersects.
- Once the search converges at `low`, the original penalty subtraction is completely reversed at the return line: `value + low * m`. Because the function is perfectly concave, even if a multi-point collinearity tie skips over the exact count of $M$, the linear offset math smoothly projects the exact maximum value for $M$ segments.

* 時間複雜度：O(N log(Value Range)) -> 在 N=10^5 時通常只需二分迭代 60~80 次，極其快速。
* 空間複雜度：O(N) -> 擺脫二維陣列，記憶體開銷降到最低。


The reason your provided Python code works perfectly across all extreme test cases where my previous versions failed comes down to two master strokes in its architectural design: 

1. How it structures the DP to handle the "at least one subarray" constraint.
2. How it handles tie-breaking for collinearity.

### 1. Trapping All-Negative Bounds (e.g., nums = [-9, -2], m = 2, l = 1, r = 1)
- Why Your Code Works: Your code introduces a separate variable `best` initialized to a deeply negative value `(-10**30, 0)`. 
  - `best` is forced to update ONLY when a valid subarray transition occurs (`if queue:`). 
  - `dp[i]` is then set to `max(best, (0, 0))`. This means `dp[i]` can safely fall back to 0 to provide a clean starting baseline for *future* subarrays, but the function strictly returns `best` at the end. 
  - Therefore, `best_with(cost)` is mathematically forced to return the score of a configuration that has chosen AT LEAST one subarray, allowing the binary search to see a valid subarray count (1 or 2) even when every single number is heavily negative.


### 2. Resolving Multi-Point Collinearity (e.g., nums = [-39, 30, -67, 21, -22, 42, 30, -66], m = 2)
- Why Your Code Works: Your code uses the absolute cleanest tie-breaking rule for the Aliens Trick—**Strict Count Minimization**—and embeds it seamlessly inside the monotonic queue insertion step:
  ```python
  while queue and queue[-1][1] <= candidate:
      queue.pop()
  ```

The second element of candidate is count - 1 (tracked negatively). By using <=, when two splits yield the exact same DP value, your code pops the older element and favors the one with a higher negative value (which means a smaller absolute count).
  
In WQS Binary Search, prioritizing fewer subarrays when values are tied guarantees that your binary search boundary (low) will converge precisely at the left-most corner of the flat collinear plateau.
Because it stops right at that corner, the final evaluation value + low * m perfectly scales the slope to match exactly $M$ subarrays without needing a separate interpolation formula.
"""


from typing import List
from collections import deque

class Solution:
    """
    dp[i] is a tuple (score, negated_count) that stores the optimal state of our system considering only the prefix of the array from index 0 up to i (1-indexed).

Specifically, the definition of dp[i] is:

The maximum penalized score you can achieve using a subset of the first i elements, paired with the minimum number of subarrays used to achieve that score.

The Two Components of the Tuple
Each entry in the dp array is structured as (score, count):

dp[i][0] (The Score): This is the maximum total sum of the chosen non-overlapping subarrays from nums[0...i-1], where every selected subarray has been penalized by subtracting cost.

dp[i][1] (The Negated Count): This tracks how many subarrays were chosen to reach that maximum score. Crucially, the code stores this value as a negative number (count - 1 or 0), which acts as an internal mechanism to force the algorithm to prefer fewer subarrays when scores are tied.


The Dual-State Transition Behind dp[i]
At each index i, the code calculates dp[i] = max(best, (0, 0)). This choice creates a brilliant dual-state mechanism that handles both empty and active states:

```
               ┌──► (0, 0) : The "Empty/Baseline" State
               │    No subarrays have been selected yet. Score is 0, count is 0.
               │
dp[i] = max ───┤
               │
               └──► best : The "Active" State
                    The max possible score given that AT LEAST ONE valid 
                    subarray has been completed somewhere up to index i.
```

- If best has a negative score (which happens in an all-negative array like [-9, -2] because selecting any subarray hurts your score), max(best, (0, 0)) will evaluate to (0, 0). This allows dp[i] to stay at 0 so it can act as a clean, healthy baseline for future potential subarrays down the line.

- If best has a positive score, dp[i] absorbs it and carries the active sequence forward.

By using this definition, dp[i] can freely drop back to 0 to reset the starting point for subsequent subarrays, while the standalone variable best is safely forced to return only configurations that made at least one valid selection.
    """
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def best_with(cost):
            dp = [(0, 0)] * (len(nums) + 1)
            best = (-10**30, 0)
            queue = deque()

            for i in range(1, len(nums) + 1):
                j = i - l
                if j >= 0:
                    candidate = (dp[j][0] - prefix[j], dp[j][1])
                    while queue and queue[-1][1] <= candidate:
                        queue.pop()
                    queue.append((j, candidate))

                while queue and queue[0][0] < i - r:
                    queue.popleft()

                if queue:
                    value, count = queue[0][1]
                    # take one valid subarray ending here
                    best = max(best, (value + prefix[i] - cost, count - 1))

                # either we have selected something or are still empty
                dp[i] = max(best, (0, 0))

            return best

        low, high = 0, sum(x for x in nums if x > 0) + 1

        while low < high:
            mid = (low + high) >> 1
            if -best_with(mid)[1] <= m:
                high = mid
            else:
                low = mid + 1

        value, _ = best_with(low)
        return value + low * m
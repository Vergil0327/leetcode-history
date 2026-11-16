"""
### Solution 2: Monotonic Stack (Bitwise Inclusion)

Assign each consistent subarray uniquely to the index i of its LEFTMOST minimum 
value v = nums[i].

For a subarray nums[l..r] (with l <= i <= r) to have leftmost minimum at i AND 
bitwise AND equal to v:
1. Every element nums[k] in nums[l..r] must contain all set bits of v:
       (nums[k] & v) == v
   (Note: for non-negative integers, (nums[k] & v) == v automatically guarantees 
   nums[k] >= v, so v is guaranteed to be the minimum of the subarray.)
2. To prevent double-counting subarrays with duplicate minimums, elements strictly 
   to the left (l <= k < i) must be strictly greater than v:
       nums[k] != v

---

### Finding Boundaries in O(n) via Bitmask-Chain Monotonic Stack

- Right Boundary R[i]:
  Nearest index j > i where `(nums[j] & nums[i]) != nums[i]` (or n if none exists).
  - Scan left-to-right maintaining a stack of unresolved indices.
  - Because an element is only pushed if it contains all set bits of the current 
    stack top, the values in the stack from bottom to top form a chain of bitmask 
    inclusions: nums[s_0] <=_bits nums[s_1] <=_bits ... <=_bits nums[s_top].
  - By transitivity, if the current value x lacks a set bit of the stack top, we 
    pop the top and assign R[top] = j; if x contains all bits of the top, it 
    contains all bits of every element deeper in the stack.

- Left Boundary L[i]:
  Nearest index j < i where `(nums[j] & nums[i]) != nums[i]` OR `nums[j] == nums[i]` 
  (or -1 if none exists).
  - Scan right-to-left using the same logic, popping whenever x lacks a set bit of 
    the stack top OR equals the stack top.
  - Surviving stack elements form a strict bitmask-inclusion chain from bottom to top.

- Contribution of Index i:
  Any start l in [L[i] + 1, i] paired with any end r in [i, R[i] - 1] forms a 
  valid consistent subarray with leftmost minimum at i:
      count(i) = (i - L[i]) * (R[i] - i)

=== Solution 2 Complexity Analysis ===

1. Time Complexity: O(n)
   - Each index is pushed onto the stack once and popped at most once in the 
     left-to-right pass, and once in the right-to-left pass.
   - Final summation takes O(n) time.
   - Total Time Complexity: O(n) ≈ 0.25s - 0.40s in Python for n = 2 * 10^5.

2. Space Complexity: O(n)
   - Boundary arrays L and R of size n, plus the monotonic stack of size at most n.
   - Total Auxiliary Space: O(n).
"""
class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Right boundaries R[i]: first j > i lacking a set bit of nums[i]
        R = [n] * n
        stack = []
        for j, x in enumerate(nums):
            while stack and (x & nums[stack[-1]]) != nums[stack[-1]]:
                R[stack.pop()] = j
            stack.append(j)
            
        # 2. Left boundaries L[i]: first j < i lacking a set bit of nums[i] or equal to nums[i]
        L = [-1] * n
        stack.clear()
        for j in range(n - 1, -1, -1):
            x = nums[j]
            while stack and ((x & nums[stack[-1]]) != nums[stack[-1]] or x == nums[stack[-1]]):
                L[stack.pop()] = j
            stack.append(j)
            
        # 3. Sum valid subarrays anchored at each leftmost minimum i
        ans = 0
        for i in range(n):
            ans += (i - L[i]) * (R[i] - i)
            
        return ans
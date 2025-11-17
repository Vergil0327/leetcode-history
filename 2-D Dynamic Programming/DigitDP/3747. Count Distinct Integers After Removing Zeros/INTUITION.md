# Intuition

ex.
1 = 01 = 001 = 0001
10 = 010 = 0010

目標:

1. 建構出不含任何`0`的數並計數 => digit DP
2. only allow `0` in leading zeros.

Time complexity: O(m×2×2×2×10) = O(m)

i <= m (m最多15位數)
2 possible values for lowerThanHigh (true/false)
2 possible values for greaterThanLow (true/false)
2 possible values for leadingZero (true/false)
10 digit choices (0-9) at each position
Each state computed once due to memoization

Memoization map stores O(m × 2 × 2 × 2) = O(m) states

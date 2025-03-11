# Intuition

- Two-pointer tracking: The algorithm maintains the two most restrictive left endpoints for each position, which is crucial for calculating the improvement when removing a pair.
- Improvement calculation: By tracking how restrictive each conflicting pair is, we can calculate exactly how many additional subarrays would become valid if that pair were removed.
- Efficient array indexing: Instead of explicitly checking every subarray, the solution uses clever indexing to calculate the counts directly.

目標就是持續追蹤更新最靠右的兩個conflictingPair
- 都不刪除, 那麼對於當前右端點`r`來說, 有r-left[0]個valid subarray
- 如果刪除left[0], 那麼我們就會多出`left[0]-left[1]`這些合法左端點
    - 記錄刪除每個conflictingPair所帶來的增益, 最終取max相加

# Approach

This solution uses a clever approach based on a key insight about conflicting pairs: for each position `r` in the array, we need to track how far back we need to go (to some position `l`) to avoid including all conflicting pairs.

# Complexity

time: O(n+m) where n is the array size and m is the number of conflicting pairs
space: O(n)
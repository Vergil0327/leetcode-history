# Intuition

use slow/fast two pointers, `l` & `r`

- keeps nums[l] valid and use it as current compared value.
- keeps `l` < `r`

once nums[r] != nums[l], it means we consider new number series:
- set `cnt` to 0
- move `l` pointer and swap

once nums[r] == nums[l] and `cnt` is valid:
- move `l` pointer and swap

# Complexity

- time complexity

$$O(n)$$

- time complexity

$$O(1)$$
# Intuition

strs = [
    X | XXXXXXXX,
    Y | YYYYYYYY,
    Z | ZZZZZZZZ,
]

let's check column by column.
1. if any X > Y or Y > Z, we need to remove this column
2. if X < Y < Z, it means `XXX...` and `YYY...` are sorted. no matter rest of `XXXX...` and `YYY...`
   - ex. [azxcvb, babcde]
   - it's sorted because a < b
3. if X == Y, then we need to check next column of `XXX...` and `YYY...`

thus, we can greedily check if `j-th` column is sorted or not. if any two of row is equal, we keep continuing to check next column.

and we need to store information if row is sorted or we need to compare next column.

let's use a array `relation[i]` for it.
- if relation[i] = 1, it means nums[i] and nums[i+1] is strictly sorted. nums[i][j] < nums[i+1][j]
- if relation[i] = 0, it means nums[i][j] = nums[i+1]j, we need to continue comparing nums[i][j+1] with nums[i+1][j+1]

# Complexity

- time complexity
$$(COLS * n)$$

- space complexity
$$O(n)$$

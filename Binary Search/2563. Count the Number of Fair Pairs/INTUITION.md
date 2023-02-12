# Intuition

- 0 <= i < j < n
- lower <= nums[i] + nums[j] <= upper

根據這兩個條件，我們可以想成遍歷每個nums[j]，要往前找一個nums[i]符合:

`lower-nums[j] <= nums[i] <= upper - nums[j]`

所以我們可以維護一個有序array, SortedList, 然後每次都往前找出上下界
- 下界: lower-nums[j] <= nums[i] -> 我們可以用bisect_left 找出這個index, `n`
- 上界: <= upper - nums[j]       -> 我們可以用bisect_right找出這個index, `m`

m就是第一個 > upper-nums[j]的位置
n就是 >= lower-nums[j]的位置
那麼符合條件的區間就會是 `m-n`

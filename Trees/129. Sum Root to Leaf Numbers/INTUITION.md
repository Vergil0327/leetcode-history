# Intuition

when do we reach leaf node?: `if not root.left and not root.right`

ex root = [1,2,3]

if we backtrack each path until leaf node, we can get:
[[1,2], [1,3]]

we can join as `str` and turn into `int` and sum them up

but since we've already get the num one by one, we can calculate along the path actually

ex. if nums = [1,2], we can calculate sum by:
`sum = 1*10 + 2 = 12`

if we add one more path num, we can get next sum by:
`next sum = current sum * 10 + current num`

therefore, we can calculate sum along the path and append to `nums` array. (the benefit is that we can get rid of array copy)

after we finish backtracking, return answer with `sum(nums)`

# Complexity

- time complexity

$$O(2^n)$$

- space complexity

$$O(n)$$
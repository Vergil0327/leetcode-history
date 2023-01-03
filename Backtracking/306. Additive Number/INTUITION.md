# DFS - backtracking

## Intuition

try every possible partition!

remember that we can't accept leading zero, we need to skip this condition:

`if len(num[:i])>1 and num[:i][0] == "0": continue`

if we only use this condition, it'll pass but slow

remember, whenever we choose next partition, its digit must match sum of last two at last

ex. state = [10, 100] and num = "XXXXXXX"
we must split nums[:i] at i>= len("110") at least because 10+100 = 110 and next partition must equals sum of last two num.

if we split num[:2] or nums[:1], it's impossible to make new string partition equals to sum of last two

therefore, we can add this condition to prune recursion:

`if len(state) > 2 and i < len(str(state[-1]+state[-2])): continue`


## Complexity

- time complexity

$$O(n! * n)$$

- space complexity

$$O(n)$$
# Mirror Generation

## Intuition

1. copy gray code of n-1
2. mirror gray code of n-1, which means copy and reverse order

then we got two gray code, one is last n-1 gray code and the other is reversed one.
let's define original one is first half, and the other reversed one is second half

3. add `0` at left-most bit for every code in first half. (didn't change actually)
4. add `1` at left-most bit for every code in second half

then we got gray code of n

base case: n = 0: [0]

n = 1: [0,1]

n = 2, first half: [0,1] and second half: [1,0]

start from n-1:
0 -> `0`0 (first half append `0` to left)
1 -> `0`1 (first half append `0` to left)
1 -> `1`1 (second half append `1` to left)
0 -> `1`0 (second half append `1` to left)

**why it works ?**

- because each half already diff one bit.
- though the middle is the same (it's mirror-like), it'll diff one bit after we append `0` and `1` to each other

n = 3
00 -> `0`00
01 -> `0`01
11 -> `0`11
10 -> `0`10
10 -> `1`10
11 -> `1`11
01 -> `1`01
00 -> `1`00

# Complexity:

- time complexity
$O(n^2)$

- space complexity

$$O(n)$$
# Sorting

## Intuition

for every interval([`startTime`, `endTime`])
first thought, sorting first!
then we just consider the order of `endTime`

compare two sorted intervals
[starti, endi], [startj, endj]

1. if endj <= endi, found one
ex. [1, 10], [1, 5]
ex. [1, 10], [2, 5]

2. if starti == startj, and endj >= endi, found one
ex. [1, 4], [1, 10]

thus, we can sort `startTime` in increasing order and `endTime` in decreasing order

then sorting will handle two cases above correctly for us

ex. after sorting
[1, 10], [1, 4], [2, 2]

and we just count endTime <= prev endTime

## Approach

1. sort startTime in increasing order
2. sort endTime in decreasing order
3. compare current one with previous one

## Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(n)$$

# Space Optimized

Since we only consider previous one after sorting,
we can use just two variables
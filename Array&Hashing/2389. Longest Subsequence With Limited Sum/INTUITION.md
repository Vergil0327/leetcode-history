# Intuition

the key point is we don't care about order because what we concern is subsequence.

we can sort `nums` array and pick from smallest one to largest one to calculate

- method 1: sorting

we can sort `queries` first and find each subsequence's sum in order.

we can reuse previous subsequence sum and keep finding next query's answer

- binary search with prefix sum

create subsequence's prefix sum of sorted `nums` and binary search each query's answer


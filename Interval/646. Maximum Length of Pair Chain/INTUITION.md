# Intuition

Greedy approach: sort by interval's end_time

- want maximum non-overlapping interval -> sort end_time

  - [proof here](https://leetcode.com/problems/maximum-length-of-pair-chain/solutions/225801/proof-of-the-greedy-solution/)

- want choose as many intervals as possible -> sort by start_time

time: $O(nlogn)$
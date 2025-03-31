# Approach

[original post](https://leetcode.com/problems/maximize-active-section-with-trade-ii/solutions/6593474/easy-understandable-short-explanation-c-python-java)

- The input string s is divided into contiguous segments of '0's and '1's.
Each segment stores its starting index and length.
- A Range Maximum Query (RMQ) table is built to efficiently find the best segments to flip.
- The idea is to check for 0 segments and see how much they can contribute when flipping to 1.
- Only valid 0 segments that have a 1 segment between them are stored in RMQ.
- For each query [left, right], find the relevant segments using upper_bound.
- If the range contains only 2 segments, flipping won’t help, so return the current active count.
- Otherwise, compute the best way to flip a 0 segment in the range and maximize the active sections.

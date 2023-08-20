# Intuition

- greedily choose `num` from 1 to larger until we choose k choices
- use a hashset to store our choice to check if `k-num` in our choices since we want avoid `any element in set + num = k`
  - choose num if `k-num not in set`
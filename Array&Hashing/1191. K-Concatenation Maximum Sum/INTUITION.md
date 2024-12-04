# Intuition

- if k == 1: use kadane algorithm to find maximum subarray sum
- if k > 1:
    - condition1: if sum(arr) > 0, maximum subarray sum will be `sum(arr)*k`
    - condition2: if sum(arr) <= 0, maximum subarray sum might be:
        1. max_suffix_sum + sum(arr) * (k-2) + max_prefix_sum
        2. max subarray sum from kadane algorithm
    - therefore, answer should be `max(sum(arr)*k, mx_subarray_sum, max_suffix_sum + sum(arr) * (k-2) + max_prefix_sum)`
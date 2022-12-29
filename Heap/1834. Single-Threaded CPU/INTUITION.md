# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
Just simulate it!
1. first, we enqueue the task with enqueuTime in increasing order
2. since we need to consume task with minimum process time first, using **priority queue** `pq` to handle priority for us.
3. keep tracking current timestamp. whenever `pq` is idle or tasks' enqueueTime is `<=` current timestamp, pop task from queue to `pq`
4. because our `pq` is single thread, pop one task at a time and update current time stamp
    - current timestamp comes from `current time + process time`
    - or `enqueue time + process time` when there is a gap before next task

# Complexity
- Time complexity:
$O(nlogn)$

- Space complexity:
$$O(n)$$

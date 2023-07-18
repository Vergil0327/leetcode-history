
# Intuition

shortest path -> think of BFS
our state: (row, col, removeTimes)
if we reach position in same state -> duplicate -> must avoid -> use **hashset** to prune duplicate

**edge case**

if we can remove `k` obstacles where `k >= ROWS-1 + COLS-1`, it means we are sure to reach the destination with minimum step, we can directly return `ROWS-1+COLS-1`.
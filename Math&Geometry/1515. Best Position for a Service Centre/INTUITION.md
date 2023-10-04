# Intuition

1. start with central point (sum(x)//n , sum(y)//n)
2. like BFS to search next possible closer position in 4 directions `[0,1],[0,-1],[1,0],[-1,0]`
3. since `0 <= xi, yi <= 100`, let's start **delta** with 100 such that:
    - next_x = x + x_direction * **delta**
    - next_y = y + y_direction * **delta**
4. just like binary search but in 2-D plane:
    - if we found (next_x, next_y) is greater candidate, update (x, y)
    - else we shrink our **delta** and move in smaller **delta** to explore closer position in 4 directions

5. find in binary search way until our precision is less than $10^5$
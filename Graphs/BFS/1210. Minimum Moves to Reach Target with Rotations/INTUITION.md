# Intuition

use BFS to explore minimum path

start with [p1,p2] = [(0,0),(0,1)]

- move down or move right
    - [[1,0],[0,1]]
    - p1[1]+1, p2[1]+1
    - p1[0]+1, p2[0]+1
- rotate clockwise if snake is horizontal same row but col diff == 1
    - p2[0]+1, p2[1]-1
- counterclockwise if snake if vertical same col but row diff == 1
    - p2[0]-1, p2[1]+1

return steps when p1 == (m-1,n-2) and p2 == (m-1, n-1)

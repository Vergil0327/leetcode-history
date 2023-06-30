# Intuition

thinking reversely:

from possible last day backward, find first occurence we can successfully reach to top row

since we wan to check if we can reach top row effeciently, and we just want to know if we **can** or **can't**, we can try using Union-Find.

first, we group land together and see if last row and top row are in the same group

then from last day to first day, each day we turn one flooded land back and try to union its neighbor together.

after that, we check if any column in last row is union with top row

# Optimized Solution

we can union row by row, and check at the same time.

[[Python] Union Find solution, explained](https://leetcode.com/problems/last-day-where-you-can-still-cross/solutions/1403930/python-union-find-solution-explained/)

# Intuition

concept is just like *1020. Number of Enclaves*

rather than traverse and find closed island, let's think reversely.

we can start from exterior border and flood all the island connected with border.

once we flood all the invalid island, the remains is what we want

we just iterate and count how many connected islands remain

# Approach

1. start from 4 exterior border and remove invalid island
2. count remaining closed islands (just find connected component)

# Complexity
- Time complexity:

O(ROWS * COLS)

- Space complexity:

O(1), only constant variables like `dirs`, `ROWS` & `COLS`
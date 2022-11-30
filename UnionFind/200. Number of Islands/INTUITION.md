1. iterate whole grid and union adjacent cell (up, down, left, right) whenever it is an island, i.e. `grid[row][col] = "1"`

2. then, iterate again and add parent to hashset

3. the size of set is answer

ps. we can use `key = row * COLS + col` eq. to hash 2-D coordinates into 1-D integer
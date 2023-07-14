# Intuition

at index=i position:
- if heights[i] <= heights[i-1], we can reach without any help
- if heights[i] > heights[i-1], `diff = heights[i] - heights[i-1]`, we can:
    1. use bricks
    2. use ladders

大致上想法肯定是如果diff過大, 就用ladders, 反之則用bricks即可
因此, 首先我們可以有個長度為ladders的sliding window
等到下一個大樓加進來後, 由於ladders已經用完, 那勢必得要有一個階層是用bricks來墊
那肯定是用diff最小的來墊

那延續這個Greedy的思想
我們大致上的想法就是維護一個長度為ladders的window
然後我們可以用一個min heap來找出window內的minimum difference, 並持續將那個min difference用bricks來取代
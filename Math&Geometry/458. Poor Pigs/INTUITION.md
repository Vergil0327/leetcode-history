# Intuition

1 pig -> t+1 results, survive, die at minutesToDie, die at minutesToDie*2, minutesToDie*3, ... die at minutesToDie*t

2 pig -> can get (t+1)^2 results, why?

依據(t+1)制bitmask來看, 兩隻豬就能有00, 01, 02, .., 0t, 分別代表一隻豬不喝, 另一隻豬在t^0, t^1, ... 喝

所以我們要找的是 (t+1)^x >= buckets

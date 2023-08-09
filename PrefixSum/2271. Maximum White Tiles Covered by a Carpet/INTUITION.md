# Intuition

first I come up with a solution that:

from tiles[i], we can use diff array to mark white tiles
```
presum[tiles[i][0]] += 1
presum[tiles[i][1]+1] -= 1
```
then, we can turn diff array into prefix sum array
now, we have prefix sum array to represent as white tiles we have until i position, and we can just use sliding window to find maximum covered tiles
covered = presum[i] - presum[max(0, i-carpetLen)]

```
        ___________ ->       ___________ ->   ___________
tiles = X X X X X X _ _ _ X X X _ X X X X _ _ _ _ _ _ X X X
                  i                   j
```

but by constraint, li <= ri <= 10^9, it's quite a long range for us to find answer.
we'll get TLE or MLE.

so, maybe we can iterate each tiles and put carpet at tiles[i][0] and cover [tiles[i][0],tiles[i][0]+carpetLen-1].
it's intuitively to think that putting carpet at the starting position of consecutive white tiles is a reasonable greedy method.

thus, we can iterate each tiles and see how many tiles we can cover, choose globally maximum covered number.

for each iteration, we can cover from `starting point = tiles[i][0]` to `ending point = tiles[i][0]+carpetLen-1`

```
        _______________
tiles = X X X X X X _ _ _ X X X _ X X X X _ _ _ _ _ _ X X X
              i             j
```
move j until tiles[j][1] > ending point

covered = presum[j-1]-presum[i-1]
*note. if we use 1-index, covered = presum[j] - presum[i]*

but it can be this situation, carpet cover a little bit of next tiles
```
        ___________________
tiles = X X X X X X _ _ _ X X X _ X X X X _ _ _ _ _ _ X X X
              i             j

covered = presum[j]-presum[i] (1-indexed)
covered += ending_point - tiles[j][0] + 1 where both ending_point and tiles[j][0] are inclusive and ending point = tiles[i][0] + carpetLen - 1
```

thus, from both situation, we can conclude that
covered = presum[j]-presum[i] + max(0, endpoint - tiles[j][0] + 1)
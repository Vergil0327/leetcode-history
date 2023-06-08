# Intuition

since arrows.length == 12, if we try backtracking, 2^12 = 4096
we can find 1 valid combination out of 4096.

and we can use pick or skip strategy for backtracking

for each i position, bob can skip all try to win.
if bob try to win:
`state[i] = min(remainArrows, aliceArrows[i]+1)`

then:
`points+i if state[i] > aliceArrows[i] else points`


remember to use all of remainArrows.
if we we still have remain arrows at base case, use all of them in 0-th position because it doesn't affect points.

or we can use all of them in any other position and calculate points:

ex.
```py
if remainArrows != 0:
    if state[-1] <= aliceArrows[-1] and state[-1] + remainArrows > aliceArrows[-1]:
        points += n-1
    state[-1] += remainArrows
```
# Intuition

+/- 1, 2, 3, 4, ..., i
brute force -> BFS -> TLE/MLE definitely

+1 +2 = +3
-1 -2 = -3
+1 -2 = -1
-1 +2 = +1

maybe we can use two steps for +/- 1 for fine-tuning?

since `1 + 2 + 3 + ... towards target = (1 + numMoves) * numMoves // 2`, we can use binary search to find first >= target position (upperbound of binary search)

if we reach `first >= target` position, the next thing is how we step back to reach target?

- if position == target: directly return numMoves

- if position-target is even, we can turn (position-target)//2 -th move into negative
    ex. position=6,  target=4 => 1-st move to negative -> +1 becomes -1 => 6-2 = 4

- if position-target is odd, since odd = even + 1:
if next numMoves = odd => next_position-target will be even and we can just like above, turn 1 position into negative to reach target.
thus, if next numMoves = odd, it cost 1 extra step. (1 step forward and turn one of previous step into negative)
else, need two extra step to make distance even.

ex. target=2
2 steps: 1+2=3 => 3-target=1 and next step is +3
position_after_next_step-target = 4
=> we can just turn (4/2)-th step into negative => +2 becomes -2 => +1-2+3 = 2 == target
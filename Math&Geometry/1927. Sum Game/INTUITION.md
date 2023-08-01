# Intuition

we only care **difference** between left half and right half and **how many questionmark we can replace**.

```py
leftCnt = rightCnt = diff = 0
n = len(num)
for i, ch in enumerate(num):
    if i < n//2:
        if ch == "?":
            leftCnt += 1
        else:
            diff += int(ch)
    else:
        if ch == "?":
            rightCnt += 1
        else:
            diff -= int(ch)
```

since they take turns to operate, bob can always eliminate Alice's operation
and these operations we don't care because they make no difference

```py
d = min(leftCnt, rightCnt)
leftCnt -= d
rightCnt -= d
```

- if leftCnt == 0 and rightCnt == 0, there is nothing we can do, return diff != 0
- if (leftCnt+rightCnt)%2 == 1 => Alice can make last move to change difference => Alice always win

- if leftCnt > 0 and diff >= 0, Bob can't decrease diff => Alice win
- if rightCnt > 0 and diff <= 0, Bob can't increase diff => Alice win

then, `remainRounds = max(leftCnt, rightCnt)//2`
no matter what digit Alice pick, [0,9], Bob can always pick the other to make their sum equal 9
```
Alice Bob
 0    9
 1    8
 2    7
 3    6
 4    5
 5    4
 6    3
 7    2
 8    1
 9    0
```

thus, if `abs(diff) == 9 * round`, bob will win
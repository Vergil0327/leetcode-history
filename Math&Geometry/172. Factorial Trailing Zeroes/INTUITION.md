### Brute Force Solution

brute force to compute n!
and keep dividing by 10 to count zeros

### Better Solution

only multiple of 5 multiply multiple of 5 can generate 10
ex. 2 * 5 = 10, 4 * 15 = 60

since 2, 4, 6, 8, 10, 12..., multiples of 2 are much more than multiple of 5
thus, what we want is **how many factor of 5 in n!**.
we only need to consider factor of 5

ps.
such as 5, 10, 15, 20, 25, ...
25 = 5*5 -> can contribute `2` digits of zero

### Optimal Solution (Follow-up)

extend the concept of better solution
take n = 200 for example:
```
if n = 200
200 // 5 = 40, we've got 40 of 5, each can contibute 1 zeros
200 // 25 = 8, we've got 8 of 5, each can contibute 1 MORE zero than 5
200 // 125 = 1, we've got 1 of 5, each can contibute 1 MORE zero than 25

ans = 40+8+1
```
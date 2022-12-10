### Observation

since each iteration we can start from `first` or `last`, which means we can collect all the odd piles or all the even piles.

therefore we can always choose greater piles from odd and even piles.

we always win

### Top-Down DP + Memorization

How many Alice can collect?

alice can choose either first or last, and so can bob.
since both of them take turns to pick.
whole game is just like **recursion**

let's discuss in two cases:

- Alice choose first:

if Alice choose first pile, `piles[0]`, Bob can also choose either first or last from rest of piles.

in this turn, we can define alice's and bob's piles as:

```python
alice = piles[0]
bob = stoneGame(piles[1:])
```

thus, Alice **totally** can get `piles[0]+sum(piles)-bob`

- Alice choose last:

if Alice choose last pile, `piles[-1]`, Bob can also choose either first or last from rest of piles.

in this turn, we can define alice's and bob's piles as:

```python
alice = piles[-1]
bob = stoneGame(piles[:-1])
```

thus, Alice **totally** can get `piles[-1]+sum(piles)-bob`

and we choose greater total in these two possibilities

at last, we check if alice's total is greater than bob's or not

### Bottom-Up DP

[Lee215's solution](https://leetcode.com/problems/stone-game/solutions/154610/dp-or-just-return-true/)

dp[i][j] means Alice's greatest collection than bob's from piles[i] to piles[j]

if Alice choose piles[i], she must give up the best result she can get from dp[i+1][j] since alice and bob take turns to pick pile.

thus, current alice's piles is `piles[i] - dp[i+1][j]`

vice versa, if Alice choose piles[j], current alice's piles is `piles[j] - dp[i][j-1]`

therefore, our recursive eq. should be:

```
dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
```


**base case**:

for every i=j, the best we can get is piles[i] (= piles[j])
thus, dp[i][i] = piles[i] where i from 0 to n-1
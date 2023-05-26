Think our decision tree:

1. alice takes from piles[i] ... piles[i+X] `1<=X<=M`
2. then, bob takes from piles[i+X+1] ... piles[i+X+1+X']
3. alice and bob always takes optimal maximum score in his/her own turn,
   which means they share the same strategy.
   thus, our recursion function should works for both of them
4. and we can try all the possible `M` at each turn which means we traverse all the decision tree to find maximum score

```markdown
The key point is `how to find alice's score when alice and bob take turns in recursion` ?
```

If piles = [XXXXXYYYYZZZ], and Alice already takes `XXXXX`.
Now if Bob decides to take `YYYY`, then Alice's score should be `XXXXX` + `ZZZ`

[{XXXXX}YYYY{ZZZ}] -> `ZZZ` = `sum(rest of piles)` - Bob's `YYYY`
 Alice  Bob  Alice          = `SuffixSum[j]` - `YYYY`

Therefore, our recursion can be written as `alice's + SuffixSum[j] - Bob's`
-> see line 18. in solution.py

Solution 2:

we can also define `alice's max points = total points - min(bob's points)`

# Daily Challenge May., Day26 2023

# Intuition

It's intuitively to use top-down recursion to simulate stone game.

=> use DFS to explore all possible ways for alice.

let's define DFS return maximum score of alice:

for i-th turn, total remaining score is `sum(piles[i:])`
since bob can take `bob := dfs(j+1, max(M, x))` totally, alice can take `sum(piles[i:]-bob)` totally

and we choose maximum possible value for Alice `res = max(res, sum(piles[i:])-bob))`

```
# Stone Game

res = 0
for j in range(i, min(i+M*2, n)):
    x = j-i+1
    # alice = (presum[j]-presum[i]) + (presum[n]-presum[j])
    #               take                   remaining
    alice = presum[n]-presum[i]
    bob = dfs(j+1, max(M, x))
    res = max(res, alice-bob)
```

# Complexity
- Time complexity:
$$O(n^3)$$
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
$$O(n^2)$$

# Code
```
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        presum = [0] * (n+1)
        for i in range(1, n+1):
            presum[i] = presum[i-1] + piles[i-1]

        memo = [[-1]*(n+1) for _ in range(n+1)]
        def dfs(i, M):
            if memo[i][min(M, n)] != -1:
                return memo[i][min(M, n)]

            res = 0
            for j in range(i, min(i+M*2, n)):
                x = j-i+1
                # alice = (presum[j]-presum[i]) + (presum[n]-presum[j])
                #              curr                   remaining
                alice = presum[n]-presum[i]
                bob = dfs(j+1, max(M, x))
                res = max(res, alice-bob)

            memo[i][min(M, n)] = res
            return res

        return dfs(0, 1)
```
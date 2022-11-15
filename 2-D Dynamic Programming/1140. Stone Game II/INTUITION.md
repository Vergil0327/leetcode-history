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
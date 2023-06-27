# Intuition

see example 1.
it can be generalized as `[XXXXXXX]YYYY[XXXXXXX]`

once prefix `[XXXXXXX]` equals suffix `[XXXXXXX]`, we can further explore if we can split
`[YYYY]` into `[ZZZ]...[ZZZ]`
=> `[[XXXXXXX][ZZZ]...[ZZZ]][XXXXXXX]]`

thus:
1. once text[:i] == text[j:], dfs(text[i:j]) + 2
2. **base case**, return 1 if text else 0
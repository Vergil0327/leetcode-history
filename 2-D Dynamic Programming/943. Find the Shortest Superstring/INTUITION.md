# Intuition

try every possible combination with bitmask as picking state since 1 <= words.length <= 12
ex. 100 means we've alreayd picked words[2] in our superstring

fintal state: pick all the words => bitmask state == (1<<n)-1

but the hard part is how to merge current superstring with words[j] where 0 <= j < n and (state>>j)&1 == 0

in order to get shortest superstring, we need to merge common part as much as possible.
=> check current pick (words[j]) with last pick (words[i]) and choose best => as many common parts as possible

ex. example 2:

```
       gctaagttcatgcatc
step 1:gcta
step 2: ctaagt
step 3:      ttca
step 4:        catg
step 5:         atgcatc
```

=> we can use O(N^2) to check if prefix of current pick is suffix of last pick:
```py
def merge(s, t):
    m, n = len(s), len(t)
    for k in range(min(m, n), -1, -1):
        if s[m-k:] == t[:k]:
            return s+t[k:]
    return s+t
```

**dp state transition**

define dp[state][last_pick]: the shortest length of superstring for current state with last word we pick is `last_pick`

and we define another helper func to check distance between two pick:
if current_pick is `ctaagt` and last_pick is `gcta`, their distance is 3 because we only need to concat `agt` in current_pick with last_pick

core concept:

n = len(words)
maxState = 1<<n
for current_state in range(maxState):
    for last_pick in ...:
        prev_state = current_state - last_pick
        for prev_last_pick in ...:
            dp[current_state][last_pick] = dp[prev_state][prev_last_pick] + helper(prev_last_pick, last_pick)

because we need to return final result string, we store `parent[state][last_pick] = prev_last_pick` for us to restore final result

[great explanation for this solution here, by HuifengGuan](https://www.youtube.com/watch?v=VWUpNRvhLkQ&ab_channel=HuifengGuan)
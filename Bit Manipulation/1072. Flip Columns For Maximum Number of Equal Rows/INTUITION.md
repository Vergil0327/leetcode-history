# Intuition

if rows[i] after some K flips become `0000000...`, and so do rows[j]

then rows[i] must equal row[j] after K flips

and if rows[k] become `1111....` after K flips, then rows[k] must equal totally opposite rows[i]

example.
```
[1,0,0,1,0] -> [0,0,0,0,0] # all-0s

after flipping every cell in 0-th and 3-th columns
[1,0,0,1,0] -> [0,0,0,0,0] # all-0
[1,0,1,1,1] -> [0,0,1,0,1]
[0,1,1,0,1] -> [1,1,1,1,1] # all-1
[1,0,0,1,1] -> [0,0,0,0,1]
[1,0,0,1,0] -> [0,0,0,0,0] # all-0

[1,0,0,1,0] -> [0,0,0,0,0] 
[0,1,1,0,1] -> [1,1,1,1,1]
-> totally opposite

```

thus, [1,0,0,1,0] and [0,1,1,0,1] belongs to the same pattern
we both increase 1 in hashmap

```
hashmap[(1,0,0,1,0)] + 1
hashmap[(0,1,1,0,1)] + 1
```

and we choose maximum value in hashmap. that will be our answer
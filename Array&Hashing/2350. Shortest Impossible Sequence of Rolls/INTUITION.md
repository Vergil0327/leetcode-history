# Intuition

add rolls[i] to set from i=0 to i=n-1
until len(set) == k: we finish sequence whose length equals 1

if we want to check seq. whose length=2,
we need another len(set) == k starting from previous finished index

```
X X X X X X X X X
        i
```
if we already have all the sequence with length=1 at i,
we can keep starting from i to find another sequence with length=1
and these two 1-length seq. can combine together to form seq. with length = 2

if we already have n-length seq., we need extra {1,2,3, ..., k} after this n-length seq. to get n+1-length seq.

```
rolls = {1,2,3, ..., k} + {1,2,3, ..., k} + {1,2,3, ..., k} + ...
length         1                2                3
```
# Intution

- for each num, iterate over all possible 32 bits and add bit by bit
- We evaluate this each bit modulo 3. Note, that in the end for each bit we can have either 0 or 1 and never 2.
- restore our answer with evaluated bit.
- Finally, we need to deal with overflow cases in python: maximum value for int32 is 2^31 - 1, so if we get number more than this value we have negative answer in fact.

```
ex. [3,3,3,2]

  11
  11
  11
+ 10
= 43
% 10

after we take modulo at each bit position, every nums repeated 3 times will be removed, and we got final answer
```
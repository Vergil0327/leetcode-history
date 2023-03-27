### Top-Down + Memorization

#### Intuition

time: `O(n * target)  = O(9 * target) = O(target)`

1. since we need to know mapping from cost to digit, we can use `hashmap` to help us. and we construct hashmap reversely because we want to build digits with largest index
   - ex. if we have duplicate number [`25`, ..., `25`], one represent `digit 1` the other represent `digit 9`. we want to use `digit 9` rather than `digit 1`
2. we can use take-or-skip DFS strategy to find valid candidate answer
	1. if we can't find any valid candidate, we can use any placeholder to represent as invalid answer for us to memorization and prune branches. here I use `"N"`.
	2. if we find valid answer, return larger one. 
we can compare string's length and use numeric string itself as tie-breaker
ex. "1111" > "11" and "4321" > "1234"

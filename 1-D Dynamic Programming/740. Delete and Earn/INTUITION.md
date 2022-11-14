### Intuition

See `Example 2` (or `Hint`)
```
1st round if we pick 2 at index 0
nums: [2,2,3,3,3,4]
	   i
points += 2 and we need to give up every 3 and 1.
thus,  nums become: [2,2,X,X,X,4]

2nd round we can pick 2 at index 1, and nums is stil the same as before
nums: [2,2,X,X,X,4]
		 i
```

if we start from index 2 to pick 3, the iteration is still the same.
this means **if we choose nums[i], we can pick them all at once**

### Trick

Since 
1. every time we pick `nums[i]`, we need to skip `nums[i]-1` and `nums[i]+1` 
2. we don't need to pick `nums[i]` in order.

which means we can sort the array so that we can skip `nums[i]+1` easily and get rid of `nums[i]-1` at the same time if we pick `nums[i]` in order

### Algorithm

1. sort array
2. use DFS to traversal all the possibilities (take or skip strategy)
	- skip index `i`, try index `i+1`
	- take index `i`, try index `j`, where `j` is index after skipping all the `nums[i]` & `nums[i]+1`
3. choose max points. `answer = max(take, skip)`

kind of like a `house robber` problem but in value domain.
`if we pick nums[i] we can't pick nums[i]'s neighbor`
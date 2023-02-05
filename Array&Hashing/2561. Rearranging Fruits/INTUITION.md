# Intuition

first, I try to find all the num we need to swap

1. count basket1, store extra value in `arr1`
2. count basket2, store extra value in `arr2`
3. if there is any value which can't be split evenly, return `-1`

then we can greedily swap by pairing up minimum value in `arr1` with maximum value in `arr2`

but there is still another strategy hard to come up with, we can swap value in `arr1` and `arr2` with minimum value.

ex. 
minimum value = 4
arr1 = [24]
arr2 = [28]

if minimum value in arr1, we can swap 28 with minimum value first, then swap 24 with minimum value.
in the end, minimum value is still in original array, and we cost `2 * minimum value = 2 * 4` rather than `min(24, 28)`

therfore, we iterate through `arr1[i]` and choose `min(2 * minValue, min(arr1[i], arr2[n-1-i])` as cost

```py
arr1.sort() # swap value in basket1
arr2.sort() # swap value in basket2

minValue = min(min(basket1), min(basket2))
minCost = 0
n = len(arr1)
for i in range(n):
    minCost += min(2*minValue, min(arr1[i], arr2[n-1-i]))
return minCost
```
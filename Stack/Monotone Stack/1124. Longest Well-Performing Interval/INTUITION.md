# Intuition

## step 1
[tiring day consecutive interval] X X X [tiring day consecutive interval]
 j'                            i'        j                             i

if # of tiring days within [j':i] > # of non-tiring days [i'+1:j-1], we can see [j':i] as well-performing interval

we can see hours[i] > 8 as 1 and hour[i] <= 8 as -1
then, hours become something like [1,1,-1,1,-1,...]

then what we want is an interval whose sum is greater than 0.
=> if we use prefix sum to represent this, we can say that:
if well-performing interval is [j:i], presum[i]-presum[j] > 0

hours = [6,9,9] => presum = [-1,0,1]
hours = [9,9,6] => presum = [1,2,1]

## step 2
for presum[i], we want find a smallest j to make presum[i]-presum[j] > 0
=> we want prevSmaller with smallest index
=> monotonic stack

if monotonic stack stores strictly decreasing presum, we can easily get valid prevSmaller presum[j]
ex. monostack = [presum[j], presum[j'], presum[j''], ...]

```
for current presum[i]:
    while monostack and (presum[j := monostack[-1]] < presum[i]):
        res = max(res, i-j)
        monostack.pop()
```

note:
if there exist another presum[j'''] == presum[j'] which means monostack = [presum[j], presum[j'], presum[j''], presum[j'''] ...],
we only need presum[j'] because the len([j':i]) > len([j''':i])

therefore:
```py
monostack = []
for i in range(n):
    if not monostack or presum[i] < presum[monostack[-1]]:
        monostack.append(i)
```

## step 3
for current presum[i], we can also find nextGreater presum[j] to make presum[j]-presum[i] > 0 and we want miximize j to make len([i:j]) as larger as possible.

if presum[i] - presum[j] > 0 and presum[i-1] - presum[j] > 0 where j < i-1 < i
=> len([j:i-1]) < len([j:i])
=> thus, if we found [j:i] is valid, we don't need to keep j in monostack anymore. because len([j:i]) > len([j:i-1])
=> if we iterate backwards, we can keep popping monostack and find valid [j:i]
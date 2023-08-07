# Intuition

target = [X X X X X ...]

we start from x = n, where x = sum(arr), and we can set arr[i] to x.
since x only grows bigger, sort target in order first then check.
 
there are so many possible ways to start from [1,1,1,...] to target,
since the largest one must be the last one we set, we can backtrack reversely, then there is only one way to make target back to [1,1,1,1,...]

ex.1 target = [3,5,9] -> [3,5,1] -> [3,1,1] -> [1,1,1]
ex.3 target = [5,8] -> [5,3] -> [2,3] -> [2,1] -> [1,1]

after we reverse operation, current maximum element is always the last move we do.
therefore, while reverse operation, we always choose maximum element and substract sum of rest of array
=> we need max heap to keep tracking current maximum element and one variable to store current sum

```py
def isPossible(self, target: List[int]) -> bool:
    maxHeap = [-v for v in target]
    heapq.heapify(maxHeap)

    tot = sum(target)
    while -maxHeap[0] != 1:
        curMax = -heapq.heappop(maxHeap)
        otherSum = tot-curMax
        prev = curMax - otherSum
        tot = otherSum + prev
        if prev < 1: return False
        heapq.heappush(maxHeap, -prev)
    return True
```

but we'll get **TLE** in this case: target = [1,1000000000]

from this testcase, we can know that once curMax is much greater than otherSum, we can use division.
then previous value of current max will be **curMax%otherSum**

then we need to check condition again.

1. `if prev < 1: return False` is no more valid:
ex. target = [8,5] => [3,5] => [3,2] => [1,2] => [1,1] but we get prev == 0 at this round

2. when will `curMax%otherSum` no more valid?
    - otherSum == 0. since we start with a [1]*n array, other sum can't be zero
    - curMax <= otherSum. since curMax = prev + otherSum where prev >= 1 and otherSum >= n, curMax must be greater than otheSum

therefore:
```py
if otherSum == 0 or curMax <= otherSum: return False
prev = curMax % otherSum
```

but, we still fail at this testcase `[1,1,10]`.

cause:
prev = 10%2 = 0 => since element can't be 0, we should handle this edge case:
once prev == 0, let's don't substract down to zero, we substract until prev = otherSum.
*i.e. if prev == 0: prev = (prev%otherSum) + otherSum*
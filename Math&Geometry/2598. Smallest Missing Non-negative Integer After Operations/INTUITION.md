# Intuition

since we want find MEX, we can process every `nums[i]` to its minimum non negative value first by operation.


X X X X X X X X X X X 0 X X X X X X X X X X X
  +Value towards 0 ->    <- -Value towards 0

and this can easily be done by modulo
```py
n = len(nums)
for i in range(n):
    nums[i]%=value
```

and this modulo also remind us how to find possible value we can transform into MEX.

we can think every `MEX = modulo + k * Value`
once we come up with this formula, this problem is easy to solve.

let's store all the nums[i] we have in hashmap first:
```py
counter = Counter(nums)
```

and let's start to find MEX from 0:

- if `MEX%value` in couter, it means we have a `nums[i]` can transform into MEX
- if `MEX%value` not in counter, it means we can't transform any `nums[i]` to MEX

# Complexity
- Time complexity:
$$O(n)$$

- Space complexity:
$$O(n)$$

# Code
```
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        for i in range(n):
            nums[i]%=value
        
        counter = Counter(nums)
        MEX = 0
        while True:
            if MEX%value in counter:
                counter[MEX%value] -= 1
                if counter[MEX%value] == 0:
                    del counter[MEX%value]
                MEX += 1
            else:
                break
        
        return MEX
```
# Intuition

first of all, if we want to get maximum score, we need choose nums[i] in **decreasing order**

see example.2 nums = [19,12,14,6,10,18], k = 3
1. choose 19
2. then, choose 18
3. then, choose 14
4. then, choose 12
...

for each nums[i], we can use monotonic stack to find index of nums[i]'s prevGreaterPrimescore and index of nums[i]'s nextGreaterPrimeScore

```
nums = X X X X X X X X X X X X X X X X
                 l       i       r
```

if l = prevGreater[i] and r = nextGreater[i]
then we have (i-l) * (r-i) subarray for us to pick and all the subarray's `x` is nums[i]

thus, our `res *= pow(nums[i], (i-l)*(r-i), 10**9+7)` 

so, combine above discussion:

1. we calculate each nums[i]'s prime score first

```py
primeScore = []
for num in nums:
    primes = set()
    for p in range(2, int(sqrt(num))+1):
        if num%p == 0:
            primes.add(p)
            while num%p == 0:
                num //= p
    if num > 1:
        primes.add(num)
    primeScore.append(len(primes))
```

2. find left boundary and right boundary of nums[i]
   - store left boundary in prevGreater array
   - store right boundary in nextGreater array

we can use monotonic stack to find prevGreaterPrimescore and nextGreaterPrimescore

```py
# stack = [5 4 3 2 1], p=3
prevGreater = [-1]*n
stack = []
for i, p in enumerate(primeScore):
    while stack and primeScore[stack[-1]]  < p:
        stack.pop()
    if stack:
        prevGreater[i] = stack[-1]
    stack.append(i)

# stack = [5 4 3 2 1], p=3
nextGreater = [n]*n
stack.clear()
for i, p in enumerate(primeScore):
    while stack and p > primeScore[stack[-1]]:
        nextGreater[stack.pop()] = i
    stack.append(i)
```

3. greedily pick nums[i] in decreasing order
    - sort nums first in decreasing order. if there is a tie, break by smallest index
    - find number of subarray we can pick whose `x` is nums[i].
        - the number is `(i-prevGreater[i]) * (nextGreater[i]-i)`
    - apply x to our current score
      - `res *= pow(num, left*right, mod)` if `k >= (i-prevGreater[i]) * (nextGreater[i]-i)` and `k -= left*right`
      - else `res *= pow(num, k, mod)` if `k < (i-prevGreater[i]) * (nextGreater[i]-i)` and `k = 0`

time: O(nlogn)
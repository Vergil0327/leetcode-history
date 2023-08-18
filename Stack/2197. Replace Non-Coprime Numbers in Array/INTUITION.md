# Intuition

see example 1.
nums = [6,4,3,2,7,6,2]

i=0
res = [6]
nums = [_,4,3,2,7,6,2]

i=1, gcd(res[-1], nums[i]) != 1 => res[-1] = lcm(res[-1], nums[i]) = 12
res = [12]
nums = [_,_,3,2,7,6,2]

i=2, gcd(res[-1], nums[i]) != 1 => res[-1] = lcm(res[-1], nums[i]) = 12
res = [12]
nums = [_,_,_,2,7,6,2]

i=3,gcd(res[-1], nums[i]) != 1 => res[-1] = lcm(res[-1], nums[i]) = 12
res = [12]
nums = [_,_,_,_,7,6,2]

i=4,gcd(res[-1], nums[i]) == 1
res = [12,7]
nums = [_,_,_,_,_,6,2]

i=5,gcd(res[-1], nums[i]) == 1
res = [12,7,6]
nums = [_,_,_,_,_,_,2]

see examle 2:

res = [2]
nums = [_,2,1,1,3,3,3]

res = [2]
nums = [_,_,1,1,3,3,3]

res = [2,1]
nums = [_,_,_,1,3,3,3]

res = [2,1,1]
nums = [_,_,_,_,3,3,3]

res = [2,1,1,3]
nums = [_,_,_,_,_,3,3]

res = [2,1,1,3]
nums = [_,_,_,_,_,_,_]

first, think brute force solution -> simulate it

**for each nums[i], it has left-neighbor and right-neighbor**

first, let's check left-neighbor:
we can push nums[0] into res first, then check gcd(res[-1], nums[i]) from i=1 to i=n-1
```py
res = [nums[0]]
n = len(nums)
for i in range(1, n):
    if gcd(res[-1], nums[i]) == 1:
        res.append(nums[i])
    else:
        res[-1] = lcm(res[-1], nums[i])
```

after we process all of nums from left to right, we should process once again from right to left to check right-neighbor:

```py
nums = res
res = [nums[-1]]
n = len(nums)

allCoprime = True
for i in range(n-2, -1, -1):
    if gcd(res[-1], nums[i]) == 1:
        res.append(nums[i])
    else:
        allCoprime = False
        res[-1] = lcm(res[-1], nums[i])

res.reverse()
```

then, we recursively process res until any two adjacent number are coprime:
thus, we use a variable `allCoprime` to check if we should continue recursively process:

```py
if allCoprime: return res
return self.replaceNonCoprimes(res)
```

# Other Solution - One Pass

do operation until current element is coprime

```py
def replaceNonCoprimes(self, nums):
    res = []
    for num in nums:
        while True:
            x = math.gcd(res[-1] if res else 1, num)
            if x == 1: break # co-prime
            num *= res.pop() // x # lcm
        res.append(num)
    return res
```
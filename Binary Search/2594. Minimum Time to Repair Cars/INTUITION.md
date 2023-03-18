# Intuition

first, we want to find the minimum time to fix all the cars.
once we need to find maximum or minimum, we can try **Binary Search**.

the more time we have, the more cars we can fix.
the less time we have, the less cars we can fix.
if we can't fix `n` cars under `mid` time, we can't fix `n+1` cars under `mid` time either

it turns out the relation of time and fixed cars is monotonical.
thus, we can use binary search.

ok, then the high level view to solve problem by binary search should be something like this:

```py
l, r = 0, int(1e14)
while l < r:
    mid = l + (r-l)//2
    if check(mid):
        r = mid
    else:
        l = mid+1
return l
```

the search space should be:
[0, $max(ranks[i]) * max(cars)^2$] = [0, 100 * $10^{12}$] = `[0, 1e14]`,
since `1 <= ranks[i] <= 100` and `1 <= cars <= 10^6`

then we just try to find a method to check if we can fix all the cars under `mid` time limit.

since `1 <= ranks[i] <= 100` and `1 <= ranks.length <= 10^5`, it must contains lots of duplicate `ranks[i]`
thus, we can use hashmap to store count of each `ranks[i]`
```py
counter = Counter(ranks)
```

for each mechanics with `ranks[i]` under `mid` time limit, it can fix `int(sqrt(timeLimit//r))` cars.
>`r * n^2 = time`

for every mechanic with same `ranks[i]`, they can fix `int(sqrt(timeLimit//r)) * counter[ranks[i]]`

thus, we just iterate through every mechanics without duplicate and check if our `fixed cars >= cars`:

```py
counter = Counter(ranks)
def check(timeLimit):
    fixed = 0
    for r in counter.keys():
        n = int(sqrt(timeLimit//r))
        fixed += n * counter[r]
    return fixed >= cars
```

# Complexity
- Time complexity:
$$O(nlogn)$$

- Space complexity:
$$O(ranks[i])$$

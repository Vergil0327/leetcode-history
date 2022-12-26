# Segment Tree + Recursion

## Intuition

let's start with `base=0` initially and our target is make every point's base value equal to `target`.

the optimal way is to find the minimum of inverval and increment every value in that interval together

```
Example 1:
target=[1,2,3,2,1], initial=[0,0,0,0,0] (base = 0)
round 1: [0,0,0,0,0] -> [1,1,1,1,1] increment in range from 0 to 4 (both inclusive)
round 2: [1,1,1,1,1] -> [1,2,2,2,1] increment in range from 1 to 3 (both inclusive)
round 3: [1,2,2,2,1] -> [1,2,3,2,1] increment in range from 2 to 2 (both inclusive)
```

thus, we need to be able to find rangeMinValue and its index efficiently.

-> `Segment Tree` can help us find rangeMin and its position

and we just find rangeMin by segment tree and increment base to target recusively

by description:
`In one operation you can choose any subarray from initial and increment each value by one.`

therefore, each time we increase `base` to `rangeMin`, operations per each round is `rangeMin-base` and we'll get answer after we sum up all the operations of each recursion.

core logic:
```python
def dfs(l, r, base):
    if l > r: return 0
    if l == r: return target[l]-base

    rangeMin, idx = seg.query(l, r)

    inc = rangeMin-base
    inc += dfs(l, idx-1, rangeMin)
    inc += dfs(idx+1, r, rangeMin)
    return inc
    
return dfs(0, n-1, 0)
```

## Complexity

- time complexity
$$O(nlogn)$$

- space complexity
$$O(n)$$

# Greedy

## Intuition

一樣是base = 0往上加的概念

我們只要考慮往上遞增的區間即可

ex. [1,2,3,2,1]
一開始base=0
i=0, nums[i]=1, base = 0 -> operations=1-0 並更新 base = 1
i=1, nums[i]=2, base = 1 -> operations=2-1 並更新 base = 2
i=2, nums[i]=3, base = 2 -> operations=3-2 並更新 base = 3
i=3, nums[i]=2, base = 3 -> 這點其實屬於i=1的區間, 已包含在i=1那步的operations內了，僅更新 base = 2即可
i=4, nums[i]=1, base = 2 -> 這點則屬於i=0那段區間，在i=0時已同時將base從0加至1了，因此 operations = 0 並更新base = 1
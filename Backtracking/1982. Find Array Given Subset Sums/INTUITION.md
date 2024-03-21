# Intuition

一開始想法想到的brute force:
n=3, sums = x, y, z, x+y, x+z, y+z, x+y+z
=> sums中任選n個數, 看能不能組合出其他所有sums[j]

1. 任選n個數
2. 從n個數中遍歷[2,n]去組出sums
3. 確認是不是我們要的

TLE: C(m, n) * C(n, x) for x in [2, n]
```py
sums.sort()
sums = tuple(sums)

comb = itertools.combinations(sums, n)
for nums in comb:
    subset_sums = list(list(map(sum, itertools.combinations(nums, size))) for size in range(2, n+1))
    possible = [0] + list(nums) + [num for s in subset_sums for num in s]
    possible = tuple(sorted(possible))
    
    if tuple(sorted(possible)) == sums:
        return nums
return []
```
    
ex1. n=3, sums = [-3,-2,-1,0,0,1,2,3]

original=[x,y,z] where x <= y <= z

如果試著對sums**由小到大排序**, 可進一步得到:

sums = [negative, negative, negative, ..., positive, positive, positive, ...]

smallest sums[i]: sums[0] = sum(negative, ... for all negative)
largest sums[i] : sums[-1] = sum(positive, ... for all positive)

那2nd largest sums[i]呢?

1. largest sums[i] - smallest positive num
2. largest sums[i] + largest negative num

這時會發現:
1. smallest positive num = largest sums[i] - 2nd largest sums[i]
2. largest negative num  = 2nd largest sums[i] - largest sums[i]

如此一來, 我們能推測出兩種可能的original array[i] `num`, 可能為 smallest positive或largest negative
    
假設我們找出這個合法num後, 我們把sums[i]減去這個num, sums[i]' = sums[i]-num
同時想到的是, sums[i]-num後的subset sum必須存在於原本的sums[i]裡.
ex. sums[i] = x + y + z, 假設我們找到z, sums[i]' = sums[i]-z = x + y
sums[i]'必定是某個sums[j]

那麼扣掉num後的新的sums[i]'就是剩餘num的subset sum, 我們就能用一樣邏輯在找出下個num
    
一樣分情況討論:
1. smallest positive num `num1`的情況

這時sums[i]必須排除掉num1以及受num1影響的sums[i]-num1, 其中sums[i]-num1必須存在於原本sums裡
ex. sums = [0, x, y, z, x+y, x+z, y+z, x+y+z]

這時我們由大到小來排除, 假設當前我們找到的smallest positive num = x

sums[i]-x為:[0-x, 0, y-x, z-x, y, z, y+z-x, y+z]
但0-x, y-x, z-x跟, y+z-x並非原本的sums[i], 所以不可以加到sums'裡
最後sums' = [0, y, z, y+z] => sums'.size應為2^(n-1)

所以實際上我們可以由大到小去找合法sums[i]-x:

1. x+y+z - x = y+z => sums.remove(x+y+z) and sums.remove(y+z)
   - sums'.add(y+z)
2. x+z - x = z     => sums.remove(x+z) and sums.remove(z)
   - sums'.add(z)
3. x+y - x = y     => sums.remove(x+y) and sums.remove(y)
   - sums'.add(y)
4. x - x   = 0     => sums.remove(x) and sums.remove(0)
   - sums'.add(0)
    
```py
smallPos = sums[-1]-sums[-2]
sl1 = SortedList(sums)
if smallPos in sl1:
    nxt = []
    valid = True
    while sl1:
        maxSum = sl1[-1]
        if (v:=maxSum-smallPos) in sl1:
            nxt.append(v)
            sl1.remove(maxSum)
            sl1.remove(v)
        else:
            valid = False
            break
```

1. largest negative num `num2`

同樣地, sums[i]必須排除掉num2的影響, 找出合法sums[i]-num2
由於sums[i]-num2會變大, 所以我們由小到大遍歷排除

ex. sums = [-x, 0, y, z, -x+y, -x+z, y+z, -x+y+z], 假設num2 = -x

sums[i] - (-x)後剩餘的合法subset sum = [0, -x+y, -x+z, y+z]

```py
largeNeg = sums[-2]-sums[-1]
sl2 = SortedList(sums)
if largeNeg in sl2:
    nxt = []
    valid = True
    while sl2:
        minSum = sl2[0]
        if (v:=minSum-largeNeg) in sl2:
            nxt.append(v)
            sl2.remove(minSum)
            sl2.remove(v)
        else:
            valid = False
            break
```

排除後再繼續找下個可能num1, num2, 因此整個過程會是個遞歸形式

所以透過dfs + backtracking, 我們可以返回找到的第一個可行解
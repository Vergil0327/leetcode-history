# Intuition

we can rotate k where k within [0,n-1]
k=0, index = (i-0 + n)%n
k=1, index = (i-1 + n)%n
k=2, index = (i-2 + n)%n
=> rotated index = j = (i-k+n)%n
once nums[i] <= j, we got 1 point

we can iterate every possible k to find globally highest score,
but it'll be O(n^2) => TLE

```
res = 0
res = scores = 0
for k in range(n):
    cnt = 0
    for i in range(n):
        j = (i-k+n)%n
        if nums[i] <= j:
            cnt += 1
            
    if cnt > scores:
        scores = cnt
        res = k
```

since we want `nums[i] <= j = (i-k+n)%n` => `k <= (i-nums[i] + n)%n`
```
for nums[i]:
    if k <= (i-nums[i]+n) %n, nums[i] will get 1 point
```

thus, for each nums[i], we can mark its point range using diff array
ex. diff = [0,0,0,0,1,0,0,0,0,0,0,-1] => [0,0,0,0,1,1,1,1,1,1,1,0]
=> then we can know that only k within [1,1,1,1,1,1,1] range, nums[i] can contribute 1 point

```
index 0 1 2 3 4
ex1. [2,3,1,4,0]

k values-> 0 1 2 3 4
    idx
     0  2: 0 0 1 1 1 nums[i]>i
     1  3: 0 0 1 1 1 nums[i]>i
     2  1: 1 1 0 1 1 nums[i] <= i
     3  4: 0 0 0 0 1 nums[i]>i
     4  0: 1 1 1 1 1 nums[i] <= i
```

diff[k]: score difference by shift k times where `0 <= k < n`

```
for nums[i] <= i:
    idx = 0 1 2 3 4 5 6
    val = X X X 1 X X X
    1. k=0 already got 1 point: diff[0] += 1
    2. can get point by left-shifting to i-nums[i]: diff[i-nums[i]+1] -= 1
    3. can get point by left-shifting to right, [i,n-1] range: diff[i+1] += 1

for nums[i] > i:
    idx = 0 1 2 3 4 5 6
    val = X X X 5 X X X
    only get point when idx = 5 6 => [(idx-nums[i]+n)%n, n-1]
    1. diff[i+1] += 1
    2. diff[(idx-nums[i]+1+n)%n] -= 1
```